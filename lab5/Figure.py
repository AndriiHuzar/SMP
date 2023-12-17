

class Figure:
    length_x = 0
    length_y = 0

    _result = ''
    _color_1 = '\033[44m'
    _color_2 = '\033[42m'
    _color_3 = '\033[43m'

    _default_color = '\033[00m'
    _shadow_color = '\033[47m'
    _symbol_color = '\033[36m'

    _space = 0
    _zoom = 1

    size_x = None
    size_y = None
    size_z = None

    _COLORS = {
        'RED': '\033[31m',
        'GREEN': '\033[32m',
        'YELLOW': '\033[33m',
        'BLUE': '\033[34m',
        'MAGENTA': '\033[35m',
        'CYAN': '\033[36m',
        'WHITE': '\033[37m',
    }

    _SYMBOLS = {
        'corner': '+',
        'horizontal': '—',
        'vertical': '|',
        'inclined': '/',
        'space': ' ',
        'nothing': '',
    }

    def __init__(self, **kwargs):
        if 'size_y' in kwargs:
            self.size_y = kwargs['size_y']
        if 'size_x' in kwargs:
            self.size_x = kwargs['size_x']
        if 'size_z' in kwargs:
            self.size_z = kwargs['size_z']
        if self.size_x:
            if not self.size_y or not self.size_z:
                self.size_y = self.size_z = self.size_x
            self.set_length_x()
            self.set_length_y()
        else:
            self.size_y = self.size_z = self.size_x = 0

    def set_length_x(self):
        self.length_x = self.length_x

    def set_length_y(self):
        self.length_y = self.length_y

    def set_zoom(self):
        self.size_x *= self._zoom
        self.size_y *= self._zoom
        self.size_z *= self._zoom

    @staticmethod
    def color_line(self, color, line):
        return color + line + self._default_color

    @staticmethod
    def build_2d_shadow(self, count, symbol, size):
        lines = []
        for index in range(count):
            line = self.build_symbol(self._SYMBOLS.get('space'), self._space, self._default_color)
            line += self.color_line(self, self._default_color, symbol * (size - index))
            lines += [line]
        return lines

    def build_symbol(self, symbol, count, color):
        line = ''
        for i in range(count):
            line += self.color_line(self, color, symbol)
        return line

    def build(self):
        self._result = self._result

    def create(self):
        self.set_zoom()
        self.build()

    def save(self, filename):
        self.create()
        result = self.remove_color_codes(self._result)
        # print(result)
        with open(filename, 'w') as file:
            file.write(result)

    def remove_color_codes(self, text):
        while '\033[' in text:
            start = text.find('\033[')
            end = text.find('m', start)
            if end != -1:
                text = text[:start] + text[end+1:]
            else:
                break
        return text

    @staticmethod
    def convert(lines):
        result = ''
        for line in lines:
            result += line + '\n'
        return result

    def __str__(self):
        return self._result
