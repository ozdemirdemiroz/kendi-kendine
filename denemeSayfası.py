import tkinter as tk

class App(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("Bina Gözcû")
        self.master.geometry("650x600+725+200")
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.choice_var1 = tk.IntVar(value=0)
        self.choice_var2 = tk.IntVar(value=0)
        self.choice_var3 = tk.IntVar(value=0)
        self.choice_var4 = tk.IntVar(value=0)
        self.choice_var5 = tk.IntVar(value=0)

        self.ques1 = tk.StringVar(value=0)
        self.ques2 = tk.StringVar(value=0)

        self.ques1 = tk.Label(self, text="Pencereniz kırıldı mı ?")
        self.ques1.pack()
        self.choice1 = tk.Radiobutton(self, text="Evet", variable=self.choice_var1, value=1)
        self.choice1.pack()
        self.choice2 = tk.Radiobutton(self, text="Hayır", variable=self.choice_var1, value=0)
        self.choice2.pack()

        self.ques2 = tk.Label(self, text="Evinizde moloz ya da beton parca düştü mü?")
        self.ques2.pack()
        self.choice3 = tk.Radiobutton(self, text="Evet", variable=self.choice_var2, value=1)
        self.choice3.pack()
        self.choice4 = tk.Radiobutton(self, text="Hayır", variable=self.choice_var2, value=0)
        self.choice4.pack()
        self.ques2 = tk.Label(self, text="Evinizde moloz ya da beton parca düştü mü?")
        self.ques2.pack()
        self.choice5 = tk.Radiobutton(self, text="Evet", variable=self.choice_var3, value=1)
        self.choice5.pack()
        self.choice6 = tk.Radiobutton(self, text="Hayır", variable=self.choice_var3, value=0)
        self.choice6.pack()

        self.sum_button = tk.Button(self, text="Hesapla", command=self.calculate_sum)
        self.sum_button.pack()
        self.sum_label = tk.Label(self, text="")
        self.sum_label.pack()

    def calculate_sum(self):
        total_sum = self.choice_var1.get() + self.choice_var2.get() + self.choice_var3.get() + self.choice_var4.get() + self.choice_var5.get()
        self.sum_label.configure(text=f"Toplam: {total_sum}")

root = tk.Tk()
app = App(master=root)
app.mainloop()