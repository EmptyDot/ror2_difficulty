import matplotlib.pyplot as plt
from diff import GenerateRun





class PlotAllRuns:
    def __init__(self, minutes_per_stage=5, player_count=3, difficulty=3, loops=1):
        self.fig, self.axs = plt.subplots(1, 3, figsize=(15, 8))
        self.mps = minutes_per_stage
        self.pc = player_count
        self.diff = difficulty
        self.loops = loops
        self.ax_mps, self.ax_pc, self.ax_diff = self.axs

    def runs(self):
        runs = [GenerateRun(mps, self.pc, self.diff, loops=self.loops) for mps in range(4, 9)]
        PlotRun(runs, self.ax_mps).plot()

        runs = [GenerateRun(self.mps, pc, self.diff, loops=self.loops) for pc in range(1, 5)]
        PlotRun(runs, self.ax_pc).plot()

        runs = [GenerateRun(self.mps, self.pc, diff, loops=self.loops) for diff in range(1, 4)]
        PlotRun(runs, self.ax_diff).plot()

    def set_labels(self):
        for ax in self.axs:
            ax.set_xlabel('Time (minutes)')
            ax.set_ylabel('Difficulty coefficient')
        self.ax_mps.set_title('Minutes per stage (4-8)')
        self.ax_pc.set_title('Player count (1-4)')
        self.ax_diff.set_title('Difficulty (Drizzle-Monsoon)')

    def show(self):
        self.runs()
        self.set_labels()
        plt.show()