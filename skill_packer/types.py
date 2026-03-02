from dataclasses import dataclass
from typing import Optional


@dataclass
class SkillInfo:
    name: str
    path: str
    description: Optional[str] = None
