import subprocess
import time


def clear_screen() -> None:
    time.sleep(0.8)
    subprocess.run(["clear"])
