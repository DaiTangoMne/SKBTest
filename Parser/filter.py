import Parser as pXL
import pandas as pd


def filter_table(col: str, keyword: str, df: pd.DataFrame) -> str:
    """
    Функция фильтрует dataframe по ключевому слову и возвращает
    результирующую таблицу в html.

    :param col: заголовок колонки
    :param keyword: ключевое слово
    :param df: таблица dataframe
    :return: отфильтрованная таблица dataframe
    """
    df_filter = df[df[col].astype(str).str.contains(keyword) == True]
    table = pXL.parserExcel.get_df_table_html(df_filter)
    return table
