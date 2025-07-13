import pandas as pd
import numpy as np
import seaborn as sns
from scipy import stats
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.figure_factory as ff


titanic_df = pd.read_csv('Titanic_Project/titanic.csv')
print(titanic_df.head(12))
