#!/usr/bin/env python3

import sys

from mods.setting import Settings
from mods.read_params import read_params
from mods.create_repo import create_repo
from mods.clone_repos import clone_repos
from mods.set_docker_compose import set_docker_compose
from mods.push_files import push_files

def main():
    """main function"""
    
    PARAMS = read_params()
    created_repo = create_repo(PARAMS)
    clone_repos(PARAMS)
    set_docker_compose(PARAMS)
    push_files(create_repo)
