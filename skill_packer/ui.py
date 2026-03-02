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

        for index, item in enumerate(items):
            is_selected = index == self.selected_index

            label = get_label(item) if get_label else str(item)
            desc = get_description(item) if get_description else ''

            if is_selected:
                prefix = Back.GREEN + Fore.BLACK + ' > ' + Style.RESET_ALL
                name = Back.GREEN + Fore.BLACK + ' ' + label + ' ' + Style.RESET_ALL
                description = Back.GREEN + Fore.BLACK + ' ' + desc + ' ' + Style.RESET_ALL if desc else ''
            else:
                prefix = '   '
                name = label
                description = Fore.WHITE + desc if desc else ''

            print(f'{prefix}{name}')
            if description:
                print(f'    {description}')

        print(Fore.BLACK + Style.BRIGHT + '\n (↑/↓ 选择, Enter 确认, Esc 退出)')

    def _render_menu(self, options: List[str], title: str):
        os.system('cls' if os.name == 'nt' else 'clear')
        print(Fore.CYAN + Style.BRIGHT + f'\n {title}\n')

        for index, option in enumerate(options):
            is_selected = index == self.selected_index

            if is_selected:
                prefix = Back.GREEN + Fore.BLACK + ' > ' + Style.RESET_ALL
                label = Back.GREEN + Fore.BLACK + ' ' + option + ' ' + Style.RESET_ALL
            else:
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
