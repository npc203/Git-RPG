from tkinter import filedialog, Tk
import os, sys
import time
from user import User
import core
from core.utils import slow

sys.stderr = open("./err.txt", "w")

root = Tk()
root.withdraw()
user = User()


def setup():
    """Sets up the folder for the test repo"""
    path = user.get("path")
    if not path:
        while True:
            slow("Create a new folder to make your repository:\n")
            path = filedialog.askdirectory(
                parent=root,
                initialdir=os.path.join(os.path.join(os.environ["USERPROFILE"]), "Desktop"),
                title="Please select a directory",
            )
            if len(path) > 0:
                if len(os.listdir(path)) == 0:
                    slow("Your Directory is set to " + path + "\n", 100)
                    user.update({"path": path})
                    time.sleep(2)
                    break
                else:
                    print(
                        "The current directory isn't empty, please select an empty directory for safety"
                    )
    return path


def main():
    path = setup()
    os.chdir(path)
    game = core.manager(*user.get("level, sublevel"))
    game.start()
    slow(
        "Welcome Traveller, I've changed the directory for you ,type cd to print the current working directory\n"
    )
    while True:
        game.step()


if __name__ == "__main__":
    main()


"""
def find_inp(text):
    for i in range(len(lvl)):
        for j in range(len(lvl[i])):
            if text == lvl[i][j]:
                return i, j
"""
