import pandas as pd
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

def get(number : int, start : str, end : str) -> pd.DataFrame:
    """
    Gets data from Bacen Time Series Management System API

    Parameters
    ----------
    number : integer
        Series number on Bacen SGS

    start : string
        Initial date for the series - DD/MM/YYY

    end : string
        Final date for the series - DD/MM/YYY

    Returns
    -------
    object : pandas.Series
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