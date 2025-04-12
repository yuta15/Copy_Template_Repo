import git
import os

from mods.logger import set_logger
from mods.setting import setting
from mods.exec_cmd import exec_cmd

def init_repo(repo):
    """Initialize a Git repository and set up a remote origin."""
    logger = set_logger(__name__)
    logger.info("Initializing repository...")
    
    try:
        # create the templates directory if it doesn't exist
        if not os.path.exists(f'{setting.ROOT_DIR}/templates'):
            logger.info(f"Creating templates directory")
            os.mkdir(f'{setting.ROOT_DIR}/templates')

        # Initialize the repository
        os.chdir(f'{setting.ROOT_DIR}/templates')
        logger.info(f"Current working directory: {os.getcwd()}")
        repository = git.Repo.init()
        
        # Remote repository setup
        repository.create_remote(
            name="origin", 
            url=f'https://{setting.PERSONAL_TOKEN}@github.com/{setting.USERNAME}/{repo.name}.git'
            )
        
        # Checkout to the main branch
        exec_cmd('git checkout -b main')
        logger.info(f"Active branch: {repository.active_branch.name}")

        logger.info('Cuurent config')
        exec_cmd('git config -l')
        
    
    except Exception as e:
        logger.error(f"Failed to initialize repository: {e}")
        raise
    else:
        logger.info(f"Repository initialized")
