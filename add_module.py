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
#------ container ---------------------------------
#------ footer ------------------------------------


add_win.mainloop()