from tkinter import*
from PIL import ImageTk,Image
from tkinter import messagebox
class Login_System:
    def __init__(self,root):
        self.root=root
        self.root.title("Login System")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="#fafafa")
        
        self.phone_image=ImageTk.PhotoImage(file=r"C:\Users\somin\Downloads\phone.png",)
        self.lbl_phone_image=Label(self.root,image=self.phone_image,bd=0).place(x=200,y=90)
        
        #--------LOGIN_FRAME---------
        
        login_frame=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        login_frame.place(x=650,y=90,width=350,height=460)
        title=Label(login_frame,text="Login System",font=("Elephant",30,"bold"),bg="white").place(x=0,y=5,relwidth=1)
        
        self.username=StringVar()
        self.password=StringVar()
        user_lbl=Label(login_frame,text="Username",font=("Andalus",15,"bold"),bg="white",fg="#767171").place(x=50,y=80)
        user_text=Entry(login_frame,textvariable=self.username,font=("times new roman",15,"bold"),bg="#ECECEC").place(x=50,y=120,width=250)
        
        
        pass_lbl=Label(login_frame,text="Password",font=("Andalus",15,"bold"),bg="white",fg="#767171").place(x=50,y=150)
        pass_text=Entry(login_frame,textvariable=self.password,show="*",font=("times new roman",15,"bold"),bg="#ECECEC").place(x=50,y=190,width=250)
        
        btn_login=Button(login_frame,text="Login",command=self.login,bd=10,fg="white",activebackground="#00B0F0",activeforeground="white",font=("Ariel Rounded MT Bold",15),bg="#00B0F0").place(x=50,y=240,width=250,height=50)
        
        hr=Label(login_frame,bg="lightgray").place(x=50,y=330,width=250,height=2)
        or_=Label(login_frame,text="or",font=("15"),bg="white").place(x=170,y=320)
        
        btn_forget=Button(login_frame,text="Forget Password?",bd=0,bg="white",fg="#00759E",font=("times new roman",10),activebackground="white",activeforeground="#00759E").place(x=120,y=360)
        
        
        #----------------------REGISTER FRAME------------------------
        
        reg_frame=Frame(self.root,bd=2,relief=RIDGE,bg="white").place(x=650,y=570,width=350,height=50)
        reg_lbl=Label(reg_frame,text="Don't have an account?",bg="white").place(x=720,y=585)
        
        btn_signup=Button(reg_frame,text="Sign Up",bg="white",fg="#00759E",bd=0,font=("times new roman",10,"bold")).place(x=850,y=585)

        #--------------------------FIT PHOTO-----------------------------
        
        
        
    
            
        
        self.img1=ImageTk.PhotoImage(file=r"C:\Users\somin\Downloads\img1.png")
        self.img2=ImageTk.PhotoImage(file=r"C:\Users\somin\Downloads\img2.png")
        
        self.lbl_chng_img=Label(self.root,image=self.img2,bd=0,bg="red").place(x=250,y=150,width=135,height=370)
        
        
        
    def login(self):    
        if self.username.get()=="" or self.password.get()=="":
            messagebox.showerror("Error","you must enter username or password")
        elif self.username.get()!="somin" or self.password.get()!="mypassword":
            messagebox.showerror("Error","Invalid username or password")
        else:
            messagebox.showinfo("Information",f"welcome: {self.username.get()}\nYour password:{self.password.get()}")
        
        
        
root=Tk()
obj=Login_System(root)
root.mainloop()
