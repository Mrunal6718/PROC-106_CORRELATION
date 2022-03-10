import csv
import plotly.express as px
import numpy as np


def plot_figure(data_path):
    data=open(data_path)
    new_data=csv.DictReader(data)
    fig=px.scatter(new_data,x="Coffee in ml",y="sleep in hours")
    fig.show()

def get_data_source(data_path):
    Coffee=[]
    sleep=[]
    data=open(data_path)
    new_data=csv.DictReader(data)

    for row in new_data:
        Coffee.append(float(row["Coffee in ml"]))
        sleep.append(float(row["sleep in hours"]))

    return {"x":Coffee,"y":sleep}

def find_correlation(data_source):
    correlation=np.corrcoef(data_source["x"],data_source["y"])
    print(correlation[0,1])



def setup():
    data_path="finding-correlation-master\cups of coffee vs hours of sleep.csv"
    plot_figure(data_path)
    data_source=get_data_source(data_path)
    find_correlation(data_source)


setup()