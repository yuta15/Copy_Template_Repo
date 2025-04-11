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
        os.chdir(setting.ROOT_DIR+"/templates")
        repository = git.Repo.init(f'{setting.ROOT_DIR}/templates')
        remote = repository.create_remote(name="origin", url=repo.html_url)
        index = repository.index
        remote.pull('main')
        logger.info(repository.branches)
        index.add(["."])
        index.commit("Add files")
        remote.push('master')
    except Exception as e:
        logger.error(f"Push failed: {e}")
        raise
    else:
        logger.info("Push completed")