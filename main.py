from tkinter import *
from tkinter import font
root = Tk()
root.title("برنامج الأستاذ مليزي محمد")
root.configure(padx=40,pady=20)
root.geometry('800x800+0+0')
win_bg_color = '#018cb6'
win_font_color = "#333"
white_c = '#fcfcfc'
root['background'] = win_bg_color


# -----------------------------------------
# ----------- Variable --------------------
#------------------------------------------
title_font = ("Dubai",48,'bold')
sub_title = ("Dubai",16,'bold')
footer_font = ("Dubai",10,'bold')
# bg_img = PhotoImage(file="./particle.png")

# lab_background=Label(root, image=bg_img).place(x=0,y=0)
#=== header =====================================================================
# title-------------------------------------
title = Label(text=" مرحبـــا مليزي محمد", font=title_font,bg=win_bg_color,fg=win_font_color).pack()
# sub title-------------------------------------

sub_title = Label(text="برنامجك لمتابعة تسجيلات الطلبة",bg=win_bg_color,font=sub_title,fg=white_c).pack()


#=== footer =====================================================================
footer_txt = Label(text=" من إنحاز مليزي خالد و مليزي ياسمين",bg=win_bg_color,fg=white_c).pack(side=BOTTOM)

print(font.families())

root.mainloop()