import subprocess
import os

domain = [".com", ".de", ".net"]


def open_firefox(link):
    try:
        subprocess.Popen(f"start firefox {link}", shell=True)
    except Exception as error:
        print("An error occurred while trying to open Firefox:", error)


while True:
    os.system("cls")
    link = input("What website do you want to visit?: ").strip()

    if not any(end in link for end in domain):
        link = f"www.google.com/search?q={link}"

    open_firefox(link)
    break
