import yaml
from typing import List

from mods.setting import setting
from mods.parameter_model import ParameterModel, ContainerNetowrkModel, ContainerInterfaceModel
from mods.logger import set_logger


def set_docker_compose(repo_params: ParameterModel):
    """
    docker-compose.ymlをparams.jsonの内容に沿って修正する関数
    """
    logger = set_logger(__name__)
    try:
        logger.info(f'set docker-compose.yml')
        container_params = set_containers_dict(repo_params.containers)
        container_nw = set_nw_to_dict(repo_params.container_nw)
        container_full = container_params | container_nw
        with open(f'{setting.ROOT_DIR}/templates/docker-compose.yml', 'w') as f:
            f.write(yaml.safe_dump(container_full))
    except Exception as e:
        logger.error(f'Error in set_docker_compose: {e}')
        raise e
    else:
        logger.info(f'docker-compose.yml created in {setting.ROOT_DIR}/templates/docker-compose.yml')


def set_containers_dict(container_params: List[ParameterModel]):
    """
    container_paramsをyaml形式に変換する関数
    """
    dict_container_params = {
        'services': {}
    }
    for container in container_params:
        container_nw_params = container_config_to_dict(container.netowrks)
        dict_container_params['services'][container.container_name]={
                'container_name': container.container_name,
                'hostname': container.container_name,
                'image': container.image,
                'restart': 'always',
                'ports': container.ports,
                'volumes': [vol.dict() for vol in container.volumes],
                'working_dir': container.workdir,
                'networks': container_nw_params,
                'command': container.command
            }
    return dict_container_params


def container_config_to_dict(container_nw: List[ContainerInterfaceModel]):
    """
    containerのinterface設定をリスト->dict形式に変換する関数
    """
    if_params = {}
    for nw in container_nw:
        if_params[nw.nw_name] = {
            'ipv4_address': str(nw.ip_address)
        }
    return if_params


def set_nw_to_dict(container_nw: List[ContainerNetowrkModel]):
    """
    container_nwをyaml形式に変換する関数
    """
    dict_nw_params = {
        'networks': {}
    }
    for nw in container_nw:
        dict_nw_params['networks'][nw.nw_name]={
                'ipam': {
                    'driver': nw.driver,
                    'config':[
                        {
                            'subnet': str(nw.subnet)
                        }
                    ]
                }
        }
    return dict_nw_params