#!/usr/bin/python3
'''File containing the do_pack, do_deploy and deploy functions'''

from fabric.api import *
from datetime import datetime
from os import path

env.hosts = ['34.75.147.95', '104.196.199.220']


def do_pack():
    '''Generates a .tgz archive from the contents of the web_static folder'''
    if path.isdir("versions") is False:
        local("mkdir versions")
    time = datetime.now().strftime("%Y%m%d%H%M%S")
    archive_name = "versions/web_static_{}.tgz".format(time)
    generate = local("tar -cvzf {} web_static".format(archive_name))
    if generate.succeeded:
        return archive_name
    else:
        return None


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


def deploy():
    '''Creates and distributes an archive to my web servers'''
    path_pack = do_pack()
    if path_pack is None:
        return False
    path_deploy = do_deploy(path_pack)
    return path_deploy
