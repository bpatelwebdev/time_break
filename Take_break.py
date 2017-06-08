import time
import webbrowser

total_break = 3
break_number = 0

print("This program started on"+time.ctime())
while(break_number<total_break):
    time.sleep(10)
    webbrowser.open("https://www.youtube.com/watch?v=vnDbGgzs_To")
    break_number += 1