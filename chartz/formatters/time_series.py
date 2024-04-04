from abc import ABC
from dataclasses import dataclass
from datetime import date

from app.chart.enums import ChartIntervalEnum
from app.chart.utils import get_range_calculator

from app.core.utils import RangeCalculator


@dataclass()
class TimeSeriesDataPoint:
    value: float
    reference_date: date


class TimeSeriesLabel:
    def __init__(self, start_date: date, end_date: date, interval: ChartIntervalEnum):
        self.start_date = start_date
        self.end_date = end_date
        self.interval = interval
        self.range_calculator: RangeCalculator = get_range_calculator(start_date, end_date, interval)

    def generate_labels(self):
        labels = []
        while self.range_calculator.start_date <= self.end_date:
            labels.append(self.range_calculator.start_date.strftime('%b %d'))
            self.range_calculator.increase_range()

        # Append the end date if it is not the same as the start date
        if self.range_calculator.start_date < self.end_date:
            labels.append(self.end_date.strftime('%m/%d/%Y'))

        return labels


class TimeSeriesDataFormatter(ABC):
    """
        Formats chart data based on an interval and calculation type.
    """
    def __init__(
            self,
            data: list[TimeSeriesDataPoint],
            start_date: date,
            end_date: date,
            interval: ChartIntervalEnum
    ):
        self.data = data
        self.range_calculator = get_range_calculator(start_date, end_date, interval)

    def average(self) -> list:
        interval_end = self.range_calculator.next_range_start_date()

        formatted_data = []
        value_sum = 0

        for (index, data_point) in enumerate(self.data, start=1):
            if data_point.reference_date >= interval_end:
                # Returns the average
                formatted_data.append(value_sum / self.range_calculator.days_between_interval())

                self.range_calculator.increase_range()
                interval_end = self.range_calculator.next_range_start_date()

                value_sum = 0

            # Update this if we need to pull other values from the field (JSON values)
            value_sum += data_point.value

            # Add the last set of statistics
            if index == len(self.data):
                formatted_data.append(value_sum / self.range_calculator.days_between_interval())

        return formatted_data

    def sum(self) -> list:
        interval_end = self.range_calculator.next_range_start_date()

        formatted_data = []
        value_sum = 0

        for (index, data_point) in enumerate(self.data, start=1):
            if data_point.added_date >= interval_end:
                # Returns the average
                formatted_data.append(value_sum)

                self.range_calculator.increase_range()
                interval_end = self.range_calculator.next_range_start_date()

                value_sum = 0

            # Update this if we need to pull other values from the field (JSON values)
            value_sum += data_point.get_value()

            # Add the last set of statistics
            if index == len(self.data):
                formatted_data.append(value_sum)

        return formatted_data
