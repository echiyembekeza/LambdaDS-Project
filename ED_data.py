import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt
import seaborn as sns

file = '/Users/ericchiyembekeza/Desktop/Data/17Q3-pt1.csv'
df = pd.read_csv(file)

import pandas_profiling
ED_profile = df.profile_report(correlations={"cramers": False})
ED_profile.to_file(output_file=Path("./ED_profile.html"))
df.columns
pd.options.display.html.table_schema = True
pd.options.display.max_rows = None
df
