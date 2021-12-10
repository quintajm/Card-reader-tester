import sqlite3

def log_data(hoy, name, i):
    con = sqlite3.connect('data/data.db')
    cur = con.cursor()

    try:
        # Create table
        cur.execute('''CREATE TABLE logs (date text, name text, rep integer)''')
    except:
        print("Table existed")
    # The qmark style used with executemany():
    lang_list = [
        (hoy, name, i),
    ]
    cur.executemany("INSERT INTO logs VALUES (?,?,?)", lang_list)

    # Save (commit) the changes
    con.commit()

    # We can also close the connection if we are done with it.
    # Just be sure any changes have been committed or they will be lost.
    con.close()

if __name__ == "__main__":
    log_data()