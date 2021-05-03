#!/usr/bin/python3
'''File containing the do_deploy function'''
from fabric.api import *
from os import path

env.hosts = ['34.75.147.95', '104.196.199.220']


def do_deploy(archive_path):
    '''Distributes an archive to my web servers'''
    if path.exists(archive_path) is False:
        return False
    try:
        name = archive_path.split("/")[1]
        no_extension = name.split(".")[0]
        path_r = "/data/web_static/releases/"
        path_c = "/data/web_static/current"
        put(archive_path, "/tmp/")
        run("mkdir -p {}{}/".format(path_r, no_extension))
        run("tar -xzf /tmp/{} -C {}{}/".format(name, path_r, no_extension))
        run("rm /tmp/{}".format(name))
        run("mv {0}{1}/web_static/* {0}{1}/".format(path_r, no_extension))
        run("rm -rf {}{}/web_static".format(path_r, no_extension))
        run("rm -rf {}".format(path_c))
        run("ln -sf {}{}/ {}".format(path_r, no_extension, path_c))
        return True
    except:
        return False
