import webbrowser
import time

total_breaks = 3
break_count = 0

print("This program started on "+time.ctime())
while(break_count < total_breaks):
    time.sleep(10)
    webbrowser.open('https://youtu.be/3cshiIac91U?t=4m11s')
    break_count = break_count + 1
