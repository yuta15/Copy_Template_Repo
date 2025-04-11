import os
import git

from mods.setting import setting
from mods.parameter_model import ParameterModel
from mods.logger import set_logger


def clone_repos(repo_params: ParameterModel):
    """ファイルを作成する関数"""
    logger = set_logger(__name__)
    logger.info("Cloning repositories...")
    for url in repo_params.repository.clone_repositories:
        path = f'{setting.ROOT_DIR}/templates/{url.split("/")[-1].split(".")[0]}'
        git.Repo.clone_from(url, path)
    logger.info(f"Clone completed in {setting.ROOT_DIR}/templates")