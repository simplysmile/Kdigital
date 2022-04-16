import cx_Oracle

cx_Oracle.init_oracle_client(lib_dir=r"/Users/yunjihyeon/Documents/cloud/instantclient_19_8 ") 
# 본인이 Instant Client 넣어놓은 경로를 입력해준다

connection = cx_Oracle.connect(user='admin', password='Clouddata2022!', dsn='guro_high')
# 본인이 접속할 오라클 클라우드 DB 사용자이름, 비밀번호, dsn을 넣어준다.
# 커서 생성
cursor = connection.cursor()

# pytab 테이블 생성
cursor.execute("create table pytab (id number, data varchar2(20))")

# 테이블에 데이터 삽입
rows = [ (1, "First" ),
         (2, "Second" ),
         (3, "Third" ),
         (4, "Fourth" ),
         (5, "Fifth" ),
         (6, "Sixth" ),
         (7, "Seventh" ) ]

cursor.executemany("insert into pytab (id, data) values (:1, :2)", rows)

# 변경사항 commit
connection.commit()

# 커서, connection 종료 
cursor.close()
connection.close()