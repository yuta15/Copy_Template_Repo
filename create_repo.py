from github import Github
import os
import json
import ipaddress
import sys
import logging



# 環境変数/グローバル変数の読み込み
GITHUB_TOKEN = os.environ.get('GITHUB_TOKEN')
CURRENT_PATH = os.getcwd()

# 設定値の読み込み
with open(file=CURRENT_PATH+'/'+'params.json') as f:
    INPUT_PARAMS = json.loads(f.read())


def validate_params():
    """REPOSITORY_PARAMSの値チェック"""
    rep_params = INPUT_PARAMS.get('repository_params', None)
    app_container_params = INPUT_PARAMS.get('app_container', None)
    db_container_params = INPUT_PARAMS.get('db_container', None)
    
    def _validate_repository_params(rep_prams):
        """REPOSITORY_PARAMSのvalidation関数"""
        name = rep_prams.get('repository_name', None)
        branches = rep_prams.get('branches', None)
        if name == None or branches is None:
            logging.error('repository_params is require parameters in params.json')
            sys.exit()
        elif name == "":
            logging.error('repository_name is require parameters in params.json')
            sys.exit()
        elif branches == []:
            branches.append('main')

    def _validate_app_contaienr_params(app_container_params):
        """APP_CONTAINER_PARAMSのvalidation関数"""
        export_port = app_container_params.get('export_port', None)
        app_container_ip = app_container_params.get('container_ip', None)
        if export_port is None or app_container_ip is None:
            logging.error('app_container.export_port or app_container.app_container_ip is required')
        try:
            ipaddress.ip_interface(app_container_ip+'/24')
        except ValueError:
            sys.exit()

        if export_port < 0 or export_port > 65535:
            logging.error('export_port is 0 - 65535')
            sys.exit()

    def _validate_DB_CONTAINER_PARAMS(db_container_params):
        """DB_CONTAINER_PARAMSのvalidation関数"""
        export_port = db_container_params.get('export_port', None)
        db_container_ip = db_container_params.get('container_ip', None)
        
        if export_port is None or db_container_ip is None:
            logging.error('db_container.export_port or db_container.db_container_ip is required')
        try:
            ipaddress.ip_interaface(db_container_ip+'/24')
        except ValueError:
            sys.exit()
        if export_port < 0 or export_port > 65535:
            logging.error('export_port is 0 - 65535')
            sys.exit()

    _validate_repository_params(rep_params)
    _validate_app_contaienr_params(app_container_params)
    _validate_app_contaienr_params(db_container_params)


def create_repo():
    """リポジトリを作成する関数"""
    pass


def create_dirs():
    """追加するdirectoryを作成する"""
    pass


def create_branch():
    """リポジトリに既定のブランチを作成する"""
    pass


def set_branch_rule():
    """リポジトリのルールを設定する"""
    pass





if __name__ == '__main__':
    validate_params()
    create_repo()
    create_dirs()
    create_branch()
    set_branch_rule()