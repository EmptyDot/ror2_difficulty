import numpy as np
import math



class GenerateRun:


    def __init__(self, minutes_per_stage: [int, float], player_count: int, difficuly_value: int, loops: int = 1):
        self.current_time = 0
        self.loops = loops
        self.minutes_per_stage = minutes_per_stage
        self.stages_completed = 0
        self.stage_factor = 0
        self.player_count = player_count
        self.difficulty_value = difficuly_value
        self.player_factor = 1 + 0.3 * (self.player_count - 1)
        self.time_factor = 0.0506 * self.difficulty_value * self.player_count ** 0.2
        self.diff_coeff = 0
        self.enemy_level = 1
        self.yticks = []


    def run(self, x_name, y_name) -> tuple[list, list]:
        x, y = [], []
        while self.check_if_run_ongoing():

            self.set_stage_factor()
            self.set_diff_coeff()
            self.set_enemy_level()

            try:
                x.append(self.get_axis()[x_name])
                y.append(self.get_axis()[y_name])

            except KeyError as ex:
                raise f'Non supported key for x or y axis\n supported keys are: {self.axes.keys()}\n {ex}'

            self.current_time += 1
        print(x, y)
        return x, y

    def get_axis(self) -> dict:
        axes = {
            'seconds': self.current_time,
            'minutes': self.current_time,
            'difficulty': self.diff_coeff,
            'enemy_level': self.enemy_level,
            'price_small_chest': self.get_money_cost('small'),
            'price_large_chest': self.get_money_cost('large'),
            'price_legendary_chest': self.get_money_cost('legendary')
        }
        return axes

    def get_money_cost(self, key: str) -> int:
        costs = {
            'small': 25,
            'large': 50,
            'legendary': 400,
            'equipment': 25,
            'category': 30,
            'adaptive': 50,
        }
        return int(costs[key] * self.diff_coeff**1.25)

    def get_arg_info(self):
        return self.minutes_per_stage, self.player_count, self.difficulty_value


    # TODO someting is broken here
    def get_yticks(self):
        yticks = []
        for i in range(1, self.get_max_enemy_level() + 25):
            yticks.append(0.33 * i + self.player_factor - 1)
        return yticks

    def check_if_run_ongoing(self) -> bool:
        self.set_stages_completed()
        return False if self.stages_completed == 6 * self.loops else True

    def set_stages_completed(self):
        self.stages_completed = math.floor(self.current_time/(self.minutes_per_stage * 60))

    def get_time_in_minutes(self) -> float:
        return self.current_time / 60

    def set_stage_factor(self):
        self.stage_factor = 1.15 ** self.stages_completed

    def set_diff_coeff(self):
        self.diff_coeff = (self.player_factor + self.get_time_in_minutes() * self.time_factor) * self.stage_factor

    def set_enemy_level(self):
        self.enemy_level = math.floor(1 + (self.diff_coeff - self.player_factor) / 0.33)

    def get_max_stages(self):
        return 6 * self.loops


    # TODO create a separate class for max funcs
    def get_total_time(self):
        return 6 * self.loops * self.minutes_per_stage * 60

    def get_total_time_in_minutes(self):
        return 6 * self.loops * self.minutes_per_stage

    def get_max_stage_factor(self):
        return 1.15 ** (self.get_max_stages())

    def get_max_enemy_level(self):
        return math.floor(1 + (self.get_total_time() / 60 * self.time_factor * self.get_max_stage_factor()) / 0.33)

    def get_max_coeff(self):
        return (self.get_player_factor() + self.get_total_time() / 60 * self.get_time_factor()) * self.get_max_stage_factor()

# TODO plotlines does not start at 0, fix: subtract starting value
# TODO Improve the fit of fig, especially in PlotAllRuns







