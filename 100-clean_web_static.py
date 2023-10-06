#!/usr/bin/python3
from fabric.api import env, run, local
import os

env.hosts = ['<IP web-01>', '<IP web-02>']

def do_clean(number=0):
    """
    Deletes unnecessary archives in the versions and /data/web_static/releases folders
    """
    number = int(number)
    if number < 1:
        number = 1

    try:
        local("ls -1t versions/ | tail -n +{} | xargs -I {{}} rm versions/{{}}".format(number + 1))
    except:
        pass

    with cd("/data/web_static/releases/"):
        run("ls -1t | tail -n +{} | xargs -I {{}} rm -rf releases/{{}}".format(number + 1))
