from dataclasses import dataclass, field
from enum import Enum


class TextAlignEnum(Enum):
    AUTO = 'auto'
    LEFT = 'left'
    RIGHT = 'right'
    CENTER = 'center'


class TextVerticalAlignEnum(Enum):
    TOP = 'top'
    MIDDLE = 'middle'
    BOTTOM = 'bottom'


@dataclass()
class Title:
    name: str = ''
    subtitle: str = ''
    show: bool = True
    text_align: TextAlignEnum = field(default=TextAlignEnum.AUTO)
    text_vertical_align: TextVerticalAlignEnum = field(default=TextVerticalAlignEnum.TOP)
    padding: int = 5
    item_gap: int = 10  # Padding between title and subtitle
    options: dict = field(default_factory=dict)

    def to_dict(self):
        return {
            'show': self.show,
            'text': self.name,
            'subtext': self.subtitle,
            'left': self.text_align.value,
            'top': self.text_vertical_align.value,
            'padding': self.padding,
            'itemGap': self.item_gap,
            **self.options
        }
