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
    ]],k="-1.Tab-"),]])
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