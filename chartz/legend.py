from dataclasses import dataclass, field
from enum import Enum


class LegendScrollEnum(Enum):
    SCROLL = 'scroll'
    PLAIN = 'plain'


class LegendOrientEnum(Enum):
    HORIZONTAL = 'horizontal'
    VERTICAL = 'vertical'


class LegendAlignEnum(Enum):
    LEFT = 'left'
    RIGHT = 'right'
    CENTER = 'center'
    AUTO = 'auto'


@dataclass()
class Legend:
    show: bool = True
    type: LegendScrollEnum = field(default=LegendScrollEnum.PLAIN)
    orient: LegendOrientEnum = field(default=LegendOrientEnum.HORIZONTAL)
    left: LegendAlignEnum = field(default=LegendAlignEnum.AUTO)
    right: LegendAlignEnum = field(default=LegendAlignEnum.AUTO)
    top: LegendAlignEnum = field(default=LegendAlignEnum.AUTO)
    bottom: LegendAlignEnum = field(default=LegendAlignEnum.AUTO)

    def horizontal(self):
        self.orient = LegendOrientEnum.HORIZONTAL

    def vertical(self):
        self.orient = LegendOrientEnum.VERTICAL

    def to_dict(self):
        return {
            'show': self.show,
            'type': self.type.value,
            'orient': self.orient.value,
            'left': self.left.value,
            'right': self.right.value,
            'top': self.top.value,
            'bottom': self.bottom.value,
        }
