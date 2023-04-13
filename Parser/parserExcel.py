import pandas as pd


def get_students_df(path) -> pd.DataFrame:
    df = pd.read_excel(
        path,
        engine="openpyxl"
    )
    return df


def get_df_table_html(df) -> str:
    # df = get_students_df(path)
    html = df.to_html(classes="table table-striped-columns")
    return html


if __name__ == '__main__':
    get_df_table_html()
