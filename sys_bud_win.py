import tkinter as tk, os, time, datetime
from PIL import ImageTk, Image

time_dict = {}
for num in range(6, 12):
    time_dict.update({str(num)+'AM':num})
for num in range(2, 6):
    time_dict.update({str(num)+'AM':num})
for num in range(13, 24):
    time_dict.update({str(num)+'PM': num})

time_dict.update({'12PM':12})
count = 13
for num in range(1, 12):
    time_dict.update({str(num)+'PM': count})
    count+=1
time_dict.update({'1AM':25, '12AM':24})

time_dict2 = {}
for num in range(0, 13):
    time_dict2.update({str(num):num})


def current_time():
    now = datetime.datetime.now()
    current_time = now. strftime("%H:%M:%p")
    current_time = current_time.split(':')
    user_current_time_option_label.configure(text = current_time)
    return current_time

time_dict = {}
for num in range(6, 12):
    time_dict.update({str(num)+'AM':num})
for num in range(2, 6):
    time_dict.update({str(num)+'AM':num})
for num in range(13, 24):
    time_dict.update({str(num)+'PM': num})

time_dict.update({'12PM':12})
count = 13
for num in range(1, 12):
    time_dict.update({str(num)+'PM': count})
    count+=1
time_dict.update({'1AM':25, '12AM':24})

time_dict2 = {}
for num in range(0, 13):
    time_dict2.update({str(num):num})

main_shutdown_time = []


def test_func():
    start = current_time()
    close = [close_hour_Var.get(), closeminute_optionvar.get(), close_time_of_day_optionvar.get()]
    
    if start[0][0] == '0':
        start[0] = start[0][1]

    if start[-1] == 'AM' and close[-1] == 'PM':
        if int(close[1]) > int(start[1]):
            hour = time_dict[str(close[0])+'PM'] - time_dict[str(start[0])+'AM']
            minute = abs(int(close[1]) - int(start[1]))
            result = 'hour(s) : %s, Minutes : %s'%(hour,minute)
            shutdown_time = (hour*3600) + (minute * 60)
            # user_shutdown_time_label.config(text=str(result))
            # main_shutdown_time.append(shutdown_time)
            print(main_shutdown_time[-1])
            


        elif int(close[1]) < int(start[1]):
            minute = (int(close[1]) + 60) - int(start[1])
            hour = (time_dict[str(close[0])+'PM'] - time_dict[str(start[0])+'AM']) - 1
            result = 'hour(s) : %s, Minutes : %s'%(hour,minute)
            shutdown_time = (hour*3600) + (minute * 60)
            user_shutdown_time_label.config(text=str(result))
            main_shutdown_time.append(shutdown_time)
            print(main_shutdown_time[-1])
            
    if start[-1] == 'AM' and close[-1] == 'AM':
        if int(close[1]) > int(start[1]):
            hour = time_dict[str(close[0])+'AM'] - time_dict[str(start[0])+'AM']
            minute = abs(int(close[1]) - int(start[1]))
            result = 'hour(s) : %s, Minutes : %s'%(hour,minute)
            shutdown_time = (hour*3600) + (minute * 60)
            user_shutdown_time_label.config(text=str(result))
            main_shutdown_time.append(shutdown_time)
            print(main_shutdown_time[-1])
            

        elif int(close[1]) < int(start[1]):
            minute = (int(close[1]) + 60) - int(start[1])
            hour = (time_dict[str(close[0])+'AM'] - time_dict[str(start[0])+'AM']) - 1
            result = 'hour(s) : %s, Minutes : %s'%(hour,minute)
            shutdown_time = (hour*3600) + (minute * 60)
            user_shutdown_time_label.config(text=str(result))
            main_shutdown_time.append(shutdown_time)
            print(main_shutdown_time[-1])
            
    elif start[-1] == 'PM' and close[-1] == 'PM':
        if int(close[1]) > int(start[1]):
            hour = time_dict[str(close[0])+'PM'] - time_dict[str(start[0])+'PM']
            minute = abs(int(close[1]) - int(start[1]))
            result = 'hour(s) : %s, Minutes : %s'%(hour,minute)
            shutdown_time = (hour*3600) + (minute * 60)
            user_shutdown_time_label.config(text=str(result))
            main_shutdown_time.append(shutdown_time)
            print(main_shutdown_time[-1])
            

        elif int(close[1]) < int(start[1]):
            minute = (int(close[1]) + 60) - int(start[1])
            hour = (time_dict[str(close[0])+'PM'] - time_dict[str(start[0])+'PM']) - 1
            result = 'hour(s) : %s, Minutes : %s'%(hour,minute)
            shutdown_time = (hour*3600) + (minute * 60)
            user_shutdown_time_label.config(text=str(result))
            main_shutdown_time.append(shutdown_time)
            print(main_shutdown_time[-1])
            
    elif start[-1] == 'PM' and close[-1] == 'AM':
        if int(close[1]) > int(start[1]):
            hour = time_dict[str(close[0])+'PM'] - time_dict[str(start[0])+'AM']
            minute = abs(int(close[1]) - int(start[1]))
            result = 'hour(s) : %s, Minutes : %s'%(hour,minute)
            shutdown_time = (hour*3600) + (minute * 60)
            user_shutdown_time_label.config(text=str(result))
            main_shutdown_time.append(shutdown_time)
            print(main_shutdown_time[-1])
            

        elif int(close[1]) < int(start[1]):
            minute = (int(close[1]) + 60) - int(start[1])
            hour = (time_dict[str(close[0])+'PM'] - time_dict[str(start[0])+'AM']) - 1
            result = 'hour(s) : %s, Minutes : %s'%(hour,minute)
            shutdown_time = (hour*3600) + (minute * 60)
            user_shutdown_time_label.config(text=str(result))
            main_shutdown_time.append(shutdown_time)
            print(main_shutdown_time[-1])
            
Canvas_height = 515
canvas_width = 723

window =tk.Tk()
window.title('sleep_buddy(shut-down version)')

canvas = tk.Canvas(window, height = Canvas_height, width = canvas_width)
canvas.pack()

background_image = ImageTk.PhotoImage(Image.open('night.png'))
background_label = tk.Label(window, image = background_image)
background_label.place(relwidth=1,relheight =1, relx = 0, rely = 0)


frame = tk.Frame(window, bg = 'white', bd= 1)
frame.place(relx=0.5, rely=0.06,relwidth=0.37,relheight =0.08, anchor='n')
sys_bud_label = tk.Label(frame, text = 'sleep_buddy',font= "Verdana 10", relief = 'solid', )
sys_bud_label.place(relwidth=1,relheight =1)


start_frame = tk.Frame(window, bg = 'white', bd= 1) #creates start time frame
start_frame.place(relx=0.5, rely=0.19,relwidth=0.30,relheight =0.07, anchor='n') #positions start time frame
user_start_time_button = tk.Button(start_frame, text= 'Get Current system time',  bd = 6, font= "Verdana 10", command = lambda: current_time()) #places label in start time frame
user_start_time_button.place(relwidth=1,relheight =1) #postions label

user_current_entry_frame = tk.Frame(window,   bg = 'white', bd= 1)
user_current_entry_frame.place(relx=0.5, rely=0.26,relwidth=0.22,relheight =0.04, anchor='n')
user_current_time_option_label = tk.Label(user_current_entry_frame, font= "Verdana 10", relief = 'solid', )
user_current_time_option_label.place(relwidth=1,relheight =1)


user_close_time_frame = tk.Frame(window, bg = 'white', bd= 1) #creates close time frame
user_close_time_frame.place(relx=0.5, rely=0.33,relwidth=0.30,relheight =0.05, anchor='n') #positions close time frame
user_close_time_label = tk.Label(user_close_time_frame, text= 'Close Time:', relief = 'solid',) #creates/displays 'close time' label 
user_close_time_label.place(relwidth=1,relheight =1) #formats text display

close_hour_Var = tk.StringVar() #CREATES variable for use selected close hour
close_hour_Var.set('4') # sets default value to 7

user_close_hour_option_frame = tk.Frame(window, bg = 'white', bd= 1, relief = 'solid',) #creates frame for close option
user_close_hour_option_frame.place(relx=0.5, rely=0.37,relwidth=0.25,relheight =0.07, anchor='n') #positions frame
user_close_time_close_option = tk.OptionMenu(user_close_hour_option_frame, close_hour_Var, *time_dict2.keys()) # creates option menu inside close hour frame 
user_close_time_close_option.pack(side = 'left') #positions menu selection to the left side of the frame


closeminute_optionvar = tk.StringVar() #creates a variable for close minute option
closeminute_optionvar.set("00") # assigns default value of 00
close_minute_option_menu = tk.OptionMenu(user_close_hour_option_frame, closeminute_optionvar, *range(0, 60, 5)) #creates option menu
close_minute_option_menu.pack(side = 'left') #positons option menue.


close_time_of_day_optionvar = tk.StringVar()
close_time_of_day_optionvar.set("PM")
close_time_of_day_option_menu = tk.OptionMenu(user_close_hour_option_frame, close_time_of_day_optionvar, 'AM', 'PM')
close_time_of_day_option_menu.pack(side = 'left')




Calc_shutdown_time_button_frame = tk.Frame(window, bg = 'white', bd= 1)
Calc_shutdown_time_button_frame.place(relx=0.5, rely=0.55,relwidth=0.30,relheight =0.07, anchor='n')
Calc_shutdown_time_button = tk.Button(Calc_shutdown_time_button_frame, text = 'Calculate', bd = 6, font= "Verdana 10",  command = lambda: test_func() )
Calc_shutdown_time_button.place(relwidth=1,relheight =1)


user_shutdown_time_frame = tk.Frame(window, bg = 'white', bd= 1)
user_shutdown_time_frame.place(relx=0.5, rely=0.65,relwidth=0.37,relheight =0.06, anchor='n')
user_shutdown_time_label = tk.Label(user_shutdown_time_frame, text= 'shutdown Time in:', relief = 'solid',)
user_shutdown_time_label.place(relwidth=1,relheight =1)

user_shutdown_time_entry_frame = tk.Frame(window, bg = '#1a0500', bd= 5)
user_shutdown_time_entry_frame.place(relx=0.5, rely=0.7,relwidth=0.29,relheight =0.04, anchor='n', )
user_shutdown_time_label = tk.Label(user_shutdown_time_entry_frame)
user_shutdown_time_label.place(relwidth=1,relheight =1)




exit_button_frame = tk.Frame(window, bg = '#1a0500', bd= 5)
exit_button_frame.place(relx=0.5, rely=0.8,relwidth=0.12,relheight =0.08, anchor='n')
exit_button = tk.Button(exit_button_frame, text = 'launch', bd = 6, font= "Verdana 10", bg = '#1a0d00', fg = 'white', command = window.quit)
exit_button.pack()

# exit_butt = tk.Button(frame, text = 'close',  bg ='#8053ac', fg = 'white', bd = 6, font= "Verdana 10 underline")
# exit_butt.place(relx=0.43, rely=0.87, relwidth=0.12,relheight =0.11)


window.mainloop()

time.sleep(main_shutdown_time[-1])
os.system("shutdown /s /t 1")