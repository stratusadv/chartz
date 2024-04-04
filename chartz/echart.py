from dataclasses import dataclass
from typing import Union

from chartz.axis import XAxis, YAxis
from chartz.title import Title
from chartz.legend import Legend, LegendAlignEnum, LegendOrientEnum
from chartz.tooltip import ToolTip
from chartz.dataset import Dataset
from chartz.series import get_series, BaseSeries


@dataclass()
class Chart:
    title: str
    height: int = 300

    def __post_init__(self):
        self._title = Title(name=self.title)
        self._legend = Legend()
        self._tooltip = ToolTip()
        self._dataset = Dataset()
        self._series: list[BaseSeries] = []
        self._x_axis = XAxis()
        self._y_axis = YAxis()

    def add_dataset(self, data: list[list, tuple]):
        self._dataset.source = data
        return self._dataset

    def add_series(self, chart_type: str, show_labels: bool = True):
        series = get_series(chart_type)

        if not show_labels:
            series.hide_labels()

        self._series.append(series)
        return series

    def hide_axis(self):
        self._x_axis.hide()
        self._y_axis.hide()

    def hide_title(self):
        self._title.show = False

    def hide_legend(self):
        self._legend.show = False

    def show_title(self):
        self._title.show = True

    def show_legend(self):
        self._legend.show = True

    def position_legend(
            self,
            orientation: Union[str, LegendOrientEnum] = LegendOrientEnum.HORIZONTAL,
            left: Union[str, LegendAlignEnum, int, None] = None,
            right: Union[str, LegendAlignEnum, int, None] = None,
            top: Union[str, LegendAlignEnum, int, None] = None,
            bottom: Union[str, LegendAlignEnum, int, None] = None,

    ):
        self._legend.orient = str_to_enum(orientation.lower(), LegendOrientEnum)

        if left is not None:
            self._legend.left = str_to_enum(left.lower(), LegendAlignEnum)

        if right is not None:
            self._legend.right = str_to_enum(right.lower(), LegendAlignEnum)

        if top is not None:
            self._legend.top = str_to_enum(top.lower(), LegendAlignEnum)

        if bottom is not None:
            self._legend.bottom = str_to_enum(bottom.lower(), LegendAlignEnum)

    def to_dict(self):
        return {
            'title': self._title.to_dict(),
            'legend': self._legend.to_dict(),
            'tooltip': self._tooltip.to_dict(),
            'dataset': self._dataset.to_dict(),
            'series': [s.to_dict() for s in self._series],
            'xAxis': self._x_axis.to_dict(),
            'yAxis': self._y_axis.to_dict(),
            'containerHeight': self.height,
        }

    @property
    def y_axis(self):
        return self._y_axis

    @property
    def x_axis(self):
        return self._x_axis
