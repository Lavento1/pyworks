# book 테이블 만들기
import sqlite3


def get_conn():
    con = sqlite3.connect('./output/sample.db')
    return con


def create_table():
    conn = get_conn()
    cur = conn.cursor()
    sql = """
        CREATE TABLE book(
            book_no INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            publisher TEXT NOT NULL,
            page INTEGER
        )
    """
    # AUTOINCREMENT - 자동 순번(sqquence)

    cur.execute(sql)
    conn.commit()
    print("book 테이블 생성")
    conn.close()


def insert_book():
    conn = get_conn()
    cur = conn.cursor()
    # sql = "INSERT INTO book(title, publisher, page) VALUES ('웹 표준의 정석', '고경희', 600)"
    sql = "INSERT INTO book(title, publisher, page) VALUES (?, ?, ?)"
    cur.execute(sql, ('점프 투 파이썬', '박응용', 300))
    conn.commit()
    conn.close()


def select_book():
    conn = get_conn()
    cur = conn.cursor()
    sql = 'SELECT * FROM book'
    cur.execute(sql)
    rs = cur.fetchall()
    # print(rs)
    for i in rs:
        print(i)
    conn.close()


def select_one(num):
    conn = get_conn()
    cur = conn.cursor()
    sql = "SELECT * FROM book WHERE book_no = ?"
    cur.execute(sql, (num, ))
    rs = cur.fetchone()
    print(rs)
    conn.close()


def update_book(set_page, num):
    conn = get_conn()
    cur = conn.cursor()
    sql = "UPDATE book SET page = ? WHERE book_no = ?"
    cur.execute(sql, (set_page, num))
    conn.commit()
    conn.close()


def delete_book(num):
    conn = get_conn()
    cur = conn.cursor()
    sql = "DELETE FROM book WHERE book_no = ?"
    cur.execute(sql, (num, ))
    conn.commit()
    conn.close()


if __name__=="__main__":
    # create_table()
    # insert_book()
    # update_book(300, 3)
    # delete_book(1)
    select_book()
    select_one(1)
