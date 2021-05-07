"""
Standard imports for the analysis notebooks.
"""
import json
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
pd.set_option('display.max_rows', 200)
idx = pd.IndexSlice
from adjustText import adjust_text

from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
scaler = StandardScaler()
from scripts.stats.pca import apply_pca
from scripts.stats import significance as sig
import numpy as np
from bidi.algorithm import get_display # bi-directional text support for plotting

# custom modules
from .paths import paths
from .export import Exporter
from .plotting import heatmap

# load the data
df = pd.read_csv(paths['dataset'], index_col='node')
df_sg = df.query("(n_times == 1) and (is_advb == False)")
