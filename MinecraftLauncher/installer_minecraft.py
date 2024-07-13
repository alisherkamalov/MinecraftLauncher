import minecraft_launcher_lib
from ui_launcher import version_dropdown_more,directory_dropdown
import os

# Глобальные переменные для отслеживания прогресса и статуса
current_max = 0
progress = 0
status_text = ''

# Функция для установки прогресса установки
def set_progress(progress_value: int):
    global progress
    if current_max != 0:
        progress = progress_value / 100
        # Дополнительные действия, если необходимо
        return progress

# Функция для установки статуса установки
def set_status(text):
    global status_text
    status_text = text

# Функция для установки максимального значения прогресса
def set_max(new_max: int):
    global current_max
    current_max = new_max / 100

# Основная функция установки Minecraft
def installer_minecraft():
    version = f'{version_dropdown_more.value}'
    minecraft_directory = f'{directory_dropdown.value}'
    callback = {
        "setStatus": set_status,
        "setProgress": set_progress,
        "setMax": set_max
    }
    print(minecraft_directory)
    minecraft_launcher_lib.fabric.install_fabric(version, minecraft_directory, callback=callback)

    # Возвращаем функцию установки статуса (если нужно)
    return set_status
