import git
import git.repo
import os
from mods.logger import set_logger
from mods.setting import setting

def push_files(repo):
    """templates内のファイルをpushする関数"""
    logger = set_logger(__name__)
    logger.info("Push started")
    
    repository = git.Repo(path=setting.ROOT_DIR+"/templates")
    remote = repository.create_remote(name="origin", url=repo.html_url)
    index = repository.index
    os.chdir(setting.ROOT_DIR+"/templates")
    index.add()
    remote.push('main')
    git.Repo.commit("Add files")
    git.Repo.create_remote(name="origin", url=repo.html_url)