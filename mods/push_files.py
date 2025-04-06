import git
import git.repo
from mods.logger import set_logger
from mods.setting import setting

def push_files(create_repo):
    """templates内のファイルをpushする関数"""
    logger = set_logger(__name__)
    logger.info("Push started")
    
    
    repo = git.Repo(path=setting.ROOT_DIR+"/templates")
    origin = repo.create_remote(name="origin", url=create_repo.html_url)
    index = repo.index
    origin.fetch()
    repo.merge_base()
    index.add()
    origin.push()
    
    git.Repo.commit("Add files")
    git.Repo.create_remote(name="origin", url=create_repo.html_url)