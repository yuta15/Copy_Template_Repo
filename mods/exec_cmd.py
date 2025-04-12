import subprocess
import shlex
import sys

from mods.logger import set_logger


def exec_cmd(cmd):
    """コマンドを実行する関数"""
    logger = set_logger(__name__)
    logger.info(f"Executing command: {cmd}")
    
    try:
        logger.info("Starting command execution")
        result = subprocess.run(
            shlex.sqlit(cmd),
            check=True,
            text=True,
            capture_output=True
            )
    except subprocess.CalledProcessError as e:
        # コマンドの実行に失敗した場合の処理
        logger.error(f"Command '{e.cmd}' failed with return code {e.returncode}")
        logger.error(f"Output: {e.stdout}")
        logger.error(f"Error: {e.stderr}")
        sys.exet(1)
    except Exception as e:
        # その他の例外処理
        logger.error(f"Command execution failed: {e}")
        sys.exit(1)
    else:
        logger.info("Command executed successfully")
        return result.stdout