
from dataclasses import dataclass, asdict
from typing import List
import json

@dataclass
class Content:
    content: str = ""

@dataclass
class Text:
    text: Content

@dataclass
class Paragraph:
    rich_text: List[Text]
    color: str = "default"

@dataclass
class Block:
    object: str
    paragraph: Paragraph = None

@dataclass
class Properties:
    title: List[Text]

@dataclass
class Icon:
    type: str = "emoji"
    emoji: str = ""

@dataclass
class Parent:
    type: str
    page_id: str 


@dataclass
class Data:
    parent: Parent
    properties: Properties
    children: List[Block]

    def to_json(self) -> str:
        return json.dumps(asdict(self), indent=4)
