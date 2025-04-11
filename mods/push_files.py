import git
import os

from mods.logger import set_logger
from mods.setting import setting
from mods.exec_cmd import exec_cmd


def push_files(repo):
    """templates内のファイルをpushする関数"""
    logger = set_logger(__name__)
    logger.info("Push started")
    
    try:
        # リポジトリ変更
        os.chdir(setting.ROOT_DIR+"/templates")
        repository = git.Repo()
        index = repository.index
        remote = repository.remote(name="origin")

        logger.info('pulling...')
        remote.pull('main')
        
        logger.info('Checking if branch exists...')
        exec_cmd('git branch -a')
        exec_cmd('git log')
        exec_cmd('git status')
        
        
        logger.info('check out to main branch...')
        exec_cmd('git checkout -b main')
        
        act_branch = repository.active_branch.name
        logger.info(f"Active branch: {act_branch}")
        
        logger.info('Adding files...')
        index.add("*")
        
        logger.info('committing...')
        index.commit("Add files")
        
        logger.info('pushing...')
        remote.push('remotes/origin/main')
        
    except Exception as e:
        logger.error(f"Push failed: {e}")
        raise
    
    else:
        logger.info("Push completed")
