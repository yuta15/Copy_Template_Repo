from github import Github, Repository
from github.GithubException import GithubException
import sys

from mods.setting import setting
from mods.parameter_model import ParameterModel
from mods.logger import set_logger
from exception.exception import ExistRepositoryError



def create_repo(repo_params: ParameterModel) -> Repository:
    """
    リポジトリを作成する関数。
    既存のリポジトリを確認し、作成するリポジトリ名が使用されていないことを確認する。
    使用されている場合は異常終了させる。
    
    Args:
        repo_params (ParameterModel): パラメータモデル
    Returns:
        repo (Repository): 作成したリポジトリのオブジェクト
    Exceptions:
        ExistRepositoryError: リポジトリ名の重複エラー
        GithubException: GitHub APIのエラー
        Exception: その他のエラー
    """
    logger = set_logger(__name__)
    logger.info("Creating repository...")
    
    g = Github(setting.PERSONAL_TOKEN)
    user = g.get_user()
    try:
        # リポジトリの重複チェック
        repos = user.get_repos(user)
        fetched_repo_names = [repo.name for repo in repos]
        # リポジトリ名が既存リポジトリ内に存在しないことを確認
        if not repo_params.repository.repository_name in fetched_repo_names:
            # 同じリポジトリ名が存在しない場合の処理
            logger.info(f"{repo_params.repository.repository_name} does not exist. Creating a new repository.")
            repo = user.create_repo(
                name=repo_params.repository.repository_name,
                private=False,
                description=repo_params.repository.repository_name,
                auto_init=True
                )
        else:
            # 同じリポジトリ名が存在する場合はraiseさせる。
            logger.error(f"{repo_params.repository.repository_name} already exists.")
            raise ExistRepositoryError(repo_params.repository.repository_name)
    except GithubException as e:
        # GitHub APIのエラー処理
        logger.error(f"Failed to create repository by Github API Error: {e}")
        sys.exit(1)
    except ExistRepositoryError as e:
        # リポジトリ名の重複エラー処理
        logger.error(f"Duplicate repository name: {e}")
        sys.exit(1)
    except Exception as e:
        # その他のエラー処理
        logger.error(f"Failed to create repository. Reason: {e}")
        sys.exit(1)
    else:
        logger.info(f"Repository created: {repo_params.repository.repository_name}")
        return repo


def fetch_remote_repos(user) -> list:
    """
    リモートリポジトリを取得する関数
    Args:
        user (NamedUser | AuthenticatedUser): GitHubのユーザーオブジェクト
    Returns:
        repos (list): リモートリポジトリのリスト
    Exceptions:
        GithubException: GitHub APIのエラー
    """
    logger = set_logger(__name__)
    logger.info("Fetching remote repositories...")
    
    try:
        # リモートリポジトリのリストを取得
        repos = user.get_repos()
        
    except GithubException as e:
        # GitHub APIのエラー処理
        logger.error(f"Failed to fetch remote repositories: {e}")
        sys.exit(1)
        
    except Exception as e:
        # その他のエラー処理
        logger.error(f"Failed to fetch remote repositories. Reason: {e}")
        sys.exit(1)
        
    else:
        logger.info("Remote repositories fetched successfully.")
        return repos