import statistics
import plotly.express as px
import pandas as pd
import math
import random
import plotly.figure_factory as ff

df = pd.read_csv('medium_data.csv')
data = df["reading_time"].toilist()
fig = ff.create_distplot([data],["reading_time"], show_hist= False)
fig.show()

population_mean = statistics.mean(data)
print("Mean = ", population_mean)
population_standareddeviation = statistics.stdev(data)
print("Standard Deiation = ", population_standareddeviation)

dataset = []
for i in range (0,1000):
    random_index = random.randint(0, len(data))
    value = data[random_index]
    dataset.append(value)
mean = statistics.mean(dataset)
standareddeviation = statistics.stdev(dataset)
print("mean of 1000 values ",mean)
print("standard deviation of 1000 values", standareddeviation)

