import tkinter as tk
import tkinter.ttk as ttk
import pandas as pd

import tkintermapview

df = pd.read_csv("kendi-kendine/kolon/veri.csv",sep=",")
df["saat"]=pd.to_datetime(df["saat"])
df = df.sort_values(by='saat',ascending=False)
df_cihaz=df.iloc[:, 0]
df_new=df_cihaz.drop_duplicates()
cihazList=df_new.to_list()
cihazList.sort()
toplanma=[(39.937047, 32.889476),(39.938728,32.891773),(39.940052,32.889299)]

def cihazsec():
    
    tree.delete(*tree.get_children())

    if str(cihaz.get()) =="":
        for index, row in df.iterrows():
            tree.insert('', 'end', values=tuple(row))
    else :
        try:
            CihazID= int(cihaz.get())
            cihazList.index(CihazID) 
            condition = df['cihaz'] == CihazID
            filtered_df = df[condition]
            # filtered_df.sort_values(by="saat",ascending=False) 
            for index, row in filtered_df.iterrows():
                
                if tuple(row)[-1]==1:
                    tree.insert('', 'end', values=tuple(row), tags=("orange",))
                    tree.tag_configure("orange",background="orange")
                else:
                    tree.insert('', 'end', values=tuple(row))

                
        except :
            error_popup()

def error_popup():
    error = tk.Toplevel(window)
    error.title('HATA!')
    error.geometry('200x200')
    errorlabel = tk.Label(error, text='Cihaz ID si yanlış!')
    errorlabel.pack(pady=10)
   

def treeview_select(event):
    selected_item = tree_cihaz.selection()[0]
    values = tree_cihaz.item(selected_item, "values")
    cihaz.delete(0, tk.END)
    cihaz.insert(0, values[0]) 

def on_treeview_double_clicked(event):
    cihazsec()


window = tk.Tk()
window.title('Bina Gözcüsü')
window.geometry("1000x500")

tabControl = ttk.Notebook(window)

tab1, tab2, tab3, tab4= (ttk.Frame(tabControl) for i in range(4))  
 
tabControl.add(tab1, text ='Kolon sensör')
tabControl.add(tab2, text ='Su Sensör')
tabControl.add(tab3, text ='Gaz kesim Sistemi')
tabControl.add(tab4, text ='En yakın Toplanma yeri')
tabControl.pack(expand = 1, fill ="both")

cihaz=tk.Entry(tab1)
cihaz.pack(anchor=tk.NW)

sec_btn=tk.Button(tab1,text="sec",command=cihazsec)
sec_btn.pack()
window.update()
sec_btn.place(x=cihaz.winfo_x()+cihaz.winfo_width(), y=cihaz.winfo_y())

tree = ttk.Treeview(tab1, columns=list(df.columns.values))
tree['show'] = 'headings'
tree.pack(pady=10, padx=10,fill=tk.BOTH, expand=True, side=tk.RIGHT)

for i in list(df.columns.values):
    tree.heading(i, text=i)

for index, row in df.iterrows():
    # tree.insert('', 'end', values=tuple(row))
    if tuple(row)[-1]==1:
        tree.insert('', 'end', values=tuple(row), tags=("orange",))
        tree.tag_configure("orange",background="orange")
    else:
        tree.insert('', 'end', values=tuple(row))


scrollbar = tk.Scrollbar(tree)
scrollbar.pack(side='right' , fill='y')
tree.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=tree.yview)

tree_cihaz= ttk.Treeview(tab1, columns='cihaz', )
tree_cihaz.heading(0,text="cihaz")
tree_cihaz['show'] = 'headings'
tree_cihaz.pack(pady=10, padx=10,fill=tk.BOTH, expand=True)

for i in cihazList:
    tree_cihaz.insert('', 'end', values=i)

tree_cihaz.bind("<<TreeviewSelect>>", treeview_select)
tree_cihaz.bind("<Double-1>", on_treeview_double_clicked)


# toplanma yeri map ------------------------------------------------------------------------
map_widget = tkintermapview.TkinterMapView(tab4, width=990, height=500, corner_radius=0)
map_widget.pack()
map_widget.set_position(39.938993,32.890957)
marker_1 = map_widget.set_position(toplanma[0][0],toplanma[0][1],marker=True)
marker_2 = map_widget.set_position(toplanma[1][0],toplanma[1][1], marker=True)
marker_3 = map_widget.set_position(toplanma[2][0],toplanma[2][1], marker=True)
marker_1.set_text("Toplanma yeri 1")
marker_2.set_text("Toplanma yeri 2")
marker_3.set_text("Toplanma yeri 3")
# --------------------------------------------------------------------------------------------

window.mainloop()
