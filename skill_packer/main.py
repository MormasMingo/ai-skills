#!/usr/bin/env python3
import os
import sys
from pathlib import Path
from colorama import init, Fore, Style

init(autoreset=True)

from .scanner import SkillScanner
from .packer import SkillPacker
from .ui import InteractiveUI
from .types import SkillInfo


class SkillPackerCLI:
    def __init__(self):
        self.scanner = SkillScanner()
        self.packer = SkillPacker()
        self.ui = InteractiveUI()
        self.output_dir = Path.cwd() / 'dist-skills'
        self._ensure_output_dir()

    def _ensure_output_dir(self):
        self.output_dir.mkdir(parents=True, exist_ok=True)

    def run(self):
        try:
            print(Fore.CYAN + Style.BRIGHT + '\n Skill Packer - Skill 打包工具\n')

            skills = self.scanner.scan()

            if not skills:
                self.ui.show_message('未找到任何 skill 目录', 'error')
                return

            self.ui.show_message(f'发现 {len(skills)} 个 skill', 'info')
            self._select_and_process(skills)
        except Exception as e:
            self.ui.show_message(f'错误: {str(e)}', 'error')

    def _select_and_process(self, skills: list[SkillInfo]):
        def get_label(skill: SkillInfo) -> str:
            return skill.name

        def get_description(skill: SkillInfo) -> str:
            return skill.description or ''

        selected_skill = self.ui.show_list(
            skills,
            '请选择要处理的 Skill',
            get_label=get_label,
            get_description=get_description
        )

        if not selected_skill:
            print(Fore.BLACK + Style.BRIGHT + '\n已退出')
            return

        action = self.ui.show_menu(
            ['打包为 ZIP', '导出为 MD', '返回列表', '退出'],
            f'操作: {selected_skill.name}'
        )

        if not action:
            self._select_and_process(skills)
            return

        if action == '打包为 ZIP':
            self._pack_as_zip(selected_skill)
        elif action == '导出为 MD':
            self._pack_as_md(selected_skill)
        elif action == '返回列表':
            self._select_and_process(skills)
            return
        elif action == '退出':
            print(Fore.BLACK + Style.BRIGHT + '\n已退出')
            return

        continue_action = self.ui.show_menu(
            ['继续处理其他 Skill', '退出'],
            '操作完成'
        )

        if continue_action == '继续处理其他 Skill':
            self._select_and_process(skills)

    def _pack_as_zip(self, skill: SkillInfo):
        try:
            self.ui.show_message(f'正在打包 {skill.name}...', 'info')
            output_path = self.packer.pack(skill, str(self.output_dir))
            self.ui.show_message(f'✓ 已打包: {output_path}', 'success')
        except Exception as e:
            self.ui.show_message(f'打包失败: {str(e)}', 'error')

    def _pack_as_md(self, skill: SkillInfo):
        try:
            self.ui.show_message(f'正在导出 {skill.name}...', 'info')
            output_path = self.packer.pack_to_md(skill, str(self.output_dir))
            self.ui.show_message(f'✓ 已导出: {output_path}', 'success')
        except Exception as e:
            self.ui.show_message(f'导出失败: {str(e)}', 'error')


def main():
    cli = SkillPackerCLI()
    cli.run()


if __name__ == '__main__':
    main()
