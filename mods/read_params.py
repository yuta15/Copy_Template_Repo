import json
import sys

from mods.parameter_model import ParameterModel
from mods.logger import set_logger
from mods.setting import setting


def read_params()->ParameterModel:
    """
    params.jsonを読み込む関数
    model_validationを使用し、読み込んだJsonを検証する。
    Args:
        None
    Returns:
        ParameterModel: 検証済みのパラメータモデル
    """
    logger = set_logger(__name__)
    logger.info("Reading parameters...")
    
    try: 
        with open(setting.PARAMETER_FILE, 'r') as f:
            params = json.load(f)
        logger.info(f'Params loaded by: {params}')
    except FileNotFoundError as f:
        logger.error(f'parameter.json file not found {e}')
        sys.exit(1)
    except ValueError as e:
        logger.error(f'Invalid JSON format in parameter.json {e}')
        sys.exit(1)
    else:
        return ParameterModel.model_validate(params)