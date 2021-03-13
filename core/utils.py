import shutil
import time, random
import subprocess, os
import webbrowser, shlex
from collections import namedtuple

base = os.path.dirname(os.path.realpath(__file__))
response = namedtuple("Response", "status increments kwargs")


def slow(t, speed=130, end="\n"):
    for l in range(len(t)):
        print(t[l], end="", flush=True)
        time.sleep(5.0 / 1000)
    print(end=end)
    time.sleep(0.7)


def run(cmd: str):
    cmd = shlex.split(cmd)
    return subprocess.run(cmd, stdout=subprocess.PIPE, shell=True).stdout.decode("utf-8")


def show(img):
    with open(f"{base}\\assets\\{img}.txt", "r") as f:
        print(f.read())
    time.sleep(0.5)


def pic(img):
    webbrowser.open(f"{base}\\assets\\{img}")
    """
    with Image.open() as img:
        img.show()"""

