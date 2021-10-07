import colorsys


class Color:
    def __init__(self, mps, pc, diff):
        self.mps = mps
        self.pc = pc
        self.diff = diff

    def get_hue(self) -> float:
        if self.diff == 1:
            return 110 / 360
        elif self.diff == 2:
            return 25 / 360
        elif self.diff == 3:
            return 360 / 360

    def get_saturation(self) -> [int, float]:
        return 25 * self.pc / 100

    def get_value(self) -> [int, float]:
        val = 100 - 10 * self.mps + 20
        if val <= 0:
            return 0
        else:
            return val / 100

    def get_rgb_color(self) -> tuple:
        return colorsys.hsv_to_rgb(self.get_hue(), self.get_saturation(), self.get_value())
