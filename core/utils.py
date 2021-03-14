import shutil
import time, random
import subprocess, os
import webbrowser, shlex
from collections import namedtuple
from termcolor import colored, cprint

base = os.path.dirname(os.path.realpath(__file__))
response = namedtuple("Response", "status increments kwargs")


def slow(t, *args, speed=130, end="\n", **kwargs):
    for l in range(len(t)):
        cprint(t[l], *args, **kwargs, end="", flush=True)
        time.sleep(5.0 / speed)
    print(end=end)
    time.sleep(0.7)


def run(cmd: str):
    cmd = shlex.split(cmd)
    return subprocess.run(cmd, stdout=subprocess.PIPE, shell=True).stdout.decode("utf-8")


def show(img, *args, **kwargs):
    with open(f"{base}\\assets\\{img}.txt", "r", encoding="utf-8") as f:
        print(colored(f.read(), *args, **kwargs))
    time.sleep(0.5)


def pic(img):
    webbrowser.open(f"{base}\\assets\\{img}")
    """
    with Image.open() as img:
        img.show()"""

