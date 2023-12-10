from tkinter import *
import random
import datetime

class Bill_App:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1300x700+0+0")
        self.root.maxsize(width = 1525,height = 750)
        self.root.minsize(width = 1525,height = 800)
        self.root.title("Surya Poultry Farm")
        
        #====================Variables========================#
        self.cus_name = StringVar()
        self.c_phone = StringVar()
        
        #For Generating Random Bill Numbers
        x = random.randint(1,9999)
        self.c_bill_no = StringVar()
        
        #Seting Value to variable
        self.c_bill_no.set(int(x))
        self.BY_PASS_20KG = IntVar()#1
        self.BY_PASS_50KG = IntVar()#2
        self.BY_PASS_50KG_Mysore = IntVar()#3
        self.BY_PASS_70KG_PP_Mysore = IntVar()#4
        self.BY_PASS_70KG_PP = IntVar()#5
        self.BY_PASS_70KG_J = IntVar()#6
        self.PROMAX_50KG = IntVar()#7
        self.SP_70KG_PP = IntVar()#8
        self.SP_20 = IntVar()#9
        self.SPL_MILKRATION_50KG = IntVar()#10
        self.SP_50KG = IntVar()#11
        self.Wheat_Bran_50KG = IntVar()#12
        


        self.total_items = StringVar()



        #===================================
        bg_color = "#074463"
        fg_color = "white"
        lbl_color = 'white'
        
        #Title of App
        title = Label(self.root,text = "Surya Poultry Farm",bd = 12,relief = GROOVE,fg = fg_color,bg = bg_color,font=("times new roman",30,"bold"),pady = 3).pack(fill = X)

        #==========Customers Frame==========#
        F1 = LabelFrame(text = "Customer Details",font = ("time new roman",12,"bold"),fg = "gold",bg = bg_color,relief = GROOVE,bd = 10)
        F1.place(x = 0,y = 100,relwidth = 10)
        #===============Customer Name===========#
        cname_lbl = Label(F1,text="Customer Name",bg = bg_color,fg = fg_color,font=("times new roman",15,"bold")).grid(row = 0,column = 0,padx = 10,pady = 5)
        cname_en = Entry(F1,bd = 8,relief = GROOVE,textvariable = self.cus_name)
        cname_en.grid(row = 0,column = 1,ipady = 3,ipadx = 30,pady = 5)
        #=================Customer Phone==============#
        cphon_lbl = Label(F1,text = "Phone No",bg = bg_color,fg = fg_color,font = ("times new roman",15,"bold")).grid(row = 0,column = 2,padx = 20)
        cphon_en = Entry(F1,bd = 8,relief = GROOVE,textvariable = self.c_phone)
        cphon_en.grid(row = 0,column = 3,ipady = 4,ipadx = 30,pady = 5)
        #====================Customer Bill No==================#
        cbill_lbl = Label(F1,text = "Bill No.",bg = bg_color,fg = fg_color,font = ("times new roman",15,"bold"))
        cbill_lbl.grid(row = 0,column = 4,padx = 20)
        cbill_en = Entry(F1,bd = 8,relief = GROOVE,textvariable = self.c_bill_no)
        cbill_en.grid(row = 0,column = 5,ipadx = 30,ipady = 4,pady = 5)
        #====================Bill Search Button===============#
        bill_btn = Button(F1,text = "Enter",bd = 7,relief = GROOVE,font = ("times new roman",12,"bold"),bg = bg_color,fg = fg_color)
        bill_btn.grid(row = 0,column = 6,ipady = 5,padx = 60,ipadx = 19,pady = 5)



        #==================By Pass Frame=====================#
        F2 = LabelFrame(self.root,text = 'BY pass frame',bd = 10,relief = GROOVE,bg = bg_color,fg = "gold",font = ("times new roman",13,"bold"))
        F2.place(x = 1,y = 200,width = 400,height = 400)
        #===========BY20
        by20_lbl = Label(F2,font = ("times new roman",10,"bold"),fg = lbl_color,bg = bg_color,text = "BY_PASS_20KG")
        by20_lbl.grid(row = 0,column = 0,padx = 1,pady = 20)
        by20_en = Entry(F2,bd = 8,relief = GROOVE,textvariable= self.BY_PASS_20KG)
        by20_en.grid(row = 0,column = 1,ipady = 5,ipadx = 5)
        #=======BY50
        face_lbl = Label(F2,font = ("times new roman",10,"bold"),fg = lbl_color,bg = bg_color,text = "BY_PASS_50KG")
        face_lbl.grid(row = 1,column = 0,padx = 10,pady = 20)
        face_en = Entry(F2,bd = 8,relief = GROOVE,textvariable = self.BY_PASS_50KG)
        face_en.grid(row = 1,column = 1,ipady = 5,ipadx = 5)
        #========BY50 my
        wash_lbl = Label(F2,font = ("times new roman",10,"bold"),fg = lbl_color,bg = bg_color,text = "BY_PASS_50KG_Mysore")
        wash_lbl.grid(row = 2,column = 0,padx = 10,pady = 20)
        wash_en = Entry(F2,bd = 8,relief = GROOVE,textvariable = self.BY_PASS_50KG_Mysore)
        wash_en.grid(row = 2,column = 1,ipady = 5,ipadx = 5)
        #========By 70 pp my
        hair_lbl = Label(F2,font = ("times new roman",10,"bold"),fg = lbl_color,bg = bg_color,text = "BY_PASS_70KG_PP_Mysore")
        hair_lbl.grid(row = 3,column = 0,padx = 10,pady = 20)
        hair_en = Entry(F2,bd = 8,relief = GROOVE,textvariable = self.BY_PASS_70KG_PP_Mysore)
        hair_en.grid(row = 3,column = 1,ipady = 5,ipadx = 5)
        #============BY_PASS_70KG_PP
        lot_lbl = Label(F2,font = ("times new roman",10,"bold"),fg = lbl_color,bg = bg_color,text = "BY_PASS_70KG_PP")
        lot_lbl.grid(row = 4,column = 0,padx = 10,pady = 20)
        lot_en = Entry(F2,bd = 8,relief = GROOVE,textvariable = self.BY_PASS_70KG_PP)
        lot_en.grid(row = 4,column = 1,ipady = 5,ipadx = 5)
        #============BY_PASS_70KG_J
        lot_lbl = Label(F2,font = ("times new roman",10,"bold"),fg = lbl_color,bg = bg_color,text = "BY_PASS_70KG_J")
        lot_lbl.grid(row = 5,column = 0,padx = 10,pady = 20)
        lot_en = Entry(F2,bd = 8,relief = GROOVE,textvariable = self.BY_PASS_70KG_J)
        lot_en.grid(row = 5,column = 1,ipady = 5,ipadx = 5)



        #==================SP Frame=====================#
        F2 = LabelFrame(self.root,text = 'SP Frame',bd = 10,relief = GROOVE,bg = bg_color,fg = "gold",font = ("times new roman",13,"bold"))
        F2.place(x = 400,y = 200,width = 325,height = 400)
        #===========Frame Content
        sp_20_lbl = Label(F2,font = ("times new roman",10,"bold"),fg = lbl_color,bg = bg_color,text = "SP_20KG")
        sp_20_lbl.grid(row = 0,column = 0,padx = 10,pady = 20)
        sp_20_en = Entry(F2,bd = 8,relief = GROOVE,textvariable = self.SP_20)
        sp_20_en.grid(row = 0,column = 1,ipady = 5,ipadx = 5)
        #=======
        SP_70KG_PP_lbl = Label(F2,font = ("times new roman",10,"bold"),fg = lbl_color,bg = bg_color,text = "SP_70KG")
        SP_70KG_PP_lbl.grid(row = 1,column = 0,padx = 10,pady = 20)
        SP_70KG_PP_en = Entry(F2,bd = 8,relief = GROOVE,textvariable = self.SP_70KG_PP)
        SP_70KG_PP_en.grid(row = 1,column = 1,ipady = 5,ipadx = 5)
        #========
        SP_50_lbl = Label(F2,font = ("times new roman",10,"bold"),fg = lbl_color,bg = bg_color,text = "SP_50KG")
        SP_50_lbl.grid(row = 3,column = 0,padx = 10,pady = 20)
        SP_50_en = Entry(F2,bd = 8,relief = GROOVE,textvariable = self.SP_50KG)
        SP_50_en.grid(row = 3,column = 1,ipady = 5,ipadx = 5)
        #============
        



        #==================Other Stuff=====================#

        F2 = LabelFrame(self.root,text = 'Others',bd = 10,relief = GROOVE,bg = bg_color,fg = "gold",font = ("times new roman",13,"bold"))
        F2.place(x = 725,y = 200,width = 380,height = 400)
        #===========Frame Content
        PROMAX_50KG_lbl = Label(F2,font = ("times new roman",10,"bold"),fg = lbl_color,bg = bg_color,text = "PROMAX_50KG")
        PROMAX_50KG_lbl.grid(row = 2,column = 0,padx = 10,pady = 20)
        PROMAX_50KG_en = Entry(F2,bd = 8,relief = GROOVE,textvariable = self.PROMAX_50KG)
        PROMAX_50KG_en.grid(row = 2,column = 1,ipady = 5,ipadx = 5)
        #=======
        SPL_MILKRATION_50KG_lbl = Label(F2,font = ("times new roman",10,"bold"),fg = lbl_color,bg = bg_color,text = "SPL_MILKRATION_50KG")
        SPL_MILKRATION_50KG_lbl.grid(row = 4,column = 0,padx = 10,pady = 20)
        SPL_MILKRATION_50KG_en = Entry(F2,bd = 8,relief = GROOVE,textvariable = self.SPL_MILKRATION_50KG)
        SPL_MILKRATION_50KG_en.grid(row = 4,column = 1,ipady = 5,ipadx = 5)
        #=====
        


        #===================Bill Aera================#
        F3 = Label(self.root,bd = 10,relief = GROOVE)
        F3.place(x = 1111,y = 200,width = 420,height = 400)
        #===========
        bill_title = Label(F3,text = "SURYA POULTRY FARM",font = ("Lucida",13,"bold"),bd= 10,relief = GROOVE)
        bill_title.pack(fill = X)
        #==============
    
        #============
        scroll_y = Scrollbar(F3,orient = VERTICAL)
        self.txt = Text(F3,yscrollcommand = scroll_y.set)
        scroll_y.pack(side = RIGHT,fill = Y)
        scroll_y.config(command = self.txt.yview)
        self.txt.pack(fill = BOTH,expand = 1)



        #===========Buttons Frame=============#
        F4 = LabelFrame(self.root,text = 'Bill Menu',bd = 10,relief = GROOVE,bg = bg_color,fg = "gold",font = ("times new roman",13,"bold"))
        F4.place(x = 0,y = 610,relwidth = 1,height = 145)
        #===================
        ByPass_lbl = Label(F4,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Total BYPASS")
        ByPass_lbl.grid(row = 0,column = 0,padx = 10,pady = 0)
        ByPass_en = Entry(F4,bd = 8,relief = GROOVE,textvariable = self.total_items)
        ByPass_en.grid(row = 0,column = 1,ipady = 2,ipadx = 5)
        
        sp_lbl = Label(F4,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Total SP")
        sp_lbl.grid(row = 0,column = 1,padx = 10,pady = 0)
        sp_en = Entry(F4,bd = 8,relief = GROOVE,textvariable = self.total_items)
        sp_en.grid(row = 0,column = 1,ipady = 2,ipadx = 5)
        
        others_lbl = Label(F4,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "others total")
        others_lbl.grid(row = 0,column = 2,padx = 10,pady = 0)
        others_en = Entry(F4,bd = 8,relief = GROOVE,textvariable = self.total_items)
        others_en.grid(row = 0,column = 1,ipady = 2,ipadx = 5)

        total_btn = Button(F4,text = "Total",bg = bg_color,fg = fg_color,font=("lucida",12,"bold"),bd = 7,relief = GROOVE,command = self.total)
        total_btn.grid(row = 1,column = 4,ipadx = 20,padx = 30)

        genbill_btn = Button(F4,text = "Generate Bill",bg = bg_color,fg = fg_color,font=("lucida",12,"bold"),bd = 7,relief = GROOVE,command = self.bill_area)
        genbill_btn.grid(row = 1,column = 5,ipadx = 20)

        #====================
        clear_btn = Button(F4,text = "Clear",bg = bg_color,fg = fg_color,font=("lucida",12,"bold"),bd = 7,relief = GROOVE,command = self.clear)
        clear_btn.grid(row = 1,column = 6,ipadx = 20,padx = 30)

        #======================
        exit_btn = Button(F4,text = "Exit",bg = bg_color,fg = fg_color,font=("lucida",12,"bold"),bd = 7,relief = GROOVE,command = self.exit)
        exit_btn.grid(row = 1,column = 7,ipadx = 20)
#Function to get total prices
    def total(self):
        #=================Total Bypass Prices
        self.total_ByPass_prices = (
            (self.BY_PASS_20KG.get() * 484)+
            (self.BY_PASS_50KG.get() * 1170)+
            (self.BY_PASS_50KG_Mysore.get() * 1060)+
            (self.BY_PASS_70KG_PP_Mysore.get() * 1496)+
            (self.BY_PASS_70KG_PP.get() * 260)+
            (self.BY_PASS_70KG_J.get() *80)
        )
        self.total_ByPass.set("Rs. "+str(self.total_ByPass_prices))
      #  self.tax_ByPass.set("Rs. "+str(round(self.total_ByPass_prices*0.05)))
        #====================Total SP Prices
        self.total_sp_prices = (
            (self.SP_20.get()*100)+
            (self.SP_70KG_PP.get() * 180)+
            (self.SP_50KG.get() * 20)

        )
        self.total_sp.set("Rs. "+str(self.total_sp_prices))
       # self.tax_groc.set("Rs. "+str(round(self.total_sp_prices*0.05)))
        #======================Total Other Prices
        self.total_other_prices = (
            (self.PROMAX_50KG.get() * 80)+
            (self.SPL_MILKRATION_50KG.get() * 170)

        )
        self.total_others.set("Rs. "+str(self.total_other_prices))
       # self.tax_other.set("Rs. "+str(round(self.total_other_prices*0.05)))


#Function For Text Area
    def welcome_soft(self):
        self.txt.delete('1.0',END)
        self.txt.insert(END,"       Welcome To Deepak Retail\n")
        self.txt.insert(END,f"\nBill No. : {str(self.c_bill_no.get())}")
        self.txt.insert(END,f"\nCustomer Name : {str(self.cus_name.get())}")
        self.txt.insert(END,f"\nPhone No. : {str(self.c_phone.get())}")
        self.txt.insert(END,"\n=========================================")
        self.txt.insert(END,"\nProduct      \t\t    Qty       \t\t Price")
        self.txt.insert(END,"\n=========================================")

#Function to clear the bill area
    def clear(self):
        self.txt.delete('1.0',END)

#Add Product name , qty and pBY_PASS_70KG_J to bill area
    def bill_area(self):
      #10  bill_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.welcome_soft()
        if self.BY_PASS_20KG.get() != 0:
            self.txt.insert(END,f"\nBY_PASS_20KG \t\t {self.BY_PASS_20KG.get()}\t       {self.BY_PASS_20KG.get() * 484}")
        if self.BY_PASS_50KG.get() != 0:
            self.txt.insert(END,f"\nFace Cream  \t\t  {self.BY_PASS_50KG.get()}\t            {self.BY_PASS_50KG.get() * 140}")
        if self.BY_PASS_50KG_Mysore.get() != 0:
            self.txt.insert(END,f"\nFace Wash \t\t    {self.BY_PASS_50KG_Mysore.get()}\t    {self.BY_PASS_50KG_Mysore.get() * 240}")
        if self.BY_PASS_70KG_PP_Mysore.get() != 0:
            self.txt.insert(END,f"\nHair Spray        {self.BY_PASS_70KG_PP_Mysore.get()}   {self.BY_PASS_70KG_PP_Mysore.get() * 340}")
        if self.BY_PASS_70KG_PP.get() != 0 :
            self.txt.insert(END,f"\nBody Lotion       {self.BY_PASS_70KG_JUTE.get()}        {self.BY_PASS_70KG_JUTE.get() * 260}")
        if self.SP_20.get() != 0:
            self.txt.insert(END,f"\nSP_20             {self.SP_20.get()}                    {self.SP_20.get() * 100}")
        if self.SP_70KG_PP.get() != 0:
            self.txt.insert(END,f"\nFood Oil          {self.SP_70KG_PP.get()}               {self.SP_70KG_PP.get() * 180}")
        if self.PROMAX_50KG.get() != 0:
            self.txt.insert(END,f"\nPROMAX_50KG       {self.PROMAX_50KG.get()}              {self.PROMAX_50KG.get() * 80}")
        if self.BY_PASS_70KG_J.get() != 0:
            self.txt.insert(END,f"\nBY_PASS_70KG_J    {self.BY_PASS_70KG_J.get()}           {self.BY_PASS_70KG_J.get() * 80}")
        if self.SPL_MILKRATION_50KG.get() != 0:
            self.txt.insert(END,f"\nSPL_MILKRATION_50KG             {self.SPL_MILKRATION_50KG.get()}           {self.SPL_MILKRATION_50KG.get() * 170}")
        if self.SP_50KG.get() != 0:
            self.txt.insert(END,f"\nSP_50KG              {self.SP_50KG.get()}           {self.SP_50KG.get() * 20}")
        if self.Wheat_Bran_50KG.get() != 0:
            self.txt.insert(END,f"\nWheat_Bran_50KG              {self.Wheat_Bran_50KG.get()}           {self.Wheat_Bran_50KG.get() * 60}")
        self.txt.insert(END,"\n===================================")
       # self.txt.insert(END,f"\n                      Total : {self.total_ByPass_prices+self.total_sp_prices+self.total_other_prices+self.total_ByPass_prices * 0.05+self.total_sp_prices * 0.05+self.total_other_prices * 0.05}")

    #Function to exit
    def exit(self):
        self.root.destroy()

    #Function To Clear All Fields



root = Tk()
object = Bill_App(root)
root.mainloop()


