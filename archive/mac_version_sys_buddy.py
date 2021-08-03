import tkinter as tk
from PIL import ImageTk, Image


Canvas_height = 615
canvas_width = 723

window = tk.Tk()
window.title('sys_buddy(shut-down version)')

canvas = tk.Canvas(window, height=Canvas_height, width=canvas_width)
canvas.pack()

worktime = {}
for num in range(7,12):
    worktime[str(num)+'am'] = num

worktime.update({'12pm':12})
count = 13
for num in range(1,12):
    worktime.update({str(num)+'pm':count})
    count+=1



background_image = ImageTk.PhotoImage(Image.open('sunset.png'))
background_label = tk.Label(window, image=background_image)
background_label.place(relwidth=1, relheight=1,)


frame = tk.Frame(window, bg='#002db3', bd=5)
frame.place(relx=0.5, rely=0.06, relwidth=0.37, relheight=0.05, anchor='n')


sys_bud_label = tk.Label(frame, text='Sys_buddy', font="Verdana 10", bg='#4747d1', fg='white')
sys_bud_label.place(relwidth=1, relheight=1)

resumption_frame = tk.Frame(window, bg='#002db3', bd=5)
resumption_frame.place(relx=0.5, rely=0.35, relwidth=0.37, relheight=0.05, anchor='n')
user_resumption_time_label = tk.Label(resumption_frame, text='Resumption Time:', relief='solid')
user_resumption_time_label.place(relwidth=1, relheight=1)


user_resumption_entry_frame = tk.Frame(window, bg='#002db3', bd=5)
user_resumption_entry_frame.place(relx=0.5, rely=0.39, relwidth=0.09, relheight=0.05, anchor='n')
user_resumption_time_entry = tk.Entry(user_resumption_entry_frame)
user_resumption_time_entry.pack()


user_close_time_frame = tk.Frame(window, bg='#002db3', bd=5)
user_close_time_frame.place(relx=0.5, rely=0.45, relwidth=0.37, relheight=0.05, anchor='n')
user_close_time_label = tk.Label(user_close_time_frame, text='Close Time:', relief='solid')
user_close_time_label.place(relwidth=1, relheight=1)


user_close_time_entry_frame = tk.Frame(window, bg='#002db3', bd=5)
user_close_time_entry_frame.place(relx=0.5, rely=0.49, relwidth=0.09, relheight=0.05, anchor='n')
user_close_time_entry = tk.Entry(user_close_time_entry_frame)
user_close_time_entry.pack()


Calc_shutdown_time_button_frame = tk.Frame(window, bg='#002db3')
Calc_shutdown_time_button_frame.place(
    relx=0.5, rely=0.55, relwidth=0.30, relheight=0.04, anchor='n')
Calc_shutdown_time_button = tk.Button(
    Calc_shutdown_time_button_frame, text='calculate shutdown time',)
Calc_shutdown_time_button.pack()


user_shutdown_time_frame = tk.Frame(window, bg='#002db3', bd=5)
user_shutdown_time_frame.place(relx=0.5, rely=0.65, relwidth=0.37, relheight=0.06, anchor='n')
user_shutdown_time_label = tk.Label(user_shutdown_time_frame, text='shutdown Time:', relief='solid')
user_shutdown_time_label.place(relwidth=1, relheight=1)


user_shutdown_time_entry_frame = tk.Frame(window, bg='#002db3', bd=5)
user_shutdown_time_entry_frame.place(relx=0.5, rely=0.7, relwidth=0.07, relheight=0.04, anchor='n')
user_shutdown_time_entry = tk.Entry(user_shutdown_time_entry_frame)
user_shutdown_time_entry.pack()

exit_button_frame = tk.Frame(window, bg='#002db3',)
exit_button_frame.place(relx=0.5, rely=0.8, relwidth=0.09, relheight=0.04, anchor='n')
exit_button = tk.Button(exit_button_frame, text='Close', command=window.quit)
exit_button.pack()

window.mainloop()
