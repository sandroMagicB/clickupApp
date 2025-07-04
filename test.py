from tkinter import *
import requests

# Global Vars
PT = "pk_88662239_ET357T6QDFLZI7ZW6ZIJ7ZNPFHJRO0AO"

# iniciate the instance of a window
window = Tk()
window.geometry("420x420")
window.title("Trash Simplifier")
#window.config(bg="lightgray")

# window.config(background="black")
#icon = PhotoImage(file='trash-347.png')
#window.iconphoto(True,icon)

#window.grid_columnconfigure(1, weight=1, minsize=200)  # Let column 1 expand for the label
#window.grid_rowconfigure(0, weight=1)

# Label for the response information
response_label = Label(window, bg="white", fg="black", text="Response will be shown here", wraplength=350, anchor="w")
response_label.grid(row=0, column=1, padx=20, pady=20, sticky="w")

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
            data = response.json()
            response_label.config(text=f"Success: {data}")
        else:
            print("Error:", response.status_code)
            response_label.config(text=f"Error: {response.status_code}")
    except Exception as e:
        print("Request failed:", e)

def quit_app():
    print("Closing App..")
    window.destroy()

# Buttons
button = Button(window, text='Click', command=click)
button.grid(row=1, column=0, padx=20, pady=10, sticky="w")

quit_button = Button(window, text='Close', command=quit_app)
quit_button.grid(row=2, column=0, padx=20, pady=10, sticky="w")



window.mainloop()
