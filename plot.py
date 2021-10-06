import matplotlib.pyplot as plt
from diff import GenerateRun
from color import Color
import math


class PlotRun:
    def __init__(self, run: [list, GenerateRun], x_name, y_name, ax=None):
        self.ax = plt.subplots()[1] if ax is None else ax
        self.run = run
        self.x_name = x_name
        self.y_name = y_name
        self.biggest_coeff = 0
        self.hardest_run = ''

    def plot(self) -> None:
        """
        checks if self.run is list and passes each element to self.plot_run, also sets x/y-labels

        Returns None
        -------
        """
        if type(self.run) == list:
            for i in self.run:
                self.plot_run(i)
                if i.get_max_coeff() > self.biggest_coeff:
                    self.biggest_coeff = i.get_max_coeff()
                    self.hardest_run = i
            self.set_yticks(self.hardest_run)

        else:
            self.plot_run(self.run)
            self.set_yticks(self.run)

        plt.tight_layout(pad=2)
        self.ax.grid()
        self.ax.set_xlabel('Time (minutes)')
        self.ax.set_ylabel('Difficulty')

    def show(self) -> None:
        """
        create and show the plot

        Returns None
        -------

        """
        self.plot()
        plt.show()

    def plot_run(self, run: GenerateRun) -> None:
        """
        plots the line and the end point and creates the legend

        Parameters
        ----------
        run: GenerateRun
        Returns None
        -------
        """
        x, y = run.run(self.x_name, self.y_name)

        plot_color = Color(run).get_rgb_color()
        self.ax.plot(x, y,
                     color=plot_color,
                     label=f'mps: {run.minutes_per_stage}, pc: {run.player_count}, diff: {run.difficulty_value}')
        self.ax.plot(x[-1], y[-1], 'o',
                     color=plot_color,
                     label=f't: {round(x[-1], 2)}min, dc: {round(y[-1], 3)}')
        self.ax.legend()

    def set_yticks(self, run: GenerateRun) -> None:
        """
        assigns ticks and tick labels to self.ax

        Parameters
        ----------
        run: GenerateRun
        Returns None
        -------

        """
        ticks = run.get_yticks()
        new_ticks = []

        for i in range(len(ticks)):
            if i % (3 * run.loops) == 0:
                if i == 0:
                    new_ticks.append(0)
                else:
                    new_ticks.append(ticks[i])
        labels = self.get_ylabels(run, new_ticks)
        self.ax.set_yticks(new_ticks)
        self.ax.set_yticklabels(labels, rotation=45)

    def get_ylabels(self, run: GenerateRun, ticks: list) -> list:
        """

        Parameters
        ----------
        run: object(GenerateRun)
        ticks: list

        Returns a list of tick labels
        -------

        """

        tick_labels = [
            'Easy', 'Normal', 'Hard', 'Very Hard', 'Insane', 'Impossible', 'I SEE YOU', 'I\'M COMING FOR YOU', 'HAHAHAHA'
        ]

        labels = []

        for idx in range(len(ticks)):
            if idx == 0:
                labels.append(tick_labels[0])
            else:
                try:
                    labels.append(tick_labels[idx * run.loops])
                except IndexError:
                    labels.append(math.floor(1 + (idx - run.player_factor) / 0.33))

        return labels


