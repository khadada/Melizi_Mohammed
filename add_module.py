from tkinter import *
from sources_vars import *
add_win = Tk()
add_win.geometry("800x800+0+0")
add_win["background"] = win_bg_color
add_win.title('مليزي محمد                                      إضافة طالب')
#------ title -------------------------------------
title_add = Label(text="برنامجك في خدمتك",fg=grey_c,bg=win_bg_color,font=title_font).pack()
#------ subtitle ----------------------------------
title_add = Label(text=" إضافـــــة طلبـــة ",fg=white_c,bg=win_bg_color,font=sub_title_font).pack()
#========== container ==================
#======================================== 
#--first_name---
frame_f_name = Frame()
frame_f_name.place(x=610,y=200)
f_name_label = Label(frame_f_name,text=":الإسم",font=standard_font).pack()
f_name_input = Entry(frame_f_name,borderwidth=15,relief=FLAT,font=standard_font,justify=CENTER,width=12).pack()

#--last_name---
frame_l_name = Frame()
frame_l_name.place(x=400,y=200)
l_name_label = Label(frame_l_name,text=":اللقب",font=standard_font).pack()
l_name_input = Entry(frame_l_name,borderwidth=15,relief=FLAT,font=standard_font,justify=CENTER,width=12).pack()


#--level---
level = Frame()
level.place(x=220,y=200)
level_label = Label(level,text=":المستوى",font=standard_font).pack()
level_input = Listbox(level,justify=CENTER,font=standard_font,width=13,height=2,selectbackground='red',cursor='hand2')
level_input.insert(1," الأولى ثانوي")
level_input.insert(2," الثانية ثانوي")
level_input.insert(3," الثالثة ثانوي")
level_input.pack()


#--branch---
perfection = Frame()
perfection.place(x=40,y=200)
perfection_label = Label(perfection,text=":الشعبة",font=standard_font).pack()
perfection_input = Listbox(perfection,justify=CENTER,font=standard_font,width=13,height=2,selectbackground='red',cursor='hand2')
perfection_input.insert(1," تقني رياضي")
perfection_input.insert(2," علوم تجريبية")
perfection_input.insert(3," ج مشترك علوم ")
perfection_input.pack()


#--address---
address = Frame()
address.place(x=500,y=400)
address_label = Label(address,text=":العنوان",font=standard_font).pack()
address_input = Listbox(address,justify=CENTER,font=standard_font,width=25,height=2,selectbackground='red',cursor='hand2')
address_input.insert(1," ثانوية رحال نقاوس ")
address_input.insert(2," محلات بخوش العويجة ")
address_input.insert(3," محلات فلان باتنة   ")
address_input.pack()


#--address---
time = Frame()
time.place(x=40,y=400)
time_label = Label(time,text=":التوقيت",font=standard_font).pack()
time_input = Listbox(time,justify=CENTER,font=standard_font,width=25,height=2,selectbackground='red',cursor='hand2')
time_input.insert(1,"08:00  =>  10:00")
time_input.insert(2,"10:00  =>  12:00")
time_input.insert(3,"12:00  =>  14:00")
time_input.insert(4,"16:00  =>  18:00")

time_input.pack()

#------ footer ------------------------------------


add_win.mainloop()