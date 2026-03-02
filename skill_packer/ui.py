import sys
import os
from typing import List, TypeVar, Optional
from colorama import init, Fore, Back, Style

init(autoreset=True)

T = TypeVar('T')


class InteractiveUI:
    def __init__(self):
        self.selected_index = 0
        self._keyboard_available = False
        self._try_import_keyboard()

    def _try_import_keyboard(self):
        try:
            import keyboard
            self._keyboard_available = True
        except ImportError:
            self._keyboard_available = False

    def show_list(self, items: List[T], title: str, get_label=None, get_description=None) -> Optional[T]:
        if not items:
            print(Fore.YELLOW + '未找到任何项目')
            return None

        self.selected_index = 0

        try:
            while True:
                self._render_list(items, title, get_label, get_description)
                key = self._get_key()

                if key == 'UP':
                    self.selected_index = max(0, self.selected_index - 1)
                elif key == 'DOWN':
                    self.selected_index = min(len(items) - 1, self.selected_index + 1)
                elif key == 'ENTER':
                    return items[self.selected_index]
                elif key == 'ESC' or key == 'q':
                    return None
        except KeyboardInterrupt:
            return None

    def show_menu(self, options: List[str], title: str) -> Optional[str]:
        self.selected_index = 0

        try:
            while True:
                self._render_menu(options, title)
                key = self._get_key()

                if key == 'UP':
                    self.selected_index = max(0, self.selected_index - 1)
                elif key == 'DOWN':
                    self.selected_index = min(len(options) - 1, self.selected_index + 1)
                elif key == 'ENTER':
                    return options[self.selected_index]
                elif key == 'ESC':
                    return None
        except KeyboardInterrupt:
            return None

    def _render_list(self, items: List[T], title: str, get_label, get_description):
        os.system('cls' if os.name == 'nt' else 'clear')
        print(Fore.CYAN + Style.BRIGHT + f'\n {title}\n')

        # 获取终端宽度
        terminal_width = self._get_terminal_width()

        for index, item in enumerate(items):
            is_selected = index == self.selected_index

            label = get_label(item) if get_label else str(item)
            desc = get_description(item) if get_description else ''

            if is_selected:
                # 选中状态：整行绿色背景
                prefix = Back.GREEN + Fore.BLACK + ' > ' + Style.RESET_ALL
                # 名称行：填充到终端宽度
                name_content = f' {label} '
                name_padding = ' ' * max(0, terminal_width - len(name_content) - 3)
                name = Back.GREEN + Fore.BLACK + name_content + name_padding + Style.RESET_ALL
                # 描述行：填充到终端宽度
                if desc:
                    desc_content = f'   {desc} '
                    desc_padding = ' ' * max(0, terminal_width - len(desc_content))
                    description = Back.GREEN + Fore.BLACK + desc_content + desc_padding + Style.RESET_ALL
                else:
                    description = ''
            else:
                # 未选中状态
                prefix = '   '
                name = label
                description = Fore.WHITE + desc if desc else ''

            print(f'{prefix}{name}')
            if description:
                print(description)

        print(Fore.BLACK + Style.BRIGHT + '\n (↑/↓ 选择, Enter 确认, Esc 退出)')

    def _get_terminal_width(self) -> int:
        """获取终端宽度"""
        try:
            import shutil
            return shutil.get_terminal_size().columns
        except:
            return 80  # 默认值

    def _render_menu(self, options: List[str], title: str):
        os.system('cls' if os.name == 'nt' else 'clear')
        print(Fore.CYAN + Style.BRIGHT + f'\n {title}\n')

        # 获取终端宽度
        terminal_width = self._get_terminal_width()

        for index, option in enumerate(options):
            is_selected = index == self.selected_index

            if is_selected:
                # 选中状态：整行绿色背景
                prefix = Back.GREEN + Fore.BLACK + ' > ' + Style.RESET_ALL
                # 填充到终端宽度
                content = f' {option} '
                padding = ' ' * max(0, terminal_width - len(content) - 3)
                label = Back.GREEN + Fore.BLACK + content + padding + Style.RESET_ALL
            else:
                # 未选中状态
                prefix = '   '
                label = option

            print(f'{prefix}{label}')

        print(Fore.BLACK + Style.BRIGHT + '\n (↑/↓ 选择, Enter 确认, Esc 返回)')

    def _get_key(self) -> str:
        if self._keyboard_available:
            return self._get_key_with_keyboard()
        else:
            return self._get_key_fallback()

    def _get_key_with_keyboard(self) -> str:
        import keyboard
        while True:
            event = keyboard.read_event()
            if event.event_type == 'down':
                if event.name == 'up':
                    return 'UP'
                elif event.name == 'down':
                    return 'DOWN'
                elif event.name == 'enter':
                    return 'ENTER'
                elif event.name == 'esc':
                    return 'ESC'
                elif event.name == 'q':
                    return 'q'

    def _get_key_fallback(self) -> str:
        """使用标准输入作为后备方案"""
        if os.name == 'nt':
            return self._get_key_windows()
        else:
            return self._get_key_unix()

    def _get_key_windows(self) -> str:
        import msvcrt
        while True:
            ch = msvcrt.getch()
            # 方向键的第一个字节是 \x00 或 \xe0
            if ch == b'\x00' or ch == b'\xe0':
                ch2 = msvcrt.getch()
                if ch2 == b'H':
                    return 'UP'
                elif ch2 == b'P':
                    return 'DOWN'
            elif ch == b'\r':
                return 'ENTER'
            elif ch == b'\x1b':
                return 'ESC'
            elif ch == b'q' or ch == b'Q':
                return 'q'

    def _get_key_unix(self) -> str:
        import tty
        import termios
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            ch = sys.stdin.read(1)
            if ch == '\x1b':
                ch2 = sys.stdin.read(1)
                if ch2 == '[':
                    ch3 = sys.stdin.read(1)
                    if ch3 == 'A':
                        return 'UP'
                    elif ch3 == 'B':
                        return 'DOWN'
                return 'ESC'
            elif ch == '\r':
                return 'ENTER'
            elif ch in ('q', 'Q'):
                return 'q'
            elif ch == '\x03':  # Ctrl+C
                raise KeyboardInterrupt
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ''

    def show_message(self, message: str, msg_type: str = 'info'):
        colors = {
            'info': Fore.BLUE,
            'success': Fore.GREEN,
            'error': Fore.RED
        }
        print(colors.get(msg_type, Fore.WHITE) + message)
