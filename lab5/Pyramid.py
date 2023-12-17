from Data.lab_5.Figure import Figure


class Pyramid(Figure):

    def set_length_x(self):
        self.length_x = self.size_x + self.size_y

    def set_length_y(self):
        self.length_y = self.size_z

    @staticmethod
    def build_up_2d_line(self, color_1, color_2, symbol_1, symbol_2, count):
        line = ''
        for size_x in range(count):
            if size_x == 0:
                line += self.color_line(self, color_1, symbol_1)
            else:
                line += self.color_line(self, color_2, symbol_2)
        return line

    @staticmethod
    def build_up_2d(self, lines, symbol, space_color):
        mx = len(lines[0])
        for index in range(len(lines)):
            if index == 0:
                color_1 = self._symbol_color
                color_2 = ''
                symbol_1 = self._SYMBOLS.get('corner')
                symbol_2 = ''
                count = 1
            else:
                color_1 = self._symbol_color
                color_2 = space_color
                symbol_1 = symbol
                symbol_2 = self._SYMBOLS.get('space')
                count = mx - len(lines[index])

            line = self.build_up_2d_line(self, color_1, color_2, symbol_1, symbol_2, count)

            lines[index] = lines[index] + line
        return lines

    @staticmethod
    def build_3d(self, lines):
        inclined_count = 0
        mx = 0
        count = 0
        for index in range(len(lines)):
            line = ''
            shadow_mx = mx + self.size_x
            shadow = ''
            if index != 0 and index != len(lines) - 1:
                if index < self.size_y:
                    count = index - 1
                    symbol = '\\'
                elif index == self.size_y:
                    mx = count
                    count = 0
                    symbol = self._SYMBOLS.get('nothing')
                else:
                    count = mx - inclined_count
                    shadow_count = shadow_mx - len(lines[index]) - 1
                    shadow = self.build_symbol(self._SYMBOLS.get('space'), shadow_count, self._shadow_color)
                    symbol = self._SYMBOLS.get('inclined')
                    inclined_count += 1
                line = self.build_symbol(self._SYMBOLS.get('space'), count, self._color_2)
                line += self.color_line(self, self._symbol_color, symbol)
                line += self.color_line(self, self._symbol_color, shadow)
            lines[index] += line
        return lines

    def build_footer(self):
        line = ''
        for index in range(self.size_y * 2 + 1):
            if index == 0 or index == (self.size_y * 2):
                symbol = '+'
                color = self._color_1
            elif index == self.size_y:
                symbol = '|'
                color = self._color_1
            else:
                symbol = ' '
                color = self._color_1
            line += self.color_line(self, self._symbol_color, symbol)
        return line

    def build(self):
        self.set_zoom()
        shadow_up_lines = self.build_2d_shadow(self, self.size_y, self._SYMBOLS.get('space'), self.size_y)
        first_list = self.build_up_2d(self, shadow_up_lines, self._SYMBOLS.get('inclined'), self._color_1)
        for index in range(len(first_list)):
            if index != 0:
                line = self.color_line(self, self._default_color, self._SYMBOLS.get('vertical'), )
            else:
                line = ''
            first_list[index] += line

        second_list = [s.replace('/', '\\') for s in first_list]
        second_list += [self.build_footer()]

        second_list = list(reversed(second_list))
        lst = first_list + second_list
        result = self.build_3d(self, lst)
        self._result = self.convert(result)
