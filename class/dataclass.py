from dataclasses import dataclass, field, fields
from typing import Optional
from enum import Enum, auto
from datetime import date


class ResourceType(Enum):  # <1>
    BOOK = auto()
    EBOOK = auto()
    VIDEO = auto()


@dataclass
class Resource:
    """Media resource description."""
    identifier: str                                    # <2>
    title: str = '<untitled>'                          # <3>
    creators: list[str] = field(default_factory=list)
    date: Optional[date] = None                        # <4>
    type: ResourceType = ResourceType.BOOK             # <5>
    description: str = ''
    language: str = ''
    subjects: list[str] = field(default_factory=list)

    def __repr__(self):
        cls = self.__class__
        cls_name = cls.__name__
        indent = ' ' * 4
        res = [f'{cls_name}(']
        for f in fields(cls):
            value = getattr(self, f.name)
            res.append(f'{indent}{f.name} = {value!r},')
        res.append(')')
        return '\n'.join(res)



# end::DATACLASS[]


description = 'Improving the design of existing code'
book = Resource('978-0-13-475759-9', 'Refactoring, 2nd Edition', ['Martin Fowler', 'Kent Beck'], 
        date(2018, 11, 19), ResourceType.BOOK, description, 'EN', 
        ['computer programming', 'OOP'])

print(book)