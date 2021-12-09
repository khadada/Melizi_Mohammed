from tkinter import *
root = Tk()
root.title("برنامج الأستاذ مليزي محمد")
root.configure(padx=0,pady=0)
root.geometry('800x800+0+0')
win_bg_color = '#018cb6'
win_font_color = "#333"
root['background'] = win_bg_color


# -----------------------------------------
# ----------- Variable --------------------
#------------------------------------------
title_font = ("Traditional Arabiv",35,'bold')

# bg_img = PhotoImage(file="./particle.png")

# lab_background=Label(root, image=bg_img).place(x=0,y=0)

# title-------------------------------------
title = Label(text="مرحبا مليزي محمد", font=title_font,bg=win_bg_color,fg=win_font_color).pack()






root.mainloop()