import os
import re
from pathlib import Path
from typing import List, Optional
from .types import SkillInfo


class SkillScanner:
    def __init__(self):
        self.skill_dirs = [
            '.trae/skills',
            'skills',
            '.skills'
        ]

    def scan(self, base_path: str = None) -> List[SkillInfo]:
        if base_path is None:
            base_path = os.getcwd()

        skills = []
        for skill_dir in self.skill_dirs:
            full_path = Path(base_path) / skill_dir
            if not full_path.exists() or not full_path.is_dir():
                continue

            for entry in full_path.iterdir():
                if entry.is_dir():
                    skill_md_path = entry / 'SKILL.md'
                    if skill_md_path.exists():
                        description = self._extract_description(skill_md_path)
                        skills.append(SkillInfo(
                            name=entry.name,
                            path=str(entry),
                            description=description
                        ))

        return skills

    def _extract_description(self, skill_md_path: Path) -> Optional[str]:
        try:
            content = skill_md_path.read_text(encoding='utf-8')

            desc_match = re.search(r'description:\s*["\'](.+?)["\']', content)
            if desc_match:
                return self._truncate(desc_match.group(1))

            header_match = re.search(r'## 描述\s*\n(.+)', content)
            if header_match:
                return self._truncate(header_match.group(1).strip())

            return None
        except Exception:
            return None

    def _truncate(self, text: str, max_length: int = 40) -> str:
        if len(text) <= max_length:
            return text
        return text[:max_length - 3] + '...'
