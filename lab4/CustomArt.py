
from Data.lab_3.ArtGenerator import ArtGenerator
from Data.lab_4.fonts import fonts


class CustomArt(ArtGenerator):
    _font = 'standard'
    _user_height = 5
    _user_width = 5
    _direction_message = ''
    _color = '\033[37m'

    _FONTS = {
        '1': 'standard',
        '2': 'banner3',
    }
    _COLORS = {
        'RED': '\033[31m',
        'GREEN': '\033[32m',
        'YELLOW': '\033[33m',
        'BLUE': '\033[34m',
        'MAGENTA': '\033[35m',
        'CYAN': '\033[36m',
        'WHITE': '\033[37m',
    }

    def _custom_justify(self):
        message = self.message
        if self.justify == 'center':
            message = message.rjust(20, ' ')
        elif self.justify == 'right':
            message = message.rjust(40)
        elif self.justify == 'left':
            message = message.ljust(0, ' ')
        return message

    def _create(self, **kwargs):
        if 'font' in kwargs:
            font = kwargs['font']
        else:
            font = self._font

        font = fonts.get(font)
        self._direction_message = self._custom_justify()
        art = []
        max_lines = max(len(font.get(letter, '').split('\n')) for letter in self._direction_message)
        for line_num in range(max_lines):
            line = ""
            for letter in self._direction_message:
                letter_lines = font.get(letter, '').split('\n')
                if line_num < len(letter_lines):
                    if self.justify == 'left':
                        line += letter_lines[line_num].ljust(len(letter_lines[0]) + 1)
                    elif self.justify == 'center':
                        line += letter_lines[line_num].center(len(letter_lines[0]) + 1)
                    elif self.justify == 'right':
                        line += letter_lines[line_num].rjust(len(letter_lines[0]) + 1)
                    else:
                        line += letter_lines[line_num].rjust(len(letter_lines[0]) + 1)
                else:
                    line += ' ' * (len(letter_lines[0]) + 1)
            art.append(line)
        output = '\n'.join(art)
        return output
