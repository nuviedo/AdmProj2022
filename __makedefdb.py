import database
import numpy as np
import pandas as pd

def make(DBW):
    DBW.PRUNE()

    DBW.CTABLES()

    
    med_DF=pd.read_csv("defmk/medicine.csv")
    med_DF.drop(["brand id","slug","manufacturer","package container"],axis=1,inplace=True)
    med_DF.dropna(inplace=True)
    
    F=med_DF[med_DF["type"]!="herbal"].copy()
    F.drop("type",axis=1,inplace=True)
    
    Count=0
    for med in F.iterrows():
        name,form,comp,dose,sizepck=tuple(med[1].to_list())
        for t in sizepck.split("),("):
            t=t.replace("(","").replace(")","").replace(",","")
            sepl=t.find(":")
            amt=t[:sepl].replace("'s pack","")
            price=t[sepl+4:]
            D={"Name":name,
            "Compound":comp,
            "Contents":f"{amt} x {form}",
            "Strength":f"{dose}",
            "Price":price,
            "Available":np.random.randint(0,200),}
            DBW.table_insert("inventory",D)
            Count+=1
    
    for i in range(1,6):
        DBW.add_employee(i,f"PASSWORD{i}")
    for i in range(500):
        MID=np.random.randint(1,Count-1)
        Med=DBW.table_find_approx("inventory",{"ID":MID})[0]
        Amt=np.random.randint(1,5)
        D={
        "Date":DBW.timestamp(int(np.random.uniform(0,60*60*24*365))),
        "MedID":MID,
        "Amount":Amt,
        "Cost":float(Med["Price"])*Amt,
        "EmplID":np.random.randint(0,4),
        }
        DBW.table_insert("sales",D)
    DBW.DB.commit()
    #DBW.DUMP()