import git
import os
from mods.logger import set_logger
from mods.setting import setting


def push_files(repo):
    """templates内のファイルをpushする関数"""
    logger = set_logger(__name__)
    logger.info("Push started")
    
    try:
        # リポジトリ変更
        remote_repo_url = f'https://github.com/{setting.USERNAME}:{setting.GITHUB_TOKEN}/{repo.name}.git'
        os.chdir(setting.ROOT_DIR+"/templates")
        repository = git.Repo.init(f'{setting.ROOT_DIR}/templates')
        remote = repository.create_remote(name="origin", url=remote_repo_url)
        index = repository.index
        
        remote.pull('main')
        logger.info(repository.branches)
        act_branch = repository.active_branch.name
        logger.info(f"Active branch: {act_branch}")
        index.add(["."])
        index.commit("Add files")
        remote.push('master')
    except Exception as e:
        logger.error(f"Push failed: {e}")
        raise
    else:
        logger.info("Push completed")