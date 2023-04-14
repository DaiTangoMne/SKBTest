import pandas as pd


def get_students_df(path: str) -> pd.DataFrame:
    """
    Функция читает excel файл и возвращает таблицу dataframe

    :param path: путь до Sample.xlsx
    :return: dataframe
    """
    df = pd.read_excel(
        path,
        engine="openpyxl"
    )
    return df


def get_df_table_html(df: pd.DataFrame) -> str:
    """
    Функция переводит dataframe в html

    :param df: dataframe
    :return: таблица в виде html
    """
    html = df.to_html(classes="table table-striped-columns")
    return html
