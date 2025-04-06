from mods.parameter_model import ParameterModel
import json
from logging import getLogger, StreamHandler, INFO, Formatter
import sys

from mods.setting import setting


def read_params()->ParameterModel:
    """
    Read params from parameter.json file.
    Returns:
        ParameterModel: Parameter model object.
    """
    logger = getLogger(__file__)
    handler = StreamHandler()
    logger.setLevel(INFO)
    handler.setLevel(INFO)
    logger.addHandler(handler)
    handler.setFormatter(Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
    
    try: 
        with open(setting.PARAMETER_FILE, 'r') as f:
            params = json.load(f)
            logger.info(f'Params loaded by: {params}')
            return ParameterModel.model_validate(params)
    except FileNotFoundError as f:
        logger.error(f'parameter.json file not found {e}')
        sys.exit()
    except ValueError as e:
        logger.error(f'Invalid JSON format in parameter.json {e}')
        sys.exit()