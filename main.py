from run import GenerateRun
from plot import PlotRun
import matplotlib.pyplot as plt
"""
GenerateRun contains all the information
we pass this object around to all other classes
we can choose what to plot on the x and y axes by passing arguments into PlotRun 
ex. PlotRun(myrun, x='time' y='difficulty')
standard values for axes are: x='time', y='difficulty'

Supported axes are: 
    'time', 
    'difficulty', 
    'enemy_level', 
    'price_small_chest', 
    'price_large_chest', 
    'price_legendary_chest', 
    'price_equipment_chest', 
    'price_category_chest', 
    'price_adaptive_chest'
    
    future support includes: 'price_shrine',  'director_currency', 


"""


if __name__ == '__main__':

    """run script"""
    fig, ax = plt.subplots()

    myruns = [GenerateRun(4, 3, 2, loops=1), GenerateRun(6, 2, 1, loops=3), GenerateRun(8, 4, 3, loops=1)]
    myrun = GenerateRun(5, 1, 3, loops=1)
    yourrun = GenerateRun(8, 1, 2)
    PlotRun(myruns, 'minutes', 'price_adaptive_chest', ax=ax).plot()

    plt.show()
