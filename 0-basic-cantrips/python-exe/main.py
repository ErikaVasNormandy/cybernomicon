import tkinter
import easygui
import os
msg = "Load application..."
title="Tom's Hardware Application Starter"
choices = ["Google Chrome","Slack","PuTTY"]
reply = easygui.buttonbox(msg, title , choices=choices)
if reply == "Google Chrome":
    os.startfile("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")
elif reply == "Slack":
    os.startfile("C:\\Users\\lespo\\AppData\\Local\\slack\\slack.exe")
elif reply == "PuTTY":
    os.system("putty")
else:
    print("Done")
