from tkinter import *
import requests

# Global Vars
PT = "pk_88662239_ET357T6QDFLZI7ZW6ZIJ7ZNPFHJRO0AO"

# iniciate the instance of a window
window = Tk()
window.geometry("420x420")
window.title("Trash Simplifier")

# window.config(background="black")
#icon = PhotoImage(file='trash-347.png')
#window.iconphoto(True,icon)

def click():
    url = "https://api.clickup.com/api/v2/user"
    headers = {
        "Authorization": PT,
        "Accept": "application/json"
    }

    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            print("Success:", response.json())
        else:
            print("Error:", response.status_code)
    except Exception as e:
        print("Request failed:", e)

def quit_app():
    print("Closing App..")
    window.destroy()

button = Button(window,text='Click', command=click)
button.pack()

quit_button = Button(window,text='Close', command=quit_app)
quit_button.pack()



window.mainloop()
