import pandas as pd
import plotly.express as px

FILE_PATH = "../data/transactions.csv"


def generate_graph():
    df = pd.read_csv(FILE_PATH, header=None,
                     names=["date", "book", "student", "type"])

    df = df[df["type"] == 1]
    trend = df.groupby("date").size().reset_index(name="count")

    fig = px.line(trend, x="date", y="count", title="Issued Books Trend")
    fig.show()