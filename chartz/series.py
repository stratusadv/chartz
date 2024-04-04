from dataclasses import dataclass, field
from enum import Enum
from typing import Union


class SeriesTypeEnum(Enum):
    LINE = 'line'
    BAR = 'bar'
    PIE = 'pie'


class SeriesLayoutByEnum(Enum):
    COLUMN = 'column'
    ROW = 'row'


@dataclass()
class BaseSeries:
    type: SeriesTypeEnum = field(default=SeriesTypeEnum.LINE)
    show_label: bool = True
    show_label_lines: bool = True

    def hide_labels(self):
        self.show_label = False
        self.show_label_lines = False

    def to_dict(self):
        return {
            'type': self.type.value,
            'label': {
                'show': self.show_label,
            },
            'labelLine': {
                'show': self.show_label_lines,
            }
        }


@dataclass()
class PieSeries(BaseSeries):
    type: SeriesTypeEnum = field(default=SeriesTypeEnum.PIE)
    radius: str = '90%'
    center: list[str] = field(default_factory=list)

    def __post_init__(self):
        self.center = ['50%', '50%']

    def position_chart(self, x: str, y: str):
        self.center = [x, y]

    def to_dict(self):
        return {
            **super().to_dict(),
            'radius': self.radius,
            'center': self.center,
        }


@dataclass()
class LineChartSeries(BaseSeries):
    type: SeriesTypeEnum = field(default=SeriesTypeEnum.LINE)
    series_layout_by: Union[SeriesLayoutByEnum, str] = field(default=SeriesLayoutByEnum.COLUMN)
    encode: dict = field(default_factory=dict)

    def __post_init__(self):
        if isinstance(self.series_layout_by, str):
            try:
                self.series_layout_by = SeriesLayoutByEnum(self.series_layout_by)
            except ValueError:
                raise ValueError(f'Invalid series layout by: {self.series_layout_by}')

    def configure(self, x_axis: str, y_axis: str):
        self.encode = {
            'x': x_axis,
            'y': y_axis,
        }

    def to_dict(self):
        return {
            **super().to_dict(),
            'seriesLayoutBy': self.series_layout_by.value,
            'encode': self.encode,
        }


def get_series(chart_type: str):
    try:
        series = SeriesTypeEnum(chart_type.lower())
    except ValueError:
        raise ValueError(f'Invalid chart type: {chart_type}')

    if series == SeriesTypeEnum.PIE:
        return PieSeries()
    elif series == SeriesTypeEnum.LINE:
        return LineChartSeries()
