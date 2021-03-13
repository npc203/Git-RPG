import utils,os,re
import shlex
cmd = 'git commit -m \'owo this is a string\''
pattern = r"([\"'])(.*?[^\\])\1"
obj = re.search(pattern,cmd)

if obj:
    print(re.sub(pattern,'', cmd))
    #cmd = cmd.split()
    print(cmd[obj.start():obj.end()])
else:
    print(obj)
#utils.pic('stage.png')

