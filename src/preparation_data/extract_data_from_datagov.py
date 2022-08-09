import shutil
import urllib.request
from typing import Dict
from typing import List

import geopandas as gpd
import pandas as pd
from bs4 import BeautifulSoup

def download_zip(url: str, save_dir: str) -> None:
    # init opener and add headers
    opener = urllib.request.build_opener()
    opener.addheaders = [('User-agent', 'Mozilla/5.0')]
    urllib.request.install_opener(opener)

    # retrieve and download file to repository
    try:
        urllib.request.urlretrieve(url, save_dir)
        print(f"Downloaded temp.zip from {url}")
    except Exception as e:
        raise (e)

    return

def unzip_file(zipfile_dir: str, target_dir: str = "preparation_data/data/") -> None:
    shutil.unpack_archive(zipfile_dir, target_dir, "zip")
    print(f"Unpacked files into {target_dir}")
    return

def parse_description(description_list: List[List[str]]) -> List[Dict[str, str]]:
    result = []
    for des in description_list:
        soup = BeautifulSoup(des)
        table = soup.find('table')
        header, values = table.find_all('th')[1:], table.find_all('td')
        dict_values = {header[i].text: values[i].text for i in range(
            len(header)) if values[i].text != ""}
        result.append(dict_values)
    return result


if __name__ == "__main__":

    ###
    # Download and extract files from data gov
    ###
    url = "https://data.gov.sg/dataset/aeaf4704-5be1-4b33-993d-c70d8dcc943e/download"
    save_dir = "preparation_data/data/raw.zip"
    download_zip(url=url, save_dir=save_dir)
    unzip_file(zipfile_dir=save_dir)
    print("[COMPLETED] Downloaded and unziped file")

    ###
    # Extract fields from geojson into flat csv file
    ###
    raw_df = gpd.read_file("preparation_data/data/hawker-centres-geojson.geojson")

    # parsing lat lon
    lat_lon_df = pd.DataFrame()
    lat_lon_df["LONGITUDE"] = raw_df["geometry"].x
    lat_lon_df["LATITUDE"] = raw_df["geometry"].y
    print("[COMPLETED] Parsed lat lon")

    # parsing description
    description_dict = parse_description(raw_df["Description"].values.tolist())
    description_df = pd.DataFrame.from_dict(description_dict)
    print("[COMPLETED] Parsed description")

    # overall df
    df = pd.concat([lat_lon_df, description_df], axis=1)
    filename = "preparation_data/data/collated_hawkercentre_data.csv"
    df.to_csv(filename)
    print(f"[COMPLETED] Extracting into csv to {filename}")
    print(df.head())
