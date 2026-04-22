import pandas as pd
import plotly.express as px

FILE_PATH = "../data/transactions.csv"


def generate_graph():
    df = pd.read_csv(FILE_PATH)

    df["type"] = df["type"].astype(str)
    df = df[df["type"] == "1"]

    df["date"] = pd.to_datetime(df["date"], format="%d/%m/%Y")
    trend = df.groupby("date").size().reset_index(name="count")
    trend = trend.sort_values(by="date")

    fig = px.line(trend, x="date", y="count", title="Issued Books Trend")
    fig.show()