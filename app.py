from flask import Flask, render_template, url_for, request
import Parser as pXL

app = Flask(__name__)


@app.route("/", methods=["POST", "GET"])
def index():
    df = pXL.parserExcel.get_students_df("data/Sample.xlsx")
    if request.method == "POST":
        col = request.form['col']
        keyword = request.form['keyword']
        table = pXL.filter.filter_table(col, keyword, df)
        return render_template("index.html", table=table, col_vals=df.columns.values.tolist())
    else:
        table = pXL.parserExcel.get_df_table_html(df)
        return render_template("index.html", table=table, col_vals=df.columns.values.tolist())


@app.route("/test1")
def test1():
    df = pXL.parserExcel.get_students_df("data/Sample.xlsx")
    table = pXL.filter.filter_table('KURS', '2', df)
    return render_template("test.html", table=table, col_vals=df.columns.values.tolist(), testname="KURS 2")


@app.route("/test2")
def test2():
    df = pXL.parserExcel.get_students_df("data/Sample.xlsx")
    table = pXL.filter.filter_table('CITIZEN', 'Российская Федерация', df)
    return render_template("test.html", table=table, col_vals=df.columns.values.tolist(), testname="CITIZEN Российская Федерация")


@app.route("/test3")
def test3():
    df = pXL.parserExcel.get_students_df("data/Sample.xlsx")
    table = pXL.filter.filter_table('SEX', 'Женский', df)
    return render_template("test.html", table=table, col_vals=df.columns.values.tolist(), testname="SEX Женский")


if __name__ == '__main__':
    app.run(debug=True)
