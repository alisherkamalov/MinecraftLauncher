import flet as ft
from background import Background, BlackOut
from ui_launcher import Header, Body, InstallerButton, RunButton,minecraft_is_run,minimaze_laucher,close_launcher
from run_minecraft import run_minecraft
from progress import progress
from installer_minecraft import installer_minecraft
import time

# Класс для основного приложения
class Main:

    # Метод для инициализации интерфейса
    def main(self, page: ft.Page):
        self.page = page
        self.page.padding = 0
        self.page.spacing = 0
        self.page.window_title_bar_hidden=True
        self.page.window.maximizable = False
        self.page.window.resizable = False
        self.progress_text = ft.Text(
            f'Началась загрузка версии, не нажимайте на run',
            color='white',
            size=25,
            weight=ft.FontWeight.W_600,
            animate_opacity=500,
            opacity=0,
            offset=ft.transform.Offset(0.1,0)
        )
        self.page.add(
            ft.Column([
                ft.Stack([
                    Background(),
                    BlackOut(),
                    ft.Column([
                        ft.Row([
                            Header()
                        ]),
                        ft.Row([
                            Body()
                        ]),
                        ft.Row([
                            ft.Container(
                                expand=True,
                                height=75,
                                content=ft.Column([
                                    ft.Row([
                                        self.progress_text
                                    ]),
                                    ft.Row([
                                        progress  # Предполагается, что это прогрессбар из вашего модуля progress
                                    ])
                                ])
                            ),
                            InstallerButton(click=self.install),
                            RunButton(click=self.run)
                        ],
                            alignment=ft.MainAxisAlignment.END,
                            offset=ft.transform.Offset(-0.01, 0)
                        )
                    ])
                ])
            ], expand=True)
        )
        self.page.update()

    # Метод для запуска Minecraft
    def run(self, event):
        minecraft_is_run.opacity=1
        self.page.update()
        time.sleep(2)
        minecraft_is_run.opacity=0
        self.page.update()
        run_minecraft()  # функция запуска Minecraft
    
    def close_launcher_minecraft(self):
        self.page.window.destroy()
        self.page.update()
        
    def minimazed_launcher_minecraft(self):
        self.page.window.minimized=True
        self.page.update()
        
    close_launcher.on_click=close_launcher_minecraft
    minimaze_laucher.on_click=minimazed_launcher_minecraft

    # Метод для установки Minecraft
    def install(self, event):
        progress.opacity = 1
        self.progress_text.opacity = 1
        progress.value = None
        self.page.update()
        installer_minecraft()  # Вызов функции установки Minecraft из installer_minecraft.py
        progress.opacity = 0
        self.progress_text.value='Загрузка окончена, нажмите run'
        self.page.update()
        time.sleep(1)
        self.progress_text.opacity = 0
        self.page.update()
        
    



if __name__ == '__main__':
    app = Main()
    ft.app(
        app.main,
        assets_dir='assets'
    )
