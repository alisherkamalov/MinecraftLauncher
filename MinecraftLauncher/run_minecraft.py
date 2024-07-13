import minecraft_launcher_lib
import subprocess
from uuid import uuid1
from random_username.generate import generate_username
from ui_launcher import version_dropdown,directory_dropdown
import os



def run_minecraft():
    username = ''
    if username == '':
        username = generate_username()[0]
    version = f'{version_dropdown.value}'
    minecraft_directory_run = f'{directory_dropdown.value}'
    options = {
        "username": username,
        "uuid": str(uuid1()),
        "token": ''
    }
    print(version)
    minecraft_command = minecraft_launcher_lib.command.get_minecraft_command(version, minecraft_directory_run, options)

    # Start Minecraft
    subprocess.run(minecraft_command)
    