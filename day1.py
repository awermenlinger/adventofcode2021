import pandas as pd
import numpy as np
from numpy.lib.stride_tricks import sliding_window_view

depths = open('files\day1.txt', 'r').read().rstrip().split('\n')
depths = [int(i) for i in depths]
depths = np.array(depths)
depths_1 = np.roll(depths, 1)
depths_1[0] = depths[0]
delta = depths - depths_1
total_positives =len(delta[delta > 0])
print("Total positives, 1 increment: {}".format(total_positives))

depths_window = depths.copy()
depths_window = np.sum(sliding_window_view(depths_window, window_shape = 3), axis = 1)

depths_window_1 = np.roll(depths_window, 1)
depths_window_1[0] = depths_window[0]
delta = depths_window - depths_window_1
total_positives =len(delta[delta > 0])
print("Total positives, 3 increment: {}".format(total_positives))