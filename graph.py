import pandas as pd
import os
import plotly.express as px

FILE_PATH = "../data/transactions.csv"


def generate_graph():
    if not os.path.exists(FILE_PATH):
        print("No transaction file found")
        return

    # Load CSV
    df = pd.read_csv(FILE_PATH, header=None, names=["date", "book_id", "student_id", "type"])

    if df.empty:
        print("No data available")
        return

    # Filter only issued books (type = 1)
    df_issued = df[df["type"] == 1]

    if df_issued.empty:
        print("No issued book data")
        return

    # Count issues by date
    trend = df_issued.groupby("date").size().reset_index(name="count")

    # Create graph
    fig = px.line(trend, x="date", y="count", title="Books Issued Trend by Date", markers=True)

    fig.show()