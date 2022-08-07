import math
import sqlite3

import pandas as pd


def get_cos_radians(x: float) -> float:
    return math.cos(math.radians(x))

def get_radians(x: float) -> float:
    return math.radians(x)

def get_sin_radians(x: float) -> float:
    return math.sin(math.radians(x))


if __name__ == "__main__":
    df = pd.read_csv("preparation_data/data/collated_hawkercentre_data.csv")
    df = df.drop(columns=["Unnamed: 0"])

    ###
    # Pre-calculate cos and sin radians
    ###
    df["LATITUDE_RADIANS_COS"] = df["LATITUDE"].apply(get_cos_radians)
    df["LONGITUDE_RADIANS"] = df["LONGITUDE"].apply(get_radians)
    df["LATITUDE_RADIANS_SIN"] = df["LATITUDE"].apply(get_sin_radians)

    print("Completed precalculation of columns in pandas df")

    ###
    # Set up database and create table
    ###
    conn = sqlite3.connect('app//core//sqlite//database.db')
    c = conn.cursor()
    table = "hawkercentre"
    try:
        # dump dataframe details into table
        df[["NAME",
            "PHOTOURL",
            "LATITUDE",
            "LONGITUDE",
            "LATITUDE_RADIANS_SIN",
            "LATITUDE_RADIANS_COS",
            "LONGITUDE_RADIANS"]].to_sql(
                table,
                conn,
                if_exists="replace",
                index=False)
        print(f"Completed insertion of rows to {table} table")
    except Exception as e:
        raise e

    conn.close()
