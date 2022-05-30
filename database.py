import sqlite3 as sq
import time
import datetime
import hashlib


class DBW:
    DB=None
    Cursor=None
    def __init__(self):
        self.DB=sq.connect("Pharma.db")
        self.DB.commit()
        self.Cursor=self.DB.cursor()
    def __del__(self):
        self.DB.commit()
        self.DB.close()
     
    #REQUIRED OP: create required tables
    def CTABLES(self):
    
        __CCOL_INV=["ID INTEGER PRIMARY KEY AUTOINCREMENT","Name VARCHAR(256)","Compound VARCHAR(256)","Contents VARCHAR(256)",
        "Strength VARCHAR(256)","Price REAL","Available INT",]
        INV=", ".join([cdef + " NOT NULL" for cdef in __CCOL_INV],)

        __CCOL_SALE=["ID INTEGER PRIMARY KEY AUTOINCREMENT","Date VARCHAR(32)","MedID INTEGER","Amount INT",
        "Cost REAL","EmplID INTEGER"]
        SALE=", ".join([cdef + " NOT NULL" for cdef in __CCOL_SALE],)
        
        self.Cursor.execute(f"CREATE TABLE IF NOT EXISTS inventory ({INV})")
        self.Cursor.execute(f"CREATE TABLE IF NOT EXISTS sales ({SALE})")
        self.Cursor.execute(f"CREATE TABLE IF NOT EXISTS employees (ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, Token VARCHAR(64) NOT NULL)")
    
    #DEBUG OP: PRUNE ALL DB
    def PRUNE(self):
        self.Cursor.execute("DROP TABLE IF EXISTS inventory")
        self.Cursor.execute("DROP TABLE IF EXISTS sales")
        self.Cursor.execute("DROP TABLE IF EXISTS employees")
    #DEBUG OP: DUMP TO CONSOLE
    def DUMP(self):
        for line in self.DB.iterdump(): 
            print(line)
    
    #REQUIRED OP: ADD PRODUCT
    Headers={
        "inventory":["Name","Compound","Contents","Strength","Price","Available"],
        "sales":["Date","MedID","Amount","Cost","EmplID"],
        "employees":["Token"]
        }
    def table_insert(self,table,data):
        #if(table=="employees"):
        #    self.Cursor.execute(f"INSERT INTO employees DEFAULT VALUES")
        #    return
        TL=[]
        d__k=data.keys()
        Headers=DBW.Headers[table]
        for h in Headers:
            if not h in d__k:
                #print(f"MALFORMED DATA FOR {table} (MISSING {h}):",data)
                return
            TL.append(data[h])
        HCONCAT=", ".join(Headers)
        QUERY=f"INSERT INTO {table} ({HCONCAT}) VALUES ({', '.join(['?']*len(Headers))})"
        #print(QUERY)
        self.Cursor.execute(QUERY,tuple(TL))
    #REQUIRED OP: SEARCH PRODUCT APPROXIMATELY
    def table_find_approx(self, table, data):
        TL=[]
        Headers=DBW.Headers[table]
        for h in ["ID"]+Headers:
            if(h not in data.keys()):
                continue
            d=data[h]
            if(type(d)==int):
                TL.append(f"({h} == {str(d)})")
            elif(type(d)==float):
                TL.append(f"({h} BETWEEN {str(d-.05)} AND {str(d+.05)})")
            else:
                d=str(d)
                d=d.replace("\"","")
                d=d.replace("'","")
                TL.append(f"({h} GLOB '*{d}*')")
        QCONCAT=" AND ".join(TL)
        QUERY=f"SELECT * FROM {table} WHERE {QCONCAT}"
        #print(QUERY)
        L=[]
        try:
            R=self.Cursor.execute(QUERY).fetchall()
            for t in R:
                D={"ID":t[0]}
                for i in range(1,len(t)):
                    D[Headers[i-1]]=t[i]
                L.append(D)
            return L
        except:
            pass
        return L
    def timestamp(self,k=0): #get time in unix seconds
        return str(datetime.datetime.now()-datetime.timedelta(seconds=k))
    def salt(self,Username,Password):
        c=hashlib.sha256(f"{Username}{Password}".encode()).hexdigest()
        return c
    def add_employee(self,Username,Password):
        self.table_insert("employees",{"ID":Username,"Token":self.salt(Username,Password)})