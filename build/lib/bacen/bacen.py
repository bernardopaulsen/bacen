import pandas as pd

def get(number : int, start : str, end : str) -> pd.DataFrame:
    """
    Gets data from Bacen Time Series Management System API

    :param number: str - Series number on Bacen SGS
    :param start: str - Initial date for the series - DD/MM/YYY
    :param end: str - Final date for the series - DD/MM/YYY
    :returns: pandas.DataFrame
    """
    
    url  = "http://api.bcb.gov.br/dados"
    url += f"/serie/bcdata.sgs.{number}"
    url += "/dados?formato=csv&"
    url += f"&dataInicial={start}&dataFinal={end}"

    df = pd.read_csv(url,
        sep=";",
        index_col=0,
        parse_dates=True,
        decimal=",",
        dayfirst = True)

    return df

if __name__ == "__main__":
    x = get(12,"01/01/2000", "01/01/2000")