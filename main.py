import pandas as pd
import numpy as np

# Loading games.csv into DataFram

try:
    df = pd.read_csv('Data/games.csv')
    print("'Games.csv' Loaded successfully!")
except FileNotFoundError:
    print("'Games.csv' not nound")