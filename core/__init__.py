from .data import level_list as lvl
import os
from .utils import run, slow
from importlib import import_module
from inspect import isclass
from pkgutil import iter_modules


class Level:
    pass


class manager:
    def __init__(self, lvl, sublvl):
        self.lvl = lvl
        self.sublvl = sublvl

    def start(self):
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

    def step(self):
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

    def designate(self, inp, out):
        if self.lvl - 1 >= 0:
            lvl_obj = self.trans[self.lvl - 1]
            lvl_obj


def info(**kwargs):
    def inner(func):
        for thing in kwargs:
            setattr(func, thing, kwargs[thing])
        return func

    return inner

