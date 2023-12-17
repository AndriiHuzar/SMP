from Data.lab_5.Rectangle import Rectangle


class ConsoleRectangle(Rectangle):
    figure = Rectangle

    @classmethod
    def set_parameters(cls, dct, input_message):
        for key, value in dct.items():
            print(f"{key}: {value}")
        value = input(f"Select {input_message}: ")
        current_value = dct.get(value, None)
        if current_value:
            return current_value
        else:
            return None

    def input_function(self, dct, input_message, default):
        check = input(f"do you want to set {input_message}? (1/0): ")
        font = None
        if check == '1':
            font = self.set_parameters(dct, input_message)
        if font:
            return font
        else:
            return default

    def configuration(self):

        self.size_x = int(input("Input size_x: "))
        self.size_y = int(input("Input size_y: "))
        self.size_z = int(input("Input size_z: "))

        self._color_1 = self.input_function(self._COLORS, 'color_1', self._color_1)
        self._color_2 = self.input_function(self._COLORS, 'color_2', self._color_2)
        self._color_3 = self.input_function(self._COLORS, 'color_3', self._color_3)

        change_space = input('do you want to create space? (1/0): ')
        if change_space == '1':
            space = int(input("Input space: "))
            self._space(space)

        change_zoom = input('do you want to create zoom? (1/0): ')
        if change_zoom == '1':
            self._zoom = int(input("Input zoom: "))
            self.set_zoom()

        check = input("do you want to save? (1/0): ")
        if check == '1':
            save = input("Input filename: ")
            self.save(save)

    def run(self):
        stop = ''
        while stop != 'f':
            try:
                self.configuration()
                self.create()
                print(self)
            except Exception as e:
                print(e)
            finally:
                stop = input("Press 'f' if you want to exit: ")
