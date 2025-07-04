from tkinter import *
import requests
import json
import time

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

def get_request(url):
    try:
        response = requests.get(url, headers=HEADERS)
        if response.status_code == 200:
            data = json.dumps(response.json(), indent=2)
            print("Success:", data)
            response_label.config(text=f"Success: {data}")
        else:
            print("Error:", response.status_code)
            response_label.config(text=f"Error: {response.status_code}")
    except Exception as e:
        print("Request failed:", e)

# TODO: fix function, returning error 400
def get_timesheet():
    team_id = "9012212996"
    user_id = "88662239"
    # Get timestamps for last 7 days
    end = int(time.time() * 1000)
    start = end - 7 * 24 * 60 * 60 * 1000
    url = "https://api.clickup.com/api/v2/team/{team_id}/time_entries?start={start}&end={end}&assignee={user_id}"

    try:
        response = requests.get(url, headers=HEADERS)
        if response.status_code == 200:
            data = json.dumps(response.json(), indent=2)
            print("Success:", data)
            for entry in data.get("data", []):
                print("Task:", entry.get("task", {}).get("name", "Unknown"))
                print("Duration (ms):", entry["duration"])
                print("Start:", entry["start"])
                print("------")
        else:
            print("Error:", response.status_code)
            response_label.config(text=f"Error: {response.status_code}")
    except Exception as e:
        print("Request failed:", e)



def get_user():
    url = "https://api.clickup.com/api/v2/user"
    get_request(url)


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

def get_space():
    url = "https://api.clickup.com/api/v2/team/9012212996/space"
    try:
        response = requests.get(url, headers=HEADERS)
        if response.status_code == 200:
            for space in response.json()["spaces"]:
                print("Space:", space["name"], "ID:", space["id"])
        else:
            print("Error:", response.status_code)
            response_label.config(text=f"Error: {response.status_code}")
    except Exception as e:
        print("Request failed:", e)

def get_folder():
    url = "https://api.clickup.com/api/v2/space/90121093695/folder"
    try:
        response = requests.get(url, headers=HEADERS)
        if response.status_code == 200:
            print("Success:", response.json())
        else:
            print("Error:", response.status_code)
            response_label.config(text=f"Error: {response.status_code}")
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
user_button = Button(window, text='Get User', command=get_user)
user_button.grid(row=1, column=0, padx=20, pady=10, sticky="w")

debug_button = Button(window, text='Debug', command=get_folder)
debug_button.grid(row=2, column=0, padx=20, pady=10, sticky="w")

timesheet_button = Button(window, text='Get Timesheet', command=get_timesheet)
timesheet_button.grid(row=3, column=0, padx=20, pady=10, sticky="w")

reset_button = Button(window, text='Reset', command=reset_response_label)
reset_button.grid(row=4, column=0, padx=20, pady=10, sticky="w")

quit_button = Button(window, text='Close', command=quit_app)
quit_button.grid(row=5, column=0, padx=20, pady=10, sticky="w")



window.mainloop()
