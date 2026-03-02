import os
import zipfile
from pathlib import Path
from datetime import datetime
from typing import Optional
from .types import SkillInfo


class SkillPacker:
    def pack(self, skill: SkillInfo, output_dir: str) -> str:
        timestamp = datetime.now().strftime('%Y-%m-%d')
        output_filename = f'{skill.name}-{timestamp}.zip'
        output_path = Path(output_dir) / output_filename

        with zipfile.ZipFile(output_path, 'w', zipfile.ZIP_DEFLATED) as zf:
            skill_path = Path(skill.path)
            for file_path in skill_path.rglob('*'):
                if file_path.is_file():
                    arcname = file_path.relative_to(skill_path)
                    zf.write(file_path, arcname)

        return str(output_path)

    def pack_to_md(self, skill: SkillInfo, output_dir: str) -> str:
        skill_md_path = Path(skill.path) / 'SKILL.md'
        timestamp = datetime.now().strftime('%Y-%m-%d')
        output_filename = f'{skill.name}-{timestamp}.md'
        output_path = Path(output_dir) / output_filename

        if not skill_md_path.exists():
            raise FileNotFoundError(f'SKILL.md not found in {skill.path}')

        content = skill_md_path.read_text(encoding='utf-8')

        examples_dir = Path(skill.path) / 'examples'
        templates_dir = Path(skill.path) / 'templates'

        if examples_dir.exists():
            content += '\n\n---\n\n## 附录：示例文件\n\n'
            for file_path in sorted(examples_dir.iterdir()):
                if file_path.is_file():
                    file_content = file_path.read_text(encoding='utf-8')
                    content += f'### {file_path.name}\n\n```\n{file_content}\n```\n\n'

        if templates_dir.exists():
            content += '\n\n---\n\n## 附录：模板文件\n\n'
            for file_path in sorted(templates_dir.iterdir()):
                if file_path.is_file():
                    file_content = file_path.read_text(encoding='utf-8')
                    content += f'### {file_path.name}\n\n```\n{file_content}\n```\n\n'

        output_path.write_text(content, encoding='utf-8')
        return str(output_path)
