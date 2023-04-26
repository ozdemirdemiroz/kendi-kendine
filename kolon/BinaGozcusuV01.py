import tkinter as tk
import tkinter.ttk as ttk
import pandas as pd

df = pd.read_csv("kendi-kendine/kolon/veri.csv",sep=",")
df["saat"]=pd.to_datetime(df["saat"])
df = df.sort_values(by='saat',ascending=False)
df_cihaz=df.iloc[:, 0]
df_new=df_cihaz.drop_duplicates()
cihazList=df_new.to_list()
cihazList.sort()

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
                print (type(tuple(row)[-1]))
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

window = tk.Tk()
window.title('Bina Gözcüsü')
window.geometry("1000x500")

cihaz=tk.Entry(window)
cihaz.pack(anchor=tk.NW)

sec_btn=tk.Button(window,text="sec",command=cihazsec)
sec_btn.pack()
window.update()
sec_btn.place(x=cihaz.winfo_x()+cihaz.winfo_width(), y=cihaz.winfo_y())

tree = ttk.Treeview(window, columns=list(df.columns.values))
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

tree_cihaz= ttk.Treeview(window, columns='cihaz', )
tree_cihaz.heading(0,text="cihaz")
tree_cihaz['show'] = 'headings'
tree_cihaz.pack(pady=10, padx=10,fill=tk.BOTH, expand=True)

for i in cihazList:
    tree_cihaz.insert('', 'end', values=i)

tree_cihaz.bind("<<TreeviewSelect>>", treeview_select)

window.mainloop()
