#!/usr/bin/python3
'''File containing the do_pack function'''
from fabric.api import local
from datetime import datetime
from os import path


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
