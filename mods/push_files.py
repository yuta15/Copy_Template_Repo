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
        remote_repo_url = f'https://{setting.PERSONAL_TOKEN}@github.com/{setting.USERNAME}/{repo.name}.git'
        os.chdir(setting.ROOT_DIR+"/templates")
        
        logger.info('Initializing repository...')
        repository = git.Repo.init()
        
        logger.info('create remote...')
        remote = repository.create_remote(name="origin", url=remote_repo_url)
        index = repository.index
        
        act_branch = repository.active_branch.name
        logger.info(f"Active branch: {act_branch}")
        
        logger.info('pulling...')
        remote.pull('main')
        
        logger.info('Checking if branch exists...')
        exec_cmd('git branch -a')
        exec_cmd('git log')
        exec_cmd('git status')
        
        
        logger.info('check out to main branch...')
        exec_cmd('git checkout -b main')
        

        logger.info('Adding files...')
        index.add("*")
        
        logger.info('committing...')
        index.commit("Add files")
        
        logger.info('pushing...')
        remote.push(act_branch)
        
    except Exception as e:
        logger.error(f"Push failed: {e}")
        raise
    
    else:
        logger.info("Push completed")
        
        
def exec_cmd(cmd):
    """コマンドを実行する関数"""
    logger = set_logger(__name__)
    logger.info(f"Executing command: {cmd}")
    
    try:
        logger.info(os.system(cmd))
    except Exception as e:
        logger.error(f"Command execution failed: {e}")
        raise
    else:
        logger.info("Command executed successfully")