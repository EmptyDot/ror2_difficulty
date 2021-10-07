import numpy as np
import math
from typing import Literal


class GenerateRun:

    def __init__(self, minutes_per_stage: [int, float], player_count: int, difficuly_value: int, loops: int = 1):
        self.minutes_per_stage = minutes_per_stage
        self.player_count = player_count
        self.difficulty_value = difficuly_value
        self.loops = loops

        self.current_time = 0
        self.stages_completed: int
        self.x_axis, self.y_axis = self.get_axes(axis_name=x_name), self.get_axes(axis_name=y_name)
        self.player_factor = 1 + 0.3 * (self.player_count - 1)
        self.time_factor = 0.0506 * self.difficulty_value * self.player_count ** 0.2

    def run(self, x_name, y_name) -> tuple[list, list]:

        x, y = [], []

        for i in (x_name, y_name):
            if i not in self.get_axes().keys():
                raise KeyError(f"The argument '{i}' is not supported as an axis. "
                               f"Supported axes are: {[i for i in self.get_axes().keys()]}")
        else:

            while self.check_if_run_ongoing():
                """this will update once for every second"""
                x.append(x_axis())
                y.append(y_axis())
                self.current_time += 1
            return x, y

    def get_axes(self, axis_name=None):
        axes = {
            'seconds': self.get_current_time_seconds,
            'minutes': self.get_current_time_minutes,
            'difficulty': self.get_diff_coeff,
            'enemy_level': self.get_enemy_level,
        }
        if axis_name is not None:
            return axes[axis_name]
        else:
            return axes

    def get_current_time_seconds(self):
        return self.current_time

    def get_current_time_minutes(self):
        return self.current_time / 60

    # TODO implement chest costs as axes
    def get_money_cost(self, key: str) -> int:
        costs = {
            'small': 25,
            'large': 50,
            'legendary': 400,
            'equipment': 25,
            'category': 30,
            'adaptive': 50,
        }
        return int(costs[key] * self.get_diff_coeff()**1.25)

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

    # TODO create a separate class for max funcs
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









