import sys,os,subprocess
from shutil import which
import time,random,pickle
import utils
from utils import slow
import first
os.system('cls')
with open('assets/intro.txt','r',encoding="utf-8") as f:
    print(f.read())

if which("git") is not None:
    print(utils.run(['git', '--version']))
else:
    print("Git not found! Kindly install before starting the game")
    exit()

levels =(
        "The Beginning",#Setting up/init Repo, setting up credentials and committing
        "The Remote Gateway",#pushing remote and push,pull
        "The Parallel Universes" #branching,merging,resolve conflicts
        )
slow("Welcome to the git world, Start/Continue your git adventures!\n",160)
user = utils.load()

for i in range(user[0]):
    slow(f'{i+1}.'+levels[i])
[print(f'{i+1}.LOCKED') for i in range(user[0],3)]

options = {1:first}
while True:
    choice = int(input('>'))
    if choice <= len(options):
        os.system('cls')
        options[choice].main()
    else:
        slow("Invalid Option, Try again")
