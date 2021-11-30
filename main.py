import pandas as pd


def score(pin: str, pout: str):
    pd.read_excel(pin)
    pd.write_csv(pout)
