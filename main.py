import os
import pandas as pd
from analiza_trendu.analiza_trendu import make_prediction

#Set work dir
dir_work = os.getcwd()

#Get data
data_file = "Data/Lista dronów.xlsx"
data_file_path = os.path.join(dir_work,data_file)
df = pd.read_excel(data_file_path)

#Set dir for plots
dir_plots = "Wykresy"
dir_plots_path = os.path.join(dir_work,dir_plots)

#Place for results
dir_result = "Results"
dir_result = os.path.join(dir_work,dir_result)

#Place for results alizy trendów
analize_trendu_filename = "AnalizaTrendow.txt"
analize_trendu_result = os.path.join(dir_result,analize_trendu_filename)

#Prediction of parameters
prediction_year = 2030

#Set Swet/Sref stosunek powierzchni omywanej Swet do powierzchni odniesienia Sw
Swet_Sref_ratio  =  2.5
Kmax = 17
oswalda = 0.8

make_prediction(df, prediction_year, dir_plots_path, analize_trendu_result)




