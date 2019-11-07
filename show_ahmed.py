import tkinter as tk
from PIL import ImageTk, Image

time = {}
for num in range(1, 13):
    time.update({str(num):num})

# count = 13
# for num in range(1, 12):
#     time.update({str(num): count})
#     count+=1

def test_func():
    result = (time[close_hour_Var.get()] - time[hour_optionvar.get()]) * 360
    user_shutdown_time_label.config(text=str(result))
    # count = 0
    # samp = []
    # while count<20:
    #     time.sleep(1)
    #     print('hello')
    #     samp.append('hello')
    #     count+=1
    # print(datetime.datetime.now())
    # print(len(samp))
    # os.system("shutdown /sc /t 1")
        # print('this is the entry:', entry)

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

background_image = ImageTk.PhotoImage(Image.open('sunset.png'))
background_label = tk.Label(window, image = background_image)
background_label.place(relwidth=1,relheight =1, relx = 0, rely = 0)


frame = tk.Frame(window, bg = '#1a0500', bd= 5)
frame.place(relx=0.5, rely=0.06,relwidth=0.37,relheight =0.05, anchor='n')

sys_bud_label = tk.Label(frame, text = 'sleep_buddy',font= "Verdana 10", bd =6,)
sys_bud_label.place(relwidth=1,relheight =1)


start_frame = tk.Frame(window, bg = '#1a0500', bd= 5) #creates start time frame
start_frame.place(relx=0.5, rely=0.19,relwidth=0.37,relheight =0.05, anchor='n') #positions start time frame
user_start_time_label = tk.Label(start_frame, text= 'Start Time:', relief = 'solid',) #places label in start time frame
user_start_time_label.place(relwidth=1,relheight =1) #postions label

hour_optionvar = tk.StringVar() #creates option variable for user's hour selection from option menu
hour_optionvar.set('7') #default vaule is set to here <------

user_current_entry_frame = tk.Frame(window, bg = '#1a0500', bd= 5)
user_current_entry_frame.place(relx=0.5, rely=0.23,relwidth=0.25,relheight =0.07, anchor='n')
user_current_time_option_menu = tk.OptionMenu(user_current_entry_frame, hour_optionvar, *time.keys())
user_current_time_option_menu.pack(side = 'left')

minute_optionvar = tk.StringVar()
minute_optionvar.set("00")
samp_option_menu = tk.OptionMenu(user_current_entry_frame, minute_optionvar, *range(10, 60, 10))
samp_option_menu.pack(side = 'left')

time_of_day_optionvar = tk.StringVar()
time_of_day_optionvar.set("am")
samp_option_menu = tk.OptionMenu(user_current_entry_frame, time_of_day_optionvar, 'am', 'pm')
samp_option_menu.pack(side = 'left')


user_close_time_frame = tk.Frame(window, bg = '#1a0500', bd= 5) #creates close time frame
user_close_time_frame.place(relx=0.5, rely=0.33,relwidth=0.37,relheight =0.05, anchor='n') #positions close time frame
user_close_time_label = tk.Label(user_close_time_frame, text= 'Close Time:', relief = 'solid',) #creates/displays 'close time' label 
user_close_time_label.place(relwidth=1,relheight =1) #formats text display

close_hour_Var = tk.StringVar() #CREATES variable for use selected close hour
close_hour_Var.set('4') # sets default value to 7

user_close_hour_option_frame = tk.Frame(window, bg = '#1a0500', bd= 5) #creates frame for close option
user_close_hour_option_frame.place(relx=0.5, rely=0.37,relwidth=0.25,relheight =0.07, anchor='n') #positions frame
user_close_time_close_option = tk.OptionMenu(user_close_hour_option_frame, close_hour_Var, *time.keys()) # creates option menu inside close hour frame 
user_close_time_close_option.pack(side = 'left') #positions menu selection to the left side of the frame


closeminute_optionvar = tk.StringVar() #creates a variable for close minute option
closeminute_optionvar.set("00") # assigns default value of 00
close_minute_option_menu = tk.OptionMenu(user_close_hour_option_frame, closeminute_optionvar, *range(10, 60, 10)) #creates option menu
close_minute_option_menu.pack(side = 'left') #positons option menue.


close_time_of_day_optionvar = tk.StringVar()
close_time_of_day_optionvar.set("pm")
close_time_of_day_option_menu = tk.OptionMenu(user_close_hour_option_frame, close_time_of_day_optionvar, 'am', 'pm')
close_time_of_day_option_menu.pack(side = 'left')




Calc_shutdown_time_button_frame = tk.Frame(window, bg = '#1a0500', bd= 5)
Calc_shutdown_time_button_frame.place(relx=0.5, rely=0.55,relwidth=0.30,relheight =0.07, anchor='n')
Calc_shutdown_time_button = tk.Button(Calc_shutdown_time_button_frame, text = 'LAUNCH', bd = 6, font= "Verdana 10",  command = lambda: test_func() )
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

start = [hour_optionvar.get(), minute_optionvar.get(), time_of_day_optionvar.get()]
close = [close_hour_Var.get(), closeminute_optionvar.get(), close_time_of_day_optionvar.get()]
print(start)
print(close)

