import PySimpleGUI as sg


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

window=sg.Window("Pharmacy Terminal",L_Main)

def EventLoop(DB):
    global window,eventdef,DBW
    DBW=DB
    #TODO: Improve event handler, implement interface, 
    while True:
        event, values = window.read()
        if event==sg.WIN_CLOSED:
            break

    window.close()