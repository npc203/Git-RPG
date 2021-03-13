from utils import slow
import utils
from tkinter import filedialog,Tk
import os,sys
import time


sys.stderr = open('./err.txt', 'w')

root = Tk()
root.withdraw()

def main():
    #Making the location for the repo
    if utils.user[1] == None:
        while True:
            slow("Create a new folder to make your repository:\n")
            path = filedialog.askdirectory(parent=root, initialdir= os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop') , title='Please select a directory')
            if len(path) > 0:
                if len(os.listdir(path)) == 0: 
                    slow("Your Directory is set to "+path+'\n',100)
                    utils.update(1,path)
                    time.sleep(2)
                    break
                else:
                    print("The current directory isn't empty, please select an empty directory for safety")
    else:
        path = utils.user[1] 
        
    os.chdir(path)
    slow("Welcome Traveller, type cd to print the current working directory\n")
    stack = {"cd":0,'git init':0,'status':0,'commit':0}
    while True:
        inp = input('>')
        out = utils.run(inp)
        print("\n>>> "+out)
        if inp == 'cd' and not stack["cd"]:
            slow("Nice,Now we are set, Let's start by making a repository.\nTip:type git init")
            stack["cd"]=1 
        elif 'git init' in inp and not stack["git init"]:
            with open("main.txt",'w') as f:
                f.write("this is some random text file that should contain some code")
            with open("password.txt",'w') as f:
                f.write("Confidential base64 password!!:TXkgYm9pIHRobyBiZSBqb2JsZXNzbHkgdHJ5aW5nIHRvIGRlY29kZSBzdHVmZiwgZ2V0IGJhY2sgbG9s")
            utils.run("mkdir somefolder")
            slow(f"So we made a repository locally. I've added few stuff in the folder\nyou can check it by opening {path} in explorer")
            print("Tip: You can add more files\n")
            slow("Let's check the status of the repo by typing: git status ...")
            stack["git init"]=1
        
        elif 'git status' in inp and not stack["status"]:
            input("Press Enter to continue...")
            slow("That's Your git status, feel free to use it anytime")
            slow("you might notice that empty folder is not displayed\ncause its pointless to commit them")
            input("Press Enter to continue...")
            os.system('cls')
            utils.show("turtle")
            slow("OwO..The master turtle has decided to travel with you!LET'S GO!")
            slow("Congrats you made a repository!,That was simple lol.\n")
            input("Press Enter to continue...")
            slow("By Default the git repo is empty, Let's commit the changes we've made!")
            slow("""    A commit is a record of what files you have changed since the last time you made a commit.
    git tracks these changes and you can revert back anytime.""",90)
            input("Press Enter to continue...")
            slow("Now commit the changes by typing : git commit -m \"This is my first commit\" ")
            slow("Note: the -m is for message, all commits must have a relavant message")
            stack["status"]=1

        elif 'git commit' in inp and not stack["commit"]:
            if "nothing added to commit" in out:
                slow("Oopsie!  You need to stage your changes.. WHaaaa")
                input("Press enter to continue..")
                os.system('cls')
                slow("Git uses something called staging files before you commit SIKE!( ͡° ͜ʖ ͡°)")
                time.sleep(0.3)
                slow("First Your changes must be staged before committing")
                utils.pic("stage.png")
                input("Press Enter to continue...")
                slow('To Stage your commits use : git add <files..>')
                slow('To stage everything do : git add .')
            else:
                slow("Sweet! you learnt how to commit changes!")
                slow("Now you can make changes and commit as much as u want!")
                input('Press Enter to Continue..')
                stack["commit"]=1
                slow()
        elif 'git add' in inp:
            slow("Alrighty Now That you've successfully Staged the Changes you can commit them now!")
            slow("")

        elif 'exit' in inp:
            slow('>>>All your unsaved progress will be lost, Do you want to quit?(y/n)')
            prompt = input('>').lower()
            if prompt in ('y','yes'):
                exit()
            print()





if __name__ == "__main__":
    main()