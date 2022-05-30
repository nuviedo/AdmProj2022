import PySimpleGUI as sg

L_Login=[[sg.Text("Please log-in.")],
[sg.Text("Username:"),sg.Push(),sg.Input("",k="-L.Username-"),],
[sg.Text("Password:"),sg.Push(),sg.Input("",password_char="*",k="-L.Password-")],
[sg.Button("Submit",k="-L.Submit-")],
]

L_Main=[[
    sg.TabGroup([[
    sg.Tab('Inventory',[[
        sg.Frame("Search",[ #Select med from inputs
            [sg.Text("Name: ",s=10),sg.Input("",k="-1.Name-",s=50,enable_events=True)],
            [sg.Text("Compound: ",s=10),sg.Input("",k="-1.Comp-",s=50,enable_events=True)],
            [sg.Text("ID: ",s=10),sg.Input("",k="-1.ID-",s=50,enable_events=True)],
            [sg.Listbox([],k="-1.Select-",enable_events=True,select_mode=sg.LISTBOX_SELECT_MODE_SINGLE,size=(1,8),expand_x=True,expand_y=True)],
        ],expand_y=True),
        sg.Push(),
        sg.Frame("Results",[ #Visualize med from inputs
            [sg.Text("Compound: ",s=10),sg.Input("",readonly=True,disabled_readonly_background_color="light gray",k="-1.Comp.Out-",s=50)],
            [sg.Text("Name: ",s=10),sg.Input("",readonly=True,disabled_readonly_background_color="light gray",k="-1.Name.Out-",s=50)],
            [sg.Text("Contents: ",s=10),sg.Input("",readonly=True,disabled_readonly_background_color="light gray",k="-1.Cont.Out-",s=50)],
            [sg.Text("Strength: ",s=10),sg.Input("",readonly=True,disabled_readonly_background_color="light gray",k="-1.Conc.Out-",s=50)],
            [sg.Text("Price: ",s=10),sg.Input("",readonly=True,disabled_readonly_background_color="light gray",k="-1.Cost.Out-",s=50)],
            [sg.Text("Available: ",s=10),sg.Input("",readonly=True,disabled_readonly_background_color="light gray",k="-1.Amnt.Out-",s=50)],
            [sg.Text("ID: ",s=10),sg.Input("",readonly=True,disabled_readonly_background_color="light gray",k="-1.ID.Out-",s=50)],
        ],expand_y=True), 
    ]],k="-1.Tab-"),
    sg.Tab('Sales', [[
        sg.Frame("Search",[ #Find purchase from info
            [sg.Frame("About the sale",[
                [sg.Text("Date: ",s=10),sg.Input("",k="-2.Date-",s=50,enable_events=True)],
                [sg.Text("Sale ID: ",s=10),sg.Input("",k="-2.IDS-",s=50,enable_events=True)],
                [sg.Text("Retailer ID: ",s=10),sg.Input("",k="-2.IDV-",s=50,enable_events=True)],
            ])],
            [sg.Frame("About the medicine",[
                [sg.Text("Medicine ID: ",s=10),sg.Input("",k="-2.IDM-",s=50,enable_events=True)],
            ])],
            [sg.Listbox([],k="-2.Select-",size=(1,8),expand_x=True,expand_y=True,enable_events=True)],
        ],expand_y=True),
        sg.Push(),
        sg.Frame("Results",[ #Display individual purchase
            [sg.Text("ID: ",s=10),sg.Input("",readonly=True,disabled_readonly_background_color="light gray",k="-2.IDS.Out-",s=50)],
            [sg.Text("Retailer ID: ",s=10),sg.Input("",readonly=True,disabled_readonly_background_color="light gray",k="-2.IDV.Out-",s=50)],
            [sg.Text("Medicine ID: ",s=10),sg.Input("",readonly=True,disabled_readonly_background_color="light gray",k="-2.IDM.Out-",s=50)],
            [sg.Text("Date: ",s=10),sg.Input("",readonly=True,disabled_readonly_background_color="light gray",k="-2.Date.Out-",s=50)],
            [sg.Text("Name: ",s=10),sg.Input("",readonly=True,disabled_readonly_background_color="light gray",k="-2.Name.Out-",s=50)],
            [sg.Text("Compound: ",s=10),sg.Input("",readonly=True,disabled_readonly_background_color="light gray",k="-2.Comp.Out-",s=50)],
            [sg.Text("Amnt. Sold: ",s=10),sg.Input("",readonly=True,disabled_readonly_background_color="light gray",k="-2.Amnt.Out-",s=50)],
            [sg.Text("Contents: ",s=10),sg.Input("",readonly=True,disabled_readonly_background_color="light gray",k="-2.Cont.Out-",s=50)],
            [sg.Text("Strength: ",s=10),sg.Input("",readonly=True,disabled_readonly_background_color="light gray",k="-2.Conc.Out-",s=50)],
            [sg.Text("Total: ",s=10),sg.Input("",readonly=True,disabled_readonly_background_color="light gray",k="-2.Cost.Out-",s=50)],
        ],expand_y=True)
    ]],k="-2.Tab-"),
    sg.Tab('Terminal', [[
        sg.Frame("Medicine Search",[ #Select med for purchase
            [sg.Text("Retailer ID: ",s=10),sg.Input("",k="-3.IDV-",s=25,readonly=True,disabled_readonly_background_color="light gray")],
            [sg.Text("Medicine ID: ",s=10),sg.Input("",k="-3.IDM-",s=25,enable_events=True)],
            [sg.Text("Name: ",s=10),sg.Input("",k="-3.MedN-",s=25,enable_events=True)],
            [sg.Text("Compound: ",s=10),sg.Input("",k="-3.MedC-",s=25,enable_events=True)],
            [sg.Listbox([],k="-3.Select-",size=(1,8),expand_x=True,expand_y=True,enable_events=True)],
        ],expand_y=True),
        #sg.Push(),
        sg.Frame("Medicine Information",[
            [sg.Text("Medicine ID: ",s=10),sg.Input("",readonly=True,disabled_readonly_background_color="light gray",k="-3.ID.Out-",s=30)],
            [sg.Text("Name: ",s=10),sg.Input("",readonly=True,disabled_readonly_background_color="light gray",k="-3.Name.Out-",s=30)],
            [sg.Text("Compound: ",s=10),sg.Input("",readonly=True,disabled_readonly_background_color="light gray",k="-3.Comp.Out-",s=30)],
            [sg.Text("Contents: ",s=10),sg.Input("",readonly=True,disabled_readonly_background_color="light gray",k="-3.Cont.Out-",s=30)],
            [sg.Text("Strength: ",s=10),sg.Input("",readonly=True,disabled_readonly_background_color="light gray",k="-3.Conc.Out-",s=30)],
            [sg.Text("Price: ",s=10),sg.Input("",readonly=True,disabled_readonly_background_color="light gray",k="-3.Cost.Out-",s=30)],
            [sg.Text("Available: ",s=10),sg.Input("",readonly=True,disabled_readonly_background_color="light gray",k="-3.Amnt.Out-",s=30)],
            [sg.VPush()],
            [sg.Text("Amount to sell:",s=15),sg.Input("",k="-3.Amnt-",s=25)],
            [sg.Button("Remove from checkout",k="-3.Rem-"),sg.Push(),sg.Button("Add to checkout",k="-3.Add-")],
        ],expand_y=True),
        #sg.Push(),
        sg.Frame("Checkout",[
            [sg.Listbox([],k="-3.Checkout-",enable_events=True,size=(35,8),expand_x=True,expand_y=True)],
            [],
            [sg.Input("Total: $0.00",readonly=True,disabled_readonly_background_color="light gray",k="-3.Total.Out-",s=15),sg.Push(),sg.Button("Finalize purchase",k="-3.Purchase-")]
        ],expand_x=True,expand_y=True)
    ]],k="-3.Tab-")
    
    
]], k="-0.Tabs-", expand_x=True,expand_y=True)
]]


DBW=None

#Windows
login_w=sg.Window("Log-in: Pharmacy Terminal",L_Login,finalize=True)
window=None
eventdef={}

def on_close(values):
    return "break"
def strmed(D):
    return f'{D["Name"]} | {D["Strength"]} | {D["Contents"]} | {D["Compound"]}'
def strsale(D):
    med=DBW.table_find_approx("inventory",{"ID":D["MedID"]})[0]
    return f'{D["Date"]} | {D["EmplID"]} | {strmed(med)}'
def search_1(values):
    IDS,NameS,CompS=values["-1.ID-"],values["-1.Name-"],values["-1.Comp-"]
    if(IDS=="" and NameS=="" and CompS==""):
        return
    Dict={}
    if(IDS!=""):
        Dict["ID"]=IDS
    if(NameS!=""):
        Dict["Name"]=NameS
    if(CompS!=""):
        Dict["Compound"]=CompS
    SR=DBW.table_find_approx("inventory",Dict)
    window["-1.Select-"].update(values=[strmed(x) for x in SR])
    window["-1.Select-"].metadata={strmed(x):x for x in SR}
    
def list_1(values):
    if(not window["-1.Select-"].metadata):
        return
    D=window["-1.Select-"].metadata[values["-1.Select-"][0]]
    
    window["-1.ID.Out-"].update(value=D["ID"])
    window["-1.Name.Out-"].update(value=D["Name"])
    window["-1.Comp.Out-"].update(value=D["Compound"])
    window["-1.Cont.Out-"].update(value=D["Contents"])
    window["-1.Conc.Out-"].update(value=D["Strength"])
    window["-1.Cost.Out-"].update(value=f"${D['Price']:.02f}")
    window["-1.Amnt.Out-"].update(value=D["Available"])
    
def search_2(values):
    IDS,IDR,DATE=values["-2.IDS-"],values["-2.IDV-"],values["-2.Date-"]
    IDM=values["-2.IDM-"]
    if((IDS=="" or IDS==None) and (IDR=="" or IDR==None) and (DATE=="" or DATE==None) and (IDM=="" or IDM==None)):
        return
    
    Dict={}
    if(IDS!=""):
        Dict["ID"]=IDS
    if(IDR!=""):
        Dict["EmplID"]=IDR
    if(DATE!=""):
        Dict["Date"]=DATE
    if(IDM!=""):
        Dict["MedID"]=IDM
    if(len(Dict.keys())==0):
        return
    SR=DBW.table_find_approx("sales",Dict)
    window["-2.Select-"].update(values=[strsale(x) for x in SR])
    window["-2.Select-"].metadata={strsale(x):x for x in SR}
    
def list_2(values):
    if(not window["-2.Select-"].metadata):
        return
    D=window["-2.Select-"].metadata[values["-2.Select-"][0]]
    med=DBW.table_find_approx("inventory",{"ID":D["MedID"]})[0]
    
    window["-2.IDS.Out-"].update(value=D["ID"])
    window["-2.IDV.Out-"].update(value=D["EmplID"])
    window["-2.IDM.Out-"].update(value=D["MedID"])
    window["-2.Date.Out-"].update(value=D["Date"])
    window["-2.Name.Out-"].update(value=med["Name"])
    window["-2.Comp.Out-"].update(value=med["Compound"])
    window["-2.Cont.Out-"].update(value=med["Contents"])
    window["-2.Conc.Out-"].update(value=med["Strength"])
    window["-2.Amnt.Out-"].update(value=D["Amount"])
    window["-2.Cost.Out-"].update(value=D["Cost"])
    
def search_3(values):
    IDS,NameS,CompS=values["-3.IDM-"],values["-3.MedN-"],values["-3.MedC-"]
    if(IDS=="" and NameS=="" and CompS==""):
        return
    Dict={}
    if(IDS!=""):
        Dict["ID"]=IDS
    if(NameS!=""):
        Dict["Name"]=NameS
    if(CompS!=""):
        Dict["Compound"]=CompS
    SR=DBW.table_find_approx("inventory",Dict)
    window["-3.Select-"].update(values=[strmed(x) for x in SR])
    window["-3.Select-"].metadata={strmed(x):x for x in SR}


Checkout=[]
checkidx=-1
def list_3(values):
    global checkidx
    if(not window["-3.Select-"].metadata):
        return
    window["-3.Rem-"].update(visible=False)
    checkidx=-1
    D=window["-3.Select-"].metadata[values["-3.Select-"][0]]
    window["-3.Add-"].update(visible=True)
    
    window["-3.ID.Out-"].update(value=D["ID"])
    window["-3.Name.Out-"].update(value=D["Name"])
    window["-3.Comp.Out-"].update(value=D["Compound"])
    window["-3.Cont.Out-"].update(value=D["Contents"])
    window["-3.Conc.Out-"].update(value=D["Strength"])
    window["-3.Cost.Out-"].update(value=f"${D['Price']:.02f}")
    window["-3.Amnt.Out-"].update(value=D["Available"])
    
def add_3(values):
    if(checkidx!=-1):
        return
    C=values["-3.Amnt-"]
    if(C=="" or C==None):
        return
    is_int=False 
    try:
        int(C)
        is_int=True
    except:
        pass
    if(not is_int):
        return
    D=DBW.table_find_approx("inventory",{"ID":values["-3.ID.Out-"]})
    if(len(D)==0):
        return
    D=D[0]
    Checkout.append([D,f"${D['Price']*int(C):.02f} | "+strmed(D),int(C)])
    window["-3.Add-"].update(visible=False)
    update_checkout_3()

def get_total():
    sumx=0
    for c in Checkout:
        sumx+=c[0]["Price"]*c[2]
    return sumx
def update_checkout_3():
    window["-3.Checkout-"].update([x[1] for x in Checkout])
    total=get_total()
    window["-3.Total.Out-"].update(value=f"Total: ${total:.02f}")
def rem_3(values):
    if(checkidx==-1):
        return
    Checkout.pop(checkidx)
    window["-3.ID.Out-"].update(value="")
    window["-3.Name.Out-"].update(value="")
    window["-3.Comp.Out-"].update(value="")
    window["-3.Cont.Out-"].update(value="")
    window["-3.Conc.Out-"].update(value="")
    window["-3.Cost.Out-"].update(value="")
    window["-3.Amnt.Out-"].update(value="")
    window["-3.Rem-"].update(visible=False)
        
    update_checkout_3()

def list_3_b(values):
    global checkidx
    checkidx=-1
    window["-3.Add-"].update(visible=False)
    for i in range(len(Checkout)):
        if(Checkout[i][1]==values["-3.Checkout-"][0]):
            checkidx=i
            break
    if(checkidx==-1):
        return 
    window["-3.Rem-"].update(visible=True)
    D=Checkout[checkidx][0]
    window["-3.ID.Out-"].update(value=D["ID"])
    window["-3.Name.Out-"].update(value=D["Name"])
    window["-3.Comp.Out-"].update(value=D["Compound"])
    window["-3.Cont.Out-"].update(value=D["Contents"])
    window["-3.Conc.Out-"].update(value=D["Strength"])
    window["-3.Cost.Out-"].update(value=f"${D['Price']:.02f}")
    window["-3.Amnt.Out-"].update(value=D["Available"])

def purchase_3(values):
    global Checkout
    for c in Checkout:
        Med=c[0]
        Amt=c[2]
        D={
        "Date":DBW.timestamp(),
        "MedID":Med["ID"],
        "Amount":Amt,
        "Cost":float(Med["Price"])*Amt,
        "EmplID":User,
        }
        DBW.table_insert("sales",D)
    Checkout=[]
    update_checkout_3()
    window["-3.Add-"].update(visible=False)
    window["-3.Rem-"].update(visible=False)
    
eventdef[sg.WIN_CLOSED]=on_close
eventdef["-1.ID-"]=search_1
eventdef["-1.Name-"]=search_1
eventdef["-1.Comp-"]=search_1
eventdef["-1.Select-"]=list_1

eventdef["-2.IDS-"]=search_2
eventdef["-2.IDV-"]=search_2
eventdef["-2.Date-"]=search_2
eventdef["-2.IDM-"]=search_2
eventdef["-2.Select-"]=list_2

eventdef["-3.IDM-"]=search_3
eventdef["-3.MedN-"]=search_3
eventdef["-3.MedC-"]=search_3

eventdef["-3.Select-"]=list_3
eventdef["-3.Add-"]=add_3
eventdef["-3.Checkout-"]=list_3_b
eventdef["-3.Rem-"]=rem_3

eventdef["-3.Purchase-"]=purchase_3



User=None
def TestLogin(Username,Password):
    global User,DBW
    Token=DBW.salt(Username,Password)
    Res=DBW.table_find_approx("employees",{"Token":Token})
    if(len(Res)==1 and str(Res[0]["ID"])==Username):
        User=Username
    else:
        sg.popup_error("Verifique su usuario y contraseña.",title="Denegado",auto_close=True,auto_close_duration=2,)
        
    
def Login(DB):
    global User,DBW
    DBW=DB
    while(User==None):
        event, values=login_w.read()
        if event==sg.WIN_CLOSED:
            break
        elif event=="-L.Submit-":
            TestLogin(values["-L.Username-"],values["-L.Password-"])
    login_w.close()
    return User!=None

def EventLoop(DB):
    global window,eventdef,DBW
    window=sg.Window("Pharmacy Terminal",L_Main,use_custom_titlebar=False,finalize=True)
    window["-3.Add-"].update(visible=False)
    window["-3.Rem-"].update(visible=False)
    window["-3.IDV-"].update(User)
    DBW=DB
    
    while True:
        event, values = window.read()
        #print(event,values)
        r=None
        if event in eventdef:
            r=eventdef[event](values)
        #else:
            #print("UNDEF. EVENT:",event)
        if(r=="break"):
            break

    window.close()