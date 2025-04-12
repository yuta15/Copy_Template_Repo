import git
import os
import sys

import git.exc

from mods.logger import set_logger
from mods.setting import setting
from mods.exec_cmd import exec_cmd


def init_repo(repo):
    """Initialize a Git repository and set up a remote origin."""
    logger = set_logger(__name__)
    logger.info("Initializing repository...")
    
    # templatesディレクトリが存在しない場合のみ作成
    if not os.path.exists(f'{setting.ROOT_DIR}/templates'):
        logger.info(f"Creating templates directory")
        os.mkdir(f'{setting.ROOT_DIR}/templates')

    # templatesディレクトリに移動
    os.chdir(f'{setting.ROOT_DIR}/templates')
    logger.info(f"Current working directory: {os.getcwd()}")

    try:
        # git init 実行
        repository = git.Repo.init()
        # git remote add origin <url> 実行
        repository.create_remote(
            name="origin", 
            url=f'https://{setting.PERSONAL_TOKEN}@github.com/{setting.USERNAME}/{repo.name}.git'
            )
        # usernameを設定
        # これをしないとcommit時のAuthorがrootとなり"fatal: detected dubious ownership in repository"エラーが発生する
        exec_cmd(f'git config user.name {setting.USERNAME}')
        # mainブランチに合わせる。初期ブランチがmasterとなることがあった為。
        # すでに存在する場合はエラーになるが、WF事態は停止しない為問題なし。
        logger.info(f"Active branch: {repository.active_branch.name}")
        exec_cmd('git checkout -b main')
        # git config -lを実行して、設定を確認
        # user.nameが設定されていることを確認
        # remote.origin.urlが設定されていることを確認
        logger.info('Cuurent config')
        exec_cmd('git config -l')
    except (
        git.exc.GitCommandError, 
        git.exc.InvalidGitRepositoryError, 
        git.exc.RepositoryDirtyError, 
        git.exc.CheckoutError
        ) as e:
        logger.error(f"Git operation failed:{e}")
        sys.exit(1)
    except Exception as e:
        logger.error(f"Failed to initialize repository: {e}")
        sys.exit(1)
    else:
        logger.info(f"Repository initialized")
