import os
import git
import shutil

from mods.setting import setting
from mods.parameter_model import ParameterModel
from mods.logger import set_logger


def clone_repos(repo_params: ParameterModel):
    """ファイルを作成する関数"""
    logger = set_logger(__name__)
    logger.info("Cloning repositories...")
    for url in repo_params.repository.clone_repositories:
        dir_name = url.split("/")[-1].split(".")[0]
        path = f'{setting.ROOT_DIR}/templates/{dir_name}'
        git.Repo.clone_from(url, path)
        os.chdir(f'{setting.ROOT_DIR}/templates/{dir_name}')
        shutil.rmtree(f'{dir_name}/.git')
    logger.info(f"Clone completed in {setting.ROOT_DIR}/templates")