from tkinter import *
import datetime
import time
import playsound
import os

def alarm(set_alarm_timer):
    sound_path = os.getcwd() + "/Popular Alarm Clock Sound Effect-77S70NhRoBc.m4a"
    while True:
        time.sleep(1)
        current_time = datetime.datetime.now()
        now = current_time.strftime("%H:%M:%S")
        date = current_time.strftime("%d/%m:%y")
        print(f"The set date is {date}")
        print(now)
        if now == set_alarm_timer:
            print("Wake up")
        playsound.playsound(sound_path)
        break

def actual_time():
    set_alarm_timer = f"{hour.get()}:{min.get()}:{sec.get()}"
    alarm(set_alarm_timer)

clock = Tk()

clock.title("Alarm clock")
clock.geometry("408x280")
time_format = Label(clock, text="Hour Min Sec", font=60).place(x=110)
set_your_alarm = Label(clock, text="When to wake up", fg="blue", relief="solid", font=("Helevetica",7,"bold")).place(x=0, y=29)

#Variables required to set the alarm
hour = StringVar()
min = StringVar()
sec = StringVar()

#Required time to set the alarm clock
hour_time = Entry(clock, textvariable=hour, bg="pink", width=15).place(x=110,y=30)
min_time = Entry(clock, textvariable=min, bg="pink", width=15).place(x=150,y=30)
sec_time = Entry(clock, textvariable=sec, bg="pink", width=15).place(x=208,y=30)

#Take time inputer by user
submit = Button(clock, text="Set alarm", fg="red", width=10, command=actual_time).place(x=110,y=70)

clock.mainloop()