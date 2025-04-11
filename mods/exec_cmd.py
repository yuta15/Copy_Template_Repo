from mods.logger import set_logger
import os


def exec_cmd(cmd):
    """コマンドを実行する関数"""
    logger = set_logger(__name__)
    logger.info(f"Executing command: {cmd}")
    
    try:
        logger.info(os.system(cmd))
    except Exception as e:
        logger.error(f"Command execution failed: {e}")
        raise
    else:
        logger.info("Command executed successfully")