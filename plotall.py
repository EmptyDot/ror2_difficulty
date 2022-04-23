import matplotlib.pyplot as plt
from run import GenerateRun
from plot import PlotRun




class PlotAllRuns:
    def __init__(self, x_name, y_name, mps_minmax: tuple[int, int],
                 minutes_per_stage=5, player_count=3, difficulty=3, loops=1):
        self.fig, self.axs = plt.subplots(1, 3, figsize=(15, 8))
        self.ax_mps, self.ax_pc, self.ax_diff = self.axs
        self.mps = minutes_per_stage
        self.pc = player_count
        self.diff = difficulty
        self.loops = loops
        self.x_name = x_name
        self.y_name = y_name
        self.mps_min, self.mps_max = mps_minmax
        self.mps_range = range(self.mps_min, self.mps_max + 1)

    def runs(self):
        runs = [GenerateRun(mps, self.pc, self.diff, loops=self.loops) for mps in self.mps_range]
        PlotRun(runs, self.x_name, self.y_name, ax=self.ax_mps).plot()

        runs = [GenerateRun(self.mps, pc, self.diff, loops=self.loops) for pc in range(1, 5)]
        PlotRun(runs, self.x_name, self.y_name, ax=self.ax_pc).plot()

        runs = [GenerateRun(self.mps, self.pc, diff, loops=self.loops) for diff in range(1, 4)]
        PlotRun(runs, self.x_name, self.y_name, ax=self.ax_diff).plot()

    def set_labels(self):
        self.ax_mps.set_title('Minutes per stage (4-8)')
        self.ax_pc.set_title('Player count (1-4)')
        self.ax_diff.set_title('Difficulty (Drizzle-Monsoon)')

    def show(self):
        self.runs()
        self.set_labels()
        plt.show()