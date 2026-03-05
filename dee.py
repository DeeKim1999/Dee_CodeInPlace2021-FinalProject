# importing all the packages I'll need -- dee
import os
import pandas as pd
import geopandas as gpd
import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import plotly.express as px
import seaborn as sns

plasticwastepercapita_dataset = pd.read_csv("/home/plastic-waste-generation-total.csv")
plasticwastepercountry_dataset = pd.read_csv("/home/plastic-waste-per-capita.csv")
