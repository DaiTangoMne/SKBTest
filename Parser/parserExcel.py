import pandas as pd


def get_students_df() -> pd.DataFrame:
    df = pd.read_excel(
        "../data/Sample.xlsx",
        engine="openpyxl"
    )
    return df


def get_df_table_html() -> str:
    df = get_students_df()
    html = df.to_html(classes="table")
    return html


if __name__ == '__main__':
    get_df_table_html()
