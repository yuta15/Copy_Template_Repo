

from github import Github
from github.GithubException import GithubException
import sys

from mods.setting import setting
from mods.parameter_model import ParameterModel
from mods.logger import set_logger


def create_repo(repo_params: ParameterModel):
    """リポジトリを作成する関数"""
    logger = set_logger(__name__)
    logger.info("Creating repository...")
    
    g = Github(setting.GITHUB_TOKEN)
    user = g.get_user()
    try:
        repo = user.create_repo(
            name=repo_params.repository.repository_name,
            private=False,
            description=repo_params.repository.repository_name,
            auto_init=True,
        )
    except GithubException as e:
        logger.error(f"Failed to create repository: {e}")
        sys.exit(1)
    else:
        logger.info(f"Repository created: {repo.html_url}")
        return repo