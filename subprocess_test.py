import subprocess
import shlex


def exec_cmd(cmd):
    try:
        text = subprocess.run(shlex.split(cmd), check=True, text=True, capture_output=True)

        print(text.args)
        # print(text.stderr)
    except subprocess.CalledProcessError as e:
        print(f"Command '{e.cmd}' failed with return code {e.returncode}")
        print(f"Output: {e.output}")
        print(f"Error: {e.stderr}")


if __name__ == "__main__":
    exec_cmd('git branch')