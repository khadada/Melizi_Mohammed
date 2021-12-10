from tkinter import *
#colors------------------------
win_bg_color = '#3CCBF7'
grey_c = "#2C2626"
white_c = '#fff'
green_c = "#13DF8D"
red_c = "#F35D5D"
purple_c = "#B281FD"
#fonts--------------------------
title_font = ("Dubai",48,'bold')
sub_title = ("Dubai",16,'bold')
footer_font = ("Dubai",10,'bold')
btn_font = ("Dubai",16,'bold')

root = Tk()
root.title("برنامج الأستاذ مليزي محمد")
root.configure(padx=40,pady=20)
root.geometry('800x800+0+0')
root['background'] = win_bg_color


# -----------------------------------------
# ----------- fonts --------------------
#------------------------------------------

# bg_img = PhotoImage(file="./particle.png")

# lab_background=Label(root, image=bg_img).place(x=0,y=0)
#=== header =====================================================================
# title-------------------------------------
title = Label(text=" مرحبـــا مليزي محمد", font=title_font,bg=win_bg_color,fg=grey_c).pack()
# sub title-------------------------------------

sub_title = Label(text="برنامجك لمتابعة تسجيلات الطلبة",bg=win_bg_color,font=sub_title,fg=white_c).pack()

# container -------------------------------------

add_btn = Button(text='إضـــــافة', fg=grey_c,bg=green_c,width=10,font=btn_font).place(x=300,y=280)
add_btn = Button(text='بـحـــــث ', fg=grey_c,bg=purple_c,width=10,font=btn_font).place(x=300,y=380)
add_btn = Button(text='حـــــذف', fg=grey_c,bg=red_c,width=10,font=btn_font).place(x=300,y=480)














#=== footer =====================================================================
footer_txt = Label(text=" من إنحاز مليزي خالد و مليزي ياسمين",bg=win_bg_color,fg=white_c).pack(side=BOTTOM)


root.mainloop()