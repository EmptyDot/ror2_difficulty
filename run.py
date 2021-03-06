import math
import warnings
from typing import Union, Iterable

class GenerateRun:

    def __init__(self, minutes_per_stage: [int, float], player_count: int, difficuly_value: int, loops: int = 1):
        self.minutes_per_stage = minutes_per_stage
        self.player_count = player_count
        self.difficulty_value = difficuly_value
        self.loops = loops

        self.current_time = 0
        self.stages_completed = self.get_stages_completed()

        self.player_factor = 1 + 0.3 * (self.player_count - 1)
        self.time_factor = 0.0506 * self.difficulty_value * self.player_count ** 0.2

        self.x = []
        self.y = []

    def generate_lists(self, x_name: str, y_name: str) -> tuple[list, list]:
        """
        Create and return the lists corresponding with x_name and y_name
        :param x_name: name of x-axis, used as key in get_axes
        :param y_name: name of y-axis, used as key in get_axes
        :return: tuple[list, list] of values for x and y
        """
        x_axis, y_axis = self.get_axes(axis_name=x_name), self.get_axes(axis_name=y_name)
        while self.check_if_run_ongoing():
            """this will update once for every second"""
            self.x.append(x_axis())
            self.y.append(y_axis())
            self.current_time += 1

        return self.x, self.y

    def get_axes(self, axis_name: str):
        """
        :param axis_name: str
        :return: return the specified func
        """
        axes = {
            'seconds': self.get_current_time_seconds,
            'minutes': self.get_current_time_minutes,
            'difficulty': self.get_diff_coeff,
            'enemy_level': self.get_enemy_level,
            'price_small_chest': self.get_money_cost(25),
            'price_large_chest': self.get_money_cost(50),
            'price_legendary_chest': self.get_money_cost(400),
            'price_equipment_chest': self.get_money_cost(25),
            'price_category_chest': self.get_money_cost(30),
            'price_adaptive_chest': self.get_money_cost(50),
        }
        try:
            axis = axes[axis_name]
        except KeyError(f'the specified axis {axis_name} is not supported:\nsupported axes are {axes.keys()}') as exc:
            raise exc
        return axis

    def get_x(self) -> list:
        """
        :return: list of x values
        """
        return self.x

    def get_y(self) -> list:
        """
        :return: list of y values
        """
        return self.y

    def get_current_time_seconds(self) -> int:
        """
        :return: int
        """
        return self.current_time

    def get_current_time_minutes(self) -> float:
        """
        :return: float
        """
        return self.current_time / 60

    def get_money_cost(self, cost: int):
        self.cost = cost
        return self.money_cost

    def money_cost(self):
        return int(self.cost * self.get_diff_coeff() ** 1.25)

    def get_arg_info(self):
        return self.minutes_per_stage, self.player_count, self.difficulty_value

    def get_stages_completed(self):
        return math.floor(self.current_time/(self.minutes_per_stage * 60))

    def check_if_run_ongoing(self) -> bool:
        return False if self.get_stages_completed() == 6 * self.loops else True

    def get_stage_factor(self):
        return 1.15 ** self.get_stages_completed()

    def get_diff_coeff(self):
        return (self.player_factor + self.get_current_time_minutes() * self.time_factor) * self.get_stage_factor()

    def get_enemy_level(self):
        return math.floor(1 + (self.get_diff_coeff() - self.player_factor) / 0.33)

    # TODO create a separate class for max funcs. Are these even required?
    def get_max_stages(self):
        return 6 * self.loops

    def get_total_time(self):
        return 6 * self.loops * self.minutes_per_stage * 60

    def get_total_time_in_minutes(self):
        return 6 * self.loops * self.minutes_per_stage

    def get_max_stage_factor(self):
        return 1.15 ** (self.get_max_stages())

    def get_max_enemy_level(self):
        return math.floor(1 + (self.get_total_time() / 60 * self.time_factor * self.get_max_stage_factor()) / 0.33)

    def get_max_coeff(self):
        return (self.player_factor + self.get_total_time() / 60 * self.time_factor) * self.get_max_stage_factor()









