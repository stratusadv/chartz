from dataclasses import dataclass, field
from enum import Enum


class DatasetTypeEnum(Enum):
    ARRAY = 'array'
    OBJECT = 'object'


@dataclass()
class Dataset:
    type: DatasetTypeEnum = field(default=DatasetTypeEnum.ARRAY)
    source: list = field(default_factory=list)

    def add_data(self, dataset: list):
        self.source.append(dataset)

    def add_dimensions(self, labels: list):
        self.source.insert(0, labels)

    def to_dict(self):
        return {
            'type': self.type.value,
            'source': self.source
        }
