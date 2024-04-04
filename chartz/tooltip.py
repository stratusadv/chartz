from dataclasses import dataclass, field
from enum import Enum
from typing import Optional


class ToolTipTriggerEnum(Enum):
    ITEM = 'item'  # used for charts that do not have an axis
    AXIS = 'axis'
    NONE = 'none'


class AxisPointerTypeEnum(Enum):
    LINE = 'line'
    SHADOW = 'shadow'
    CROSS = 'cross'


@dataclass()
class ToolTip:
    show: bool = True
    trigger: str = field(default=ToolTipTriggerEnum.ITEM.value)
    axis_pointer_type: Optional[AxisPointerTypeEnum] = None  # Usually configured in axis who needs them.
    # formatter: str = '{a} <br/>{b} : {c}'
    value_format: Optional[str] = None  # This needs to be a js callback function
    options: dict = field(default_factory=dict)

    def to_dict(self):
        return {
            'show': self.show,
            'trigger': self.trigger,
            'axisPointer': {
                'type': self.axis_pointer_type.value if self.axis_pointer_type else None
            },
            # 'formatter': self.formatter,
            'valueFormat': self.value_format,
            **self.options
        }
