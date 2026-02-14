import subprocess
import os
from urllib.parse import quote_plus


# ---- Main Menu ----
def open_menu():
    print(
        """
╔═══════════════════════╗
║        LazyCMD        ║
╠═══════════════════════╣
║ 1) Open Firefox       ║
║ 2) Downloader         ║
║ E) Exit               ║
╚═══════════════════════╝
"""
    )


def get_choice():
    choice = input("→ Choose an option: ").strip()
    return choice


# ---- Firefox ----
domains = [".com", "cn", ".de", ".net", ".org", ".uk", ".ru", "nl", ".br", ".au"]


def open_firefox():
    os.system("cls")
    link = input("Enter a link: ")
    # Endcoding the link to url (for example "+" -> "%2B")
    encoded_link = quote_plus(link)
    if not any(end in link for end in domains):
        link = f"www.google.com/search?q={encoded_link}"
    try:
        subprocess.Popen(f"start firefox {link}", shell=True)
    except Exception as error:
        print("An error occurred while trying to open Firefox:", error)
    os.system("cls")
    input("Press Enter to continue...")


# ---- Downloads ----
def open_downloads():
    print(
        """
╔═══════════════════════╗
║        LazyCMD        ║
╠═══════════════════════╣
║ 1) Open Firefox       ║
║ 2) Downloader         ║
║ E) Exit               ║
╚═══════════════════════╝
"""
    )


def downloads():
    os.system


# ---- Main script ----
def main():
    while True:
        os.system("cls")
        open_menu()

        choice = get_choice()

        if choice == "1":
            open_firefox()
        elif choice == "2":
            downloads()
        elif choice == "E" or choice == "e" or choice == "exit" or choice == "Exit":
            break
        else:
            print("\nInvalid choice.")
            input("Press Enter to continue...")


if __name__ == "__main__":
    main()
