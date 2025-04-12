#!/usr/bin/env python3

import sys
import os

from mods.setting import setting
from mods.read_params import read_params
from mods.create_repo import create_repo
from mods.clone_repos import clone_repos
from mods.set_docker_compose import set_docker_compose
from mods.push_files import push_files
from mods.logger import set_logger
from mods.init_repo import init_repo

def main():
    """main function"""
    logger = set_logger(__name__)
    PARAMS = read_params()
    repo = create_repo(PARAMS)
    init_repo(repo)
    clone_repos(PARAMS)
    logger.info(f'{os.listdir(f"{setting.ROOT_DIR}/templates")}')
    set_docker_compose(PARAMS)
    push_files()


if __name__ == "__main__":
    main()