from .. import Level, info
from ..utils import slow, run, show, response, base
import os, time


class start(Level):
    progress = 1

    def __lt__(self, other):
        return self.progress < other.progress

    @info(name="cd")
    def cd(out):
        slow(
            "Nice,Now we are set, Let's start by making a repository.\nTip:type git init", "cyan",
        )
        return 1

    @info(name="git init")
    def init(out):
        path = os.getcwd()
        with open("main.txt", "w") as f:
            f.write("this is some random text file that should contain some code")
        with open("password.txt", "w") as f:
            f.write(
                "Confidential base64 password!!:TXkgYm9pIHRobyBiZSBqb2JsZXNzbHkgdHJ5aW5nIHRvIGRlY29kZSBzdHVmZiwgZ2V0IGJhY2sgbG9s"
            )
        run("mkdir somefolder")
        slow(
            f"\nSo we made a repository locally. I've added few stuff in the folder\nyou can check it by opening {path} in explorer",
            "green",
        )
        print("Tip: You can add more files\n")
        slow(f"Open {path} folder and have a look at the files and come back", "yellow")
        input("Press Enter to continue...")
        os.system("cls")
        slow("Let's check the status of the repo by typing: git status ...")
        return 1

    @info(name="git status")
    def status(out):
        input("Press Enter to continue...")
        slow("That's Your git status, feel free to use it anytime", "cyan")
        slow(
            "you might notice that empty folder is not displayed\ncause its pointless to commit them",
            "cyan",
        )
        input("Press Enter to continue...")
        os.system("cls")
        show("turtle", "green")
        slow("OwO..The master turtle has decided to travel with you!LET'S GO!")
        slow("Congrats you made a repository!,That was simple lol.\n", "yellow")
        input("Press Enter to continue...")
        slow("By Default the git repo is empty, Let's commit the changes we've made!", "cyan")
        slow(
            "A commit is a record of what files you have changed since the last time you made a commit.\n"
            "Git tracks these changes and you can revert back anytime.",
            "yellow",
            speed=90,
        )
        input("Press Enter to continue...")
        slow('Now commit the changes by typing : git commit -m "This is my first commit" ')
        slow("Note: the -m is for message, all commits must have a relavant message")
        return 1

    @info(name="git commit")
    def commit(out):
        if "nothing added to commit" in out:
            slow("Oopsie!  You need to stage your changes.. WHaaaa", "yellow")
            input("Press enter to continue..")
            os.system("cls")
            slow(
                "Git uses something called staging files before you commit SIKE!( ͡° ͜ʖ ͡°)",
                "cyan",
            )
            time.sleep(0.3)
            slow("First Your changes must be staged before committing\n", "cyan")
            show("stage")
            print()
            input("Press Enter to continue...")
            slow("To Stage your commits use : git add <files..>")
            slow("To stage everything do : git add .")
            return 0
        else:
            slow("Sweet! you learnt how to commit changes!", "cyan")
            slow("Now you can make changes and commit as much as u want!", "cyan")
            input("Press Enter to continue..")
            return 1

    @info(name="git add")
    def stage(out):
        slow(
            "Alrighty Now That you've successfully Staged the Changes you can commit them now!",
            "cyan",
        )
        return 1
