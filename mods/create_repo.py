

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
        # リポジトリの重複チェック
        repos = user.get_repos()
        if not repo_params.repository.repository_name in [repo.name for repo in repos]:
            repo = user.create_repo(
                name=repo_params.repository.repository_name,
                private=False,
                description=repo_params.repository.repository_name,
                auto_init=True,
            )
        else:
            logger.info(f"Repository {repo_params.repository.repository_name} already exists.")
            for repo in repos:
                if repo.name == repo_params.repository.repository_name:
                    repo = repo
                    break

    except GithubException as e:
        logger.error(f"Failed to create repository: {e}")
        sys.exit(1)
    else:
        logger.info(f"Repository created: {repo.html_url}")
        return repo