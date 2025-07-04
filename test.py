from tkinter import *
import requests
import json

# Global Vars
PT = "pk_88662239_ET357T6QDFLZI7ZW6ZIJ7ZNPFHJRO0AO"
#MS_SPACE_ID =
HEADERS = {
    "Authorization": PT,
    "Accept": "application/json"
}
# iniciate the instance of a window
window = Tk()
window.geometry("420x420")
window.title("Trash Simplifier")
#window.config(bg="lightgray")

# window.config(background="black")
#icon = PhotoImage(file='trash-347.png')
#window.iconphoto(True,icon)

# Label for the response information
response_label = Label(window, bg="white", fg="black", text="Response will be shown here", justify=LEFT, wraplength=350, anchor="w")
response_label.grid(row=0, column=1, padx=20, pady=20, sticky="w")



def get_user():
    url = "https://api.clickup.com/api/v2/user"

    try:
        response = requests.get(url, headers=HEADERS)
        if response.status_code == 200:
            print("Success:", response.json())
            data = json.dumps(response.json(), indent=2)
            response_label.config(text=f"Success: {data}")
        else:
            print("Error:", response.status_code)
            response_label.config(text=f"Error: {response.status_code}")
    except Exception as e:
        print("Request failed:", e)

def get_team():
    url = "https://api.clickup.com/api/v2/team"
    try:
        response = requests.get(url, headers=HEADERS)
        if response.status_code == 200:
            for team in response.json()["teams"]:
                print("Team:", team["name"], "ID:", team["id"])
        else:
            print("Error:", response.status_code)
    except Exception as e:
        print("Request failed:", e)


def get_folders_ms():
    url = "https://api.clickup.com/api/v2/space//folder"

    try:
        response = requests.get(url, headers=HEADERS)
        if response.status_code == 200:
            print("Success:", response.json())
            data = json.dumps(response.json(), indent=2)
            response_label.config(text=f"Success: {data}")
        else:
            print("Error:", response.status_code)
            response_label.config(text=f"Error: {response.status_code}")
    except Exception as e:
        print("Request failed:", e)

def quit_app():
    print("Closing App..")
    window.destroy()

def reset_response_label():
    print("Clearing Information..")
    response_label.config(text="")


# Buttons
button = Button(window, text='Get User', command=get_user)
button.grid(row=1, column=0, padx=20, pady=10, sticky="w")

team_button = Button(window, text='Get Team', command=get_team)
team_button.grid(row=1, column=0, padx=20, pady=10, sticky="w")

reset_button = Button(window, text='Reset', command=reset_response_label)
reset_button.grid(row=2, column=0, padx=20, pady=10, sticky="w")

quit_button = Button(window, text='Close', command=quit_app)
quit_button.grid(row=3, column=0, padx=20, pady=10, sticky="w")



window.mainloop()
