import colorsys
from diff import GenerateRun

class Color:
    def __init__(self, run: GenerateRun):
        self.run = run
        self.color = (float, float, float)
        self.mps, self.pc, self.diff = run.get_arg_info()
        self.hue = 0
        self.sat = 0
        self.val = 0

    def get_hue(self) -> int:
        if self.diff == 1:
            return 110
        elif self.diff == 2:
            return 25
        elif self.diff == 3:
            return 360

    def get_saturation(self) -> [int, float]:
        return 25 * self.pc

    def get_value(self) -> [int, float]:
        val = 100 - 10 * self.mps + 20
        if val <= 0:
            return 0
        else:
            return val

    def set_color(self):

        self.hue = self.get_hue() / 360
        self.sat = self.get_saturation() / 100
        self.val = self.get_value() / 100

    def get_rgb_color(self) -> tuple:
        self.set_color()
        return colorsys.hsv_to_rgb(self.hue, self.sat, self.val)
