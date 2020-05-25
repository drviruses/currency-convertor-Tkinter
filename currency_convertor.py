
from tkinter import ttk, StringVar, messagebox
from ttkthemes import ThemedTk, ThemedStyle
import sqlite3

class currency_converter:
    STYLE = 'arc'
    user_info = None

    def __init__(self):
        # create user table
        conn = sqlite3.connect('user.db')
        query = "CREATE TABLE IF NOT EXISTS user_accounts (uid integer primary key autoincrement, name string, username string, password string, phone string)"
        conn.execute(query)
        conn.commit()

        self.show_login_window()
        #self.show_signup_window()

    def show_login_window(self):
        # init gui
        root = ThemedTk(theme=self.STYLE)
        root.geometry("400x400")
        root.title('Login')
        #root.configure(background='#fefefe')
        root.resizable(0,0)

        # title
        ttk.Label(root, font=('default', 19, 'bold'), text='Currency Converter').grid(row=0, column=0, sticky='w', padx=15)
        ttk.Separator(root, orient='horizontal').grid(row=1, columnspan=2, sticky='ew')

        # sub title
        ttk.Label(root, font=('default', 14, 'bold'), text='Login').grid(row=2, column=0, sticky='w', padx=5, pady=10)

        # defs
        def show_signup():
            root.destroy()
            self.show_signup_window()
        
        def login_db():
            conn = sqlite3.connect('user.db')
            try:
                query = f"SELECT * FROM user_accounts WHERE username='{var_user.get()}' AND password='{var_pass.get()}'"
                var_output = conn.execute(query)
                self.user_info=list(var_output)[0]
                messagebox.showinfo('Success!', f'User logged in!')
                root.destroy()
                self.converter()
                
            except:
                messagebox.showerror('Error!', 'Username or password does not match!')

        PADX,PADY=5,5
        # login form
        ttk.Label(root, text='Username:').grid(row=3, column=0, sticky='w', padx=PADX, pady=PADY)
        ttk.Label(root, text='Password:').grid(row=4, column=0, sticky='w', padx=PADX, pady=PADY)

        var_user, var_pass = StringVar(), StringVar()
        ttk.Entry(root, textvariable=var_user, width=25).grid(row=3, column=0, sticky='e', padx=PADX, pady=PADY)
        ttk.Entry(root, textvariable=var_pass, width=25).grid(row=4, column=0, sticky='e', padx=PADX, pady=PADY)

        ttk.Button(root, text='Signup', command=show_signup).grid(row=5, column=0, sticky='w', padx=PADX, pady=PADY)
        ttk.Button(root, text='Login', command=login_db).grid(row=5, column=0, sticky='e', padx=PADX, pady=PADY)
        root.mainloop()

    def show_signup_window(self):
        # init gui
        root = ThemedTk(theme=self.STYLE)
        root.geometry("900x900")
        root.title('Signup')
        #root.configure(background='#fefefe')
        root.resizable(0,0)

        # title
        ttk.Label(root, font=('default', 19, 'bold'), text='Currency Converter').grid(row=0, column=0, sticky='w', padx=15)
        ttk.Separator(root, orient='horizontal').grid(row=1, columnspan=2, sticky='ew')

        # sub title
        ttk.Label(root, font=('default', 14, 'bold'), text='Signup').grid(row=2, column=0, sticky='w', padx=5, pady=10)
        
        # defs
        def show_login():
            root.destroy()
            self.show_login_window()

        def signup_db():
            conn = sqlite3.connect('user.db')
            if not var_pass.get()==var_repass.get():
                messagebox.showwarning('Warning!', 'Passwords do not match.')
                return
            elif not var_phone.get().isdigit():
                messagebox.showwarning('Warning!', 'Enter a valid phone number.')
                return
            try:
                query = f"INSERT INTO user_accounts(name, username, password, phone) VALUES ('{var_name.get()}', '{var_user.get()}', '{var_pass.get()}', '{var_phone.get()}')"
                conn.execute(query)
                conn.commit()
                messagebox.showinfo('Success!', f'User account for {var_name.get()} successfuly created!')
                
            except:
                messagebox.showerror('Error!', 'There was an unexpected error!')

        PADX, PADY = 5, 5
        # signup form
        ttk.Label(root, text='Username:').grid(row=3, column=0, sticky='w', padx=PADX, pady=PADY)
        ttk.Label(root, text='Password:').grid(row=4, column=0, sticky='w', padx=PADX, pady=PADY)
        ttk.Label(root, text='Re-Password:').grid(row=5, column=0, sticky='w', padx=PADX, pady=PADY)
        ttk.Label(root, text='Name:').grid(row=6, column=0, sticky='w', padx=PADX, pady=PADY)
        ttk.Label(root, text='Phone No:').grid(row=7, column=0, sticky='w', padx=PADX, pady=PADY)

        var_user, var_pass, var_repass, var_name, var_phone = StringVar(), StringVar(), StringVar(), StringVar(), StringVar()
        ttk.Entry(root, textvariable=var_user, width=25).grid(row=3, column=0, sticky='e', padx=PADX, pady=PADY)
        ttk.Entry(root, textvariable=var_pass, width=25).grid(row=4, column=0, sticky='e', padx=PADX, pady=PADY)
        ttk.Entry(root, textvariable=var_repass, width=25).grid(row=5, column=0, sticky='e', padx=PADX, pady=PADY)
        ttk.Entry(root, textvariable=var_name, width=25).grid(row=6, column=0, sticky='e', padx=PADX, pady=PADY)
        ttk.Entry(root, textvariable=var_phone, width=25).grid(row=7, column=0, sticky='e', padx=PADX, pady=PADY)

        ttk.Button(root, text='Signup', command=signup_db).grid(row=8, column=0, sticky='e', padx=PADX, pady=PADY)
        ttk.Button(root, text='Login', command=show_login).grid(row=8, column=0, sticky='w', padx=PADX, pady=PADY)

        root.mainloop()

    def converter(self):
        import tkinter
        from tkinter import StringVar, DoubleVar, ttk, messagebox
        import time
        import datetime

        window=tkinter.Tk()
        window.title("Currency converter")
        window.geometry('')
        window.configure(background='black')

        LeftMainFrame = tkinter.Frame(window, width=600, height=400, bd=8, relief='raise')
        LeftMainFrame.pack(side = "left")
        RightMainFrame =tkinter.Frame(window, width=200, height=400, bd=8, relief="raise")
        RightMainFrame.pack(side = "right")

        precur= StringVar()
        postcur= StringVar()
        convert = DoubleVar()
        currency = DoubleVar()

        EnterCurrency = tkinter.Entry(LeftMainFrame, font=('consolas',20,'bold'), textvariable=convert, bd=2, width=28, justify= 'center')
        EnterCurrency.grid(row=0,column=1)

        box1=ttk.Combobox(LeftMainFrame,textvariable=precur, state='readonly', font=('consolas',20,'bold'),width=20)
        box1['values'] = ('','U.S. Dollar(USD)','Indian Rupee(INR)','European Euro(EUR)','Japanese Yen(JPY)','British Pound(GBP)','Swiss Franc(CHF)','Canadian Dollar(CAD)')
        box1.current(0)
        box1.grid(row=0, column=2)

        box2=ttk.Combobox(LeftMainFrame,textvariable=postcur, state='readonly', font=('consolas',20,'bold'),width=20)
        box2['values'] = ('','U.S. Dollar(USD)','Indian Rupee(INR)','European Euro(EUR)','Japanese Yen(JPY)','British Pound(GBP)','Swiss Franc(CHF)','Canadian Dollar(CAD)')
        box2.current(0)
        box2.grid(row=4, column=2)

        ExitCurrency = tkinter.Label(LeftMainFrame, font=('consolas',20,'bold'), textvariable=currency, bd=2, width=25, bg='white', pady='2', padx='2', relief='sunken', justify= 'center')
        ExitCurrency.grid(row=4,column=1)

        def Convert():
            li=['U.S. Dollar(USD)','Indian Rupee(INR)','European Euro(EUR)','Japanese Yen(JPY)','British Pound(GBP)','Swiss Franc(CHF)','Canadian Dollar(CAD)']
            rate=[1.00,0.014,1.11,0.0092,1.29,1.01,0.76]
            if(precur.get()!=postcur.get()):
                st=(li.index(precur.get()))
                med=convert.get() * rate[st]
                if postcur.get()=="U.S. Dollar(USD)":
                    convert1 = float(med * 1.00)
                    convert2 = "$ ", str('%.2f'%(convert1))
                    currency.set(convert2)
                if postcur.get()=="Indian Rupee(INR)":
                    convert1 = float(med * 70.91)
                    convert2 = "₹ ", str('%.2f'%(convert1))
                    currency.set(convert2)    
                if postcur.get()=="European Euro(EUR)":
                    convert1 = float(med * 0.90)
                    convert2 = "€ ", str('%.2f'%(convert1))
                    currency.set(convert2)
                if postcur.get()=="Japanese Yen(JPY)":
                    convert1 = float(med * 108.61)
                    convert2 = "¥ ", str('%.2f'%(convert1))
                    currency.set(convert2)
                if postcur.get()=="British Pound(GBP)":
                    convert1 = float(med * 0.78)
                    convert2 = "£ ", str('%.2f'%(convert1))
                    currency.set(convert2)
                if postcur.get()=="Swiss Franc(CHF)":
                    convert1 = float(med * 0.99)
                    convert2 = "fr. ", str('%.2f'%(convert1))
                    currency.set(convert2)   
                if postcur.get()=="Canadian Dollar(CAD)":
                    convert1 = float(med * 1.31)
                    convert2 = "C$ ", str('%.2f'%(convert1))
                    currency.set(convert2)     
            else:
                currency.set(convert.get())

        def Exit():
            Exit=messagebox.askyesno("Exit System","Do you wish to quit?")
            if Exit>0:
                print("Thank you for using our system")
                window.destroy()
                return
        def Reset():
            precur.set("Pre Currency")
            postcur.set("Post Currency")
            convert.set("0.0")
            currency.set("0.0")        

        butConvert= tkinter.Button(RightMainFrame, text='Convert', padx='2', pady='2', bd=2, fg='black',
                            font=('consolas',20,'bold'), width=12, height=1, command=Convert).grid(row=1,column=0)
        butReset= tkinter.Button(RightMainFrame, text='Reset', padx='2', pady='2', bd=2, fg='black',
                            font=('consolas',20,'bold'), width=12, height=1, command=Reset).grid(row=2,column=0)
        butExit= tkinter.Button(RightMainFrame, text='Exit', padx='2', pady='2', bd=2, fg='black',
                            font=('consolas',20,'bold'), width=12, height=1, command=Exit).grid(row=3,column=0) 





        window.mainloop()
        
#everything starts here        
currency_converter()
