
import tkinter as tk
from PIL import ImageTk, Image

time = {}
for num in range(7, 11):
    time.update({str(num)+'am':num})
time.update({'12pm':12})
count = 13
for num in range(1, 12):
    time.update({str(num)+'pm': count})
    count+=1
# da47ca8f8d873c1e71c99be10d832cb3
#api.openweathermap.org/data/2.5/forecast?q={city name},{country code}

def test_func():
    result = time.get(close_optionVar.get()) - time.get(optionVar.get())
    user_shutdown_time_label.config(text=str(result))
    print('this is the entry:', entry)

# def get_weather(city):
#     weather_key = 'da47ca8f8d873c1e71c99be10d832cb3'
#     url = 'https://api.openweathermap.org/data/2.5/forecast'
#     params = {'APPIS': weather_key, 'q': city, 'units': imperial }


Canvas_height = 515
canvas_width = 723

window =tk.Tk()
window.title('sleep_buddy(shut-down version)')

canvas = tk.Canvas(window, height = Canvas_height, width = canvas_width)
canvas.pack()

background_image = ImageTk.PhotoImage(Image.open('night.png'))
background_label = tk.Label(window, image = background_image)
background_label.place(relwidth=1,relheight =1, relx = 0, rely = 0)


frame = tk.Frame(window, bg = '#1a0500', bd= 5)
frame.place(relx=0.5, rely=0.06,relwidth=0.37,relheight =0.05, anchor='n')

sys_bud_label = tk.Label(frame, text = 'sleep_buddy',font= "Verdana 10", bd =6,)
sys_bud_label.place(relwidth=1,relheight =1)


resumption_frame = tk.Frame(window, bg = '#1a0500', bd= 5)
resumption_frame.place(relx=0.5, rely=0.35,relwidth=0.37,relheight =0.05, anchor='n')
user_resumption_time_label = tk.Label(resumption_frame, text= 'Resumption Time:', relief = 'solid',)
user_resumption_time_label.place(relwidth=1,relheight =1)



optionVar = tk.StringVar()
optionVar.set("7am")

user_resumption_entry_frame = tk.Frame(window, bg = '#1a0500', bd= 5)
user_resumption_entry_frame.place(relx=0.5, rely=0.39,relwidth=0.16,relheight =0.07, anchor='n')
user_resumption_time_option_menu = tk.OptionMenu(user_resumption_entry_frame, optionVar, *time.keys())
user_resumption_time_option_menu.pack()


close_optionVar = tk.StringVar()
close_optionVar.set("7am")

user_close_time_frame = tk.Frame(window, bg = '#1a0500', bd= 5)
user_close_time_frame.place(relx=0.5, rely=0.45,relwidth=0.37,relheight =0.05, anchor='n')
user_close_time_label = tk.Label(user_close_time_frame, text= 'Close Time:', relief = 'solid',)
user_close_time_label.place(relwidth=1,relheight =1)

user_close_time_entry_frame = tk.Frame(window, bg = '#1a0500', bd= 5)
user_close_time_entry_frame.place(relx=0.5, rely=0.49,relwidth=0.09,relheight =0.05, anchor='n')
user_close_time_close_option = tk.OptionMenu(user_close_time_entry_frame, close_optionVar, *time.keys())
user_close_time_close_option.pack()


Calc_shutdown_time_button_frame = tk.Frame(window, bg = '#1a0500', bd= 5)
Calc_shutdown_time_button_frame.place(relx=0.5, rely=0.55,relwidth=0.30,relheight =0.07, anchor='n')
Calc_shutdown_time_button = tk.Button(Calc_shutdown_time_button_frame, text = 'calculate shutdown time', bd = 6, font= "Verdana 10",  command = lambda: test_func() )
Calc_shutdown_time_button.pack()


user_shutdown_time_frame = tk.Frame(window, bg = '#1a0500', bd= 5)
user_shutdown_time_frame.place(relx=0.5, rely=0.65,relwidth=0.37,relheight =0.06, anchor='n')
user_shutdown_time_label = tk.Label(user_shutdown_time_frame, text= 'shutdown Time:', relief = 'solid',)
user_shutdown_time_label.place(relwidth=1,relheight =1)

user_shutdown_time_entry_frame = tk.Frame(window, bg = '#1a0500', bd= 5)
user_shutdown_time_entry_frame.place(relx=0.5, rely=0.7,relwidth=0.07,relheight =0.04, anchor='n', )
user_shutdown_time_label = tk.Label(user_shutdown_time_entry_frame)
user_shutdown_time_label.place(relwidth=1,relheight =1)




exit_button_frame = tk.Frame(window, bg = '#1a0500', bd= 5)
exit_button_frame.place(relx=0.5, rely=0.8,relwidth=0.12,relheight =0.08, anchor='n')
exit_button = tk.Button(exit_button_frame, text = 'Close', bd = 6, font= "Verdana 10", bg = '#1a0d00', fg = 'white', command = window.quit)
exit_button.pack()

# exit_butt = tk.Button(frame, text = 'close',  bg ='#8053ac', fg = 'white', bd = 6, font= "Verdana 10 underline")
# exit_butt.place(relx=0.43, rely=0.87, relwidth=0.12,relheight =0.11)



window.mainloop()

print('resumption time:', optionVar.get(), 'close time:',close_optionVar.get())  