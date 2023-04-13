from flask import Flask, render_template, url_for
import Parser as pXL

app = Flask(__name__)


@app.route("/")
def index():
    df = pXL.parserExcel.get_students_df("data/Sample.xlsx")
    table = pXL.parserExcel.get_df_table_html(df)
    return render_template("index.html", table=table)


if __name__ == '__main__':
    app.run(debug=True)