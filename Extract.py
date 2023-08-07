import pandas as pd

def extract_rates(url):
    return pd.DataFrame(pd.read_json(url))

def extract_datas(csv):
    return pd.DataFrame(pd.read_csv(csv))



    