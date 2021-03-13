import shutil
import time,random
import subprocess,os,pickle
import webbrowser,shlex

base = os.path.dirname(os.path.realpath(__file__))

def slow(t,speed=130,end='\n'):
    for l in range(len(t)):
        print(t[l],end='',flush=True)
        time.sleep(5.0/speed)
    print(end=end)
    time.sleep(0.7)

def run(cmd:str):
    cmd =  shlex.split(cmd)
    return subprocess.run(cmd, stdout=subprocess.PIPE,shell=True).stdout.decode('utf-8')

def load():
    if os.path.isfile('user'):
        with open('user','rb') as f:
            user = pickle.load(f)
    else:
        user = [1,None]
        with open('user','wb') as f:
            pickle.dump(user,f)
    return user

def update(index,data):
    user[index] = data
    with open('user','wb') as f:
        pickle.dump(user,f)

def show(img):
    with open(f"{base}\\assets\\{img}.txt",'r') as f:
        print(f.read())
    time.sleep(0.5)

def pic(img):
    webbrowser.open(f"{base}\\assets\\{img}")
    '''
    with Image.open() as img:
        img.show()'''

user = load()