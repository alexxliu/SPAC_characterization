import pickle
import numpy as np
import sys
import time
import matplotlib.pyplot as plt
import spac
from spac.visualization import histogram, cal_bin_num  # Adjust your import path if needed

def load_anndata(file_path):
    """Load AnnData object from a pickle file."""
    with open(file_path, "rb") as f:
        adata = pickle.load(f)
    return adata
#feature

    fig1 = spac.visualization.histogram(adata, feature=input.h1_feat(), layer=input.h1_layer(), log_scale=(input.h1_log_x(), input.h1_log_y()))
    return fig1

print("test")

#boxplot 

#annotations

#featvanno

#annovanno

#spatial 

#umap

#scatterplot