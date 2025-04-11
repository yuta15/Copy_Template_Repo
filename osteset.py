import os
from mods.logger import set_logger

logger = set_logger(__name__)

logger.info(os.system('git branch -a'))