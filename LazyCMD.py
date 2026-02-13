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
║ 2) Exit               ║
╚═══════════════════════╝
"""
    )


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


def get_choice():
    choice = input("→ Choose an option: ").strip()
    return choice


def main():
    while True:
        os.system("cls")
        open_menu()

        choice = get_choice()

        if choice == "1":
            open_firefox()
        elif choice == "2":
            break
        else:
            print("\nInvalid choice.")
            input("Press Enter to continue...")


if __name__ == "__main__":
    main()
