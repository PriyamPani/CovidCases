import pandas as pd 
import plotly_express as pe

db = pd.read_csv("data.csv")
var = pe.scatter(db,x="date",y="cases",color="country")

print("Scatter Graph ready")
var.show()