import pandas as pd
from pandas import Series, DataFrame
import os

file = open('crime.txt', 'r')
content = file.read()
myData = DataFrame(list(content))
myData
