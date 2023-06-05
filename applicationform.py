from tkinter import*
from tkinter import ttk
from tkinter import messagebox

def enterdata():
    accepted = tcheckvar.get()
    if accepted == "Accepted":
        firstname = fname_entry.get()
        lastname = lnameentry.get()

        if firstname and lastname:
            titleget = titlecombo.get()
            ageget = agespin.get()
            nation = nationalitycombo.get()
            gen = gendercombo.get()

            regstatus = rgstatusvar.get()
            ncourses = comspin.get()
            sem = semspin.get()

            print("First name: ", firstname, "Last name: ", lastname)
            print("Title: ", titleget, "Age: ", ageget, "Nationality: ", nation)
            print("# Courses: ", ncourses, "# Semesters: ", sem)
            print("Registration status", regstatus)
            print("Gender:", gen)
            print("Data entered successfully.")
        
        else:
            messagebox.showwarning(title="Error",message="First name and last name are required.")

    else:
        messagebox.showwarning(title="Error",message="You have not accepted terms and conditions.")


window = Tk()
window.title('Application form')

f = Frame(window)
f.pack()

userinfo = LabelFrame(f,text='User Information')
userinfo.grid(row=0,column=0,padx=20,pady=10)

fname = Label(userinfo,text='First Name')
fname.grid(row=0,column=0)
lname = Label(userinfo,text='Last Name')
lname.grid(row=0,column=1)

fname_entry = Entry(userinfo)
fname_entry.grid(row=1,column=0)
lnameentry = Entry(userinfo)
lnameentry.grid(row=1,column=1)

title = Label(userinfo,text='Title')
titlecombo = ttk.Combobox(userinfo,values=["", "Mr.", "Ms.", "Dr."])
title.grid(row=0,column=2)
titlecombo.grid(row=1,column=2)

age = Label(userinfo,text='Age')
agespin = ttk.Spinbox(userinfo,from_=18,to=110)
age.grid(row=2,column=0)
agespin.grid(row=3,column=0)

nationality = Label(userinfo,text='Nationality')
nationalitycombo = ttk.Combobox(userinfo,values=["Indian", "Pakistani", "Bangladeshi", "British", "American"])
nationality.grid(row=2,column=1)
nationalitycombo.grid(row=3,column=1)

gender = Label(userinfo,text='Gender')
gendercombo = ttk.Combobox(userinfo,values=["","Male","Female","Other"])
gender.grid(row=2,column=2)
gendercombo.grid(row=3,column=2)

for widget in userinfo.winfo_children():
    widget.grid_configure(padx=10,pady=5)


secondframe = LabelFrame(f)
secondframe.grid(row=1,column=0,padx=20,pady=10)

rgstatus = Label(secondframe,text="Registration Status")
rgstatus.grid(row=0,column=0)
rgstatusvar = StringVar(value="Not Registered")
rgcheck = Checkbutton(secondframe,text="Currently Registered",variable=rgstatusvar,onvalue="Registered",offvalue="Not Registered")
rgcheck.grid(row=1,column=0)

comstatus = Label(secondframe,text="#Completed Courses")
comstatus.grid(row=0,column=1)
comspin = Spinbox(secondframe,from_=0,to='infinity')
comspin.grid(row=1,column=1)

semlabel = Label(secondframe,text="#Semesters")
semlabel.grid(row=0,column=2)
semspin = Spinbox(secondframe,from_=0,to='infinity')
semspin.grid(row=1,column=2)

for widget in secondframe.winfo_children():
    widget.grid_configure(padx=19,pady=5)


thirdframe = LabelFrame(f,text="Terms & Conditions")
thirdframe.grid(row=2,column=0,padx=20,pady=10)

tcheckvar = StringVar(value="Not accepted")
tccheck = Checkbutton(thirdframe,text="I accept terms and conditions.",variable=tcheckvar,onvalue="Accepted",offvalue="Not Accepted")
tccheck.grid(row=0,column=0)


Submitbutton = Button(f,text="Enter Data",command=enterdata)
Submitbutton.grid(row=3,column=0,padx=20,pady=10)


window.mainloop()