from dataclasses import dataclass, field
from enum import Enum
from typing import Union


class AxisTypeEnum(Enum):
    VALUE = 'value'
    CATEGORY = 'category'
    TIME = 'time'
    LOG = 'log'


@dataclass()
class XAxis:
    show: bool = True
    name: str = ''
    name_rotate: int = 0
    type: Union[str, AxisTypeEnum] = field(default=AxisTypeEnum.CATEGORY)

    def __post_init__(self):
        if isinstance(self.type, str):
            try:
                self.type = AxisTypeEnum(self.type.lower())
            except ValueError:
                raise ValueError(f'Invalid axis type: {self.type}')

    def hide(self):
        self.show = False

    def to_dict(self):
        return ({
            'show': self.show,
            'name': self.name,
            'nameRotate': self.name_rotate,
            'type': self.type.value,
        })


@dataclass()
class YAxis:
    show: bool = True
    name: str = ''
    name_rotate: int = 0
    type: Union[str, AxisTypeEnum] = field(default=AxisTypeEnum.VALUE)
    min: int = 0

    def __post_init__(self):
        if isinstance(self.type, str):
            try:
                self.type = AxisTypeEnum(self.type.lower())
            except ValueError:
                raise ValueError(f'Invalid axis type: {self.type}')

    def hide(self):
        self.show = False

    def to_dict(self):
        return {
            'show': self.show,
            'name': self.name,
            'nameRotate': self.name_rotate,
            'type': self.type.value,
            'min': self.min,
        }
