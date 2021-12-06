import sqlite3


def get_conn():
    con = sqlite3.connect("c:/pydb/mydb.db")  # db 연결 객체 생성
    return con


def select_emp():
    # conn = sqlite3.connect("c:/pydb/mydb.db")  # db 연결 객체 생성
    conn = get_conn()
    cur = conn.cursor()  # db 작업 객체
    sql = "SELECT * FROM employee ORDER BY emp_id"  # db 검색
    cur.execute(sql)    # 검색 실행
    rs = cur.fetchall()     # 모든 자료 가져오기
    print(rs)

    conn.close()    # db 연결 종료


def insert_emp():
    # conn = sqlite3.connect("c:/pydb/mydb.db")  # db 연결 객체 생성
    conn = get_conn()
    cur = conn.cursor()  # db 작업 객체
    # 방법 1 칼럼값을 직접 입력
    # sql = "INSERT INTO employee VALUES ('e1001', '추신수', 40, 40000)"     # data 추가
    # 방법 2 - ?를 사용하여 동적 입력
    sql = "INSERT INTO employee VALUES (?, ?, ?, ?)"
    cur.execute(sql, ('e1004', '박인비', 33, 30000))
    conn.commit()   # 커밋 실행 - 필수
    conn.close()


def select_one():
    # conn = sqlite3.connect("c:/pydb/mydb.db")
    conn = get_conn()
    cur = conn.cursor()
    # sql = "SELECT emp_id, name FROM employee WHERE salary = 50000"
    sql = "SELECT emp_id, name FROM employee WHERE salary=?"
    cur.execute(sql, (50000, ))     # 튜플 구조는 1개를 명시할 때 콤마를 찍어야 함
    rs = cur.fetchall()
    print(rs)

    conn.close()


def update_one():
    # conn = sqlite3.connect("c:/pydb/mydb.db")
    conn = get_conn()
    cur = conn.cursor()
    sql = "UPDATE employee SET age = 30 WHERE emp_id = ?"
    cur.execute(sql, ('e1004', ))
    conn.commit()

    conn.close()


def delete_emp():
    # conn = sqlite3.connect("c:/pydb/mydb.db")
    conn = get_conn()
    cur = conn.cursor()
    sql = "DELETE FROM employee WHERE name = ?"
    cur.execute(sql, ('안산',))
    conn.commit()

    conn.close()


if __name__=="__main__":
    # insert_emp()
    select_emp()
    # select_one()
    # update_one()
    # delete_emp()
