import git
import os
import sys
import git.exc

from mods.logger import set_logger
from mods.setting import setting
from mods.exec_cmd import exec_cmd


def push_files():
    """templates内のファイルをpushする関数"""
    logger = set_logger(__name__)
    logger.info("Push started")
    try:
        # directory変更
        os.chdir(setting.ROOT_DIR+"/templates")
        # branch設定
        repository = git.Repo()
        index = repository.index
        remote = repository.remote(name="origin")
        logger.info('pulling...')
        remote.pull('main')
        logger.info('Check branch setting...')
        exec_cmd('git branch -a')
        exec_cmd('git log')
        exec_cmd('git status')
        exec_cmd('git config -l')
        act_branch = repository.active_branch.name
        logger.info(f"Active branch: {act_branch}")
        logger.info('Adding files...')
        index.add("*")
        logger.info('committing...')
        index.commit("Add files")
        logger.info('gitlog...')
        exec_cmd('git log')
        logger.info('pushing...')
        exec_cmd('git push origin main:main')
    except (git.exc.GitCommandError) as e:
        logger.error(f"Git command error: {e}")
        sys.exit(1)
    except Exception as e:
        logger.error(f"Push failed: {e}")
        sys.exit(1)
    else:
        logger.info("Push completed")
