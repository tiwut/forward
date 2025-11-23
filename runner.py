import os
import subprocess
import sys

def run_main_exe():
    try:
        if getattr(sys, 'frozen', False):
            script_dir = os.path.dirname(sys.executable)
        else:
            script_dir = os.path.dirname(os.path.abspath(__file__))

        target_exe = os.path.join(script_dir, "main.exe")

        if not os.path.exists(target_exe):
            print(f"Error: The file {target_exe} was not found.")
            return
        if os.name == 'nt':
            subprocess.Popen(
                [target_exe],
                cwd=script_dir,
                creationflags=subprocess.CREATE_NO_WINDOW
            )
        else:
            subprocess.Popen(
                [target_exe],
                cwd=script_dir
            )

    except Exception as e:
        print(f"An error has occurred: {e}")

if __name__ == "__main__":
    run_main_exe()