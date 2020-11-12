import sqlite3


def sqlite3_simple_example_create_db():
    con = sqlite3.connect('base1.db')
    cur = con.cursor()

    cur.execute("CREATE TABLE IF NOT EXISTS core_fes(First text, Lastname text, Gender text)")

    # data = ["Ivan", "Str", "M"]

    # cur.execute('INSERT INTO core_fes VALUES(?, ?, ?)', data)

    big_data = []
    data1 = ["Ivan", "Str", "M"]
    data2 = ["Serhii", "Trg", "M"]
    big_data.append(data1)
    big_data.append(data2)

    for data_unit in big_data:
        cur.execute('INSERT INTO core_fes VALUES(?, ?, ?)', data_unit)

    con.commit()
    cur.close()
    con.close()


sqlite3_simple_example_create_db()
