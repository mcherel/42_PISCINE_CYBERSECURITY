#!/usr/bin/env python3

import subprocess
import argparse
import sys
import os

def create_venv(venv_name):
    if os.path.exists(venv_name):
        print(f"Virtual environment {venv_name} is already created.")
    else:
        subprocess.run([sys.executable, '-m', 'venv', venv_name], check=True)

""" def activate_venv(venv_name):
    #this activation works only for Linux
    activate_cmd = f'bash -c source {venv_name}/bin/activate'
    subprocess.run(activate_cmd, shell=True, check=True) """
    
def activate_venv(venv_name):
    if os.path.exists(venv_name):
        activate_script = os.path.join(venv_name, 'bin', 'activate')
        subprocess.run(f'bash -c "source {activate_script} && exec $SHELL"', shell=True, check=True)
    else:
        print("Did not find .venv")
        
def deactivate_venv():
    subprocess.run('unset VIRTUAL_ENV', shell=True, check=True)
    # need to exit manually 
    #subprocess.run('exit', shell=True, check=True)

if __name__ == "__main__":
    venv_name = ".venv"
    create_venv(venv_name)
    activate_venv(venv_name)
    deactivate_venv()
    parser = argparse.ArgumentParser()
    # parser.add_argument("echo")
    args = parser.parse_args()
    print(sys.path)
