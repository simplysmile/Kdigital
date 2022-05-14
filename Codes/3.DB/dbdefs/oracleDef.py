import cx_Oracle
import jaydebeapi

class Oracles():
    lib_dir = "/Users/jihyeon/instantclient_19_8/"
    wallet_location = "/Users/jihyeon/instantclient_19_8/network/admin/Wallet_Guro.zip"

    cx_Oracle.init_oracle_client(lib_dir)
    username='ADMIN'
    password = 'Clouddata2022!'
    jdbc_driver_loc = "/Library/Java/Extensions/ojdbc8/ojdbc8.jar"

    #  jdbc:oracle:thin:@데이터베이스 이름_medium?TNS_ADMIN=/전자지갑경로/Wallet_데이터베이스 이름/
    jdbc ='jdbc:oracle:thin:@Guro_medium?TNS_ADMIN=//Users/jihyeon/instantclient_19_8/network/admin/Wallet_Guro'

    jdbc_class ="oracle.jdbc.driver.OracleDriver"

    def oraconn():
        conn = jaydebeapi.connect(Oracles.jdbc_class,Oracles.jdbc,[Oracles.username, Oracles.password],Oracles.jdbc_driver_loc)
        # conn.setAutoCommit(False)
        return conn

    def oracs(conn):
        cs = conn.cursor()
        return cs

    def oraclose(cs,conn):
        cs.close()
        conn.commit()
        conn.close()