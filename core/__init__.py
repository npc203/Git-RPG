from .data import level_list
import os
from .utils import run, slow, show
from importlib import import_module
from inspect import isclass
from pkgutil import iter_modules
from types import FunctionType


class Level(type):
    pass


class manager:
    def __init__(self, lvl, sublvl, user):
        self.user = user
        self.lvl = lvl
        self.sublvl = sublvl
        self.lvlnames = None
        self.stack = None
        temp_list = []
        # This auto populates the trans with the levels present in level folder
        pkg_dir = os.path.join(os.path.dirname(__file__), "levels")
        for (module_loader, name, ispkg) in iter_modules([pkg_dir]):
            theme_module = import_module(f"{__name__}.levels.{name}")
            for attribute in dir(theme_module):
                attr = getattr(theme_module, attribute)
                if isclass(attr) and issubclass(attr, Level) and attr is not Level:
                    temp_list.append(attr)
        self.trans = sorted(temp_list)

    def start(self):
        self.repopulate(self.lvl - 1)
        show("intro", "green")
        tmp = tuple(level_list.keys())
        for ind in range(len(tmp)):
            print(f" {ind + 1} ." if ind < self.lvl else " \N{LOCK}", tmp[ind])
        while True:
            choice = int(input("\nSelect Level: "))
            if self.lvl <= choice:
                self.lvl = choice
                break
            else:
                print("You need to complete the previous levels")

    def repopulate(self, lvl):
        self.lvlnames = []
        self.stack = []
        for key, val in self.trans[lvl].__dict__.items():
            if hasattr(val, "decorator"):
                self.lvlnames.append(val)
                self.stack.append(0)

    def step(self):
        if not self.check_lvl_completion():
            inp = input(">")
            if "exit" in inp:
                slow(">>>All your unsaved progress will be lost, Do you want to quit?(y/n)")
                prompt = input(">").lower()
                if prompt in ("y", "yes"):
                    exit()
            else:
                out = run(inp)
                print("\n>>> " + out)
                return self.designate(inp, out)
        else:
            self.lvl += 1
            self.user.update("level", self.lvl)

    def designate(self, inp, out):
        for ind in range(len(self.lvlnames)):
            if inp.startswith(self.lvlnames[ind].name):
                if self.stack[ind] != 1:
                    self.stack[ind] = self.lvlnames[ind](out)
                    break
                break

    def check_lvl_completion(self):
        return all(self.stack)


def info(**kwargs):
    def inner(func):
        setattr(func, "decorator", "info")
        for thing in kwargs:
            setattr(func, thing, kwargs[thing])
        return func

    return inner

