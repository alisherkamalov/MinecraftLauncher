import flet as ft 
import minecraft_launcher_lib
import os


directory_dropdown = ft.Dropdown(
    width=250,
    bgcolor=ft.colors.LIGHT_GREEN_600,
    hint_text="Выберите директорию",
    autofocus=True,
    hint_style=ft.TextStyle(
        weight=ft.FontWeight.W_500,
        height=2,
        color='white'
    ),
    text_style=ft.TextStyle(
        weight=ft.FontWeight.W_500,
        color='white'
    ),
    options=[
        ft.dropdown.Option('E:/.minecraft'),
        ft.dropdown.Option('C:/.minecraft'),
        ft.dropdown.Option('F:/.minecraft'),
        ft.dropdown.Option('D:/.minecraft'),
    ]
    
)



version_dropdown = ft.Dropdown(
    width=250,
    bgcolor=ft.colors.LIGHT_GREEN_600,
    hint_text="Выберите версию",
    autofocus=True,
    hint_style=ft.TextStyle(
        weight=ft.FontWeight.W_500,
        height=2,
        color='white'
    ),
    text_style=ft.TextStyle(
        weight=ft.FontWeight.W_500,
        color='white'
    ),
    
)

version_dropdown_more = ft.Dropdown(
    width=350,
    bgcolor=ft.colors.LIGHT_GREEN_600,
    hint_text="Выберите версию для скачивания",
    autofocus=True,
    hint_style=ft.TextStyle(
        weight=ft.FontWeight.W_500,
        height=2,
        color='white'
    ),
    text_style=ft.TextStyle(
        weight=ft.FontWeight.W_500,
        color='white'
    ),
    
)

minecraft_is_run = ft.Text(
    'Minecraft Запускается...',
    color='white',
    weight=ft.FontWeight.W_700,
    animate_opacity=500,
    opacity=0,
    size=25,
    offset=ft.transform.Offset(2,3)
)

directory = "E:/.minecraft/versions"

# Проверяем, существует ли директория с версиями Minecraft
if os.path.exists(directory) and os.path.isdir(directory):
    # Получаем список папок (версий Minecraft) в директории
    folders = [name for name in os.listdir(directory) if os.path.isdir(os.path.join(directory, name))]
    
    # Создаем список опций для выпадающего списка
    options = []
    for folder in folders:
        options.append(ft.dropdown.Option(folder))  # Добавляем каждую версию как опцию
        
    # Устанавливаем опции в выпадающем списке
    version_dropdown.options = options
    
else:
    # Если директория не существует или не содержит версий, устанавливаем соответствующее сообщение
    version_dropdown.options = [ft.dropdown.Option('Нету версий')]

options_more = []
for i in minecraft_launcher_lib.utils.get_version_list():
    options_more.append(ft.dropdown.Option(i['id']))
    version_dropdown_more.options = options_more
    
close_launcher = ft.IconButton(
    icon=ft.icons.ARROW_BACK_IOS_NEW_OUTLINED,
    icon_color='white'
)

minimaze_laucher = ft.IconButton(
    icon=ft.icons.MINIMIZE_OUTLINED,
    icon_color='white'
)

class Header(ft.Container):
    def __init__(self):
        super().__init__()
        self.bgcolor=ft.colors.LIGHT_GREEN_500
        self.expand=True
        self.height=75
        self.content=ft.Row([
            ft.Row([
                close_launcher,
                minimaze_laucher
            ],alignment=ft.MainAxisAlignment.START,offset=ft.transform.Offset(0.1,0)),
            ft.Row([
                ft.Text(
                'Launcher Minecraft By Alexander',
                size=25,
                weight=ft.FontWeight.W_700,
                color='white'
            )
            ],alignment=ft.MainAxisAlignment.CENTER,expand=True),
            
            
        ],expand=True)
        
class Body(ft.Container):
    def __init__(self):
        super().__init__()
        self.expand=True
        self.height=500
        self.content=ft.Column([
            ft.Row([
                ft.Column([
                ft.Row([
                   ft.Text(
                       'Скачанные версии:',
                       color='white',
                       size=25,
                       weight=ft.FontWeight.W_700
                   ) 
                ]),
                ft.Row([
                    version_dropdown
                ])
                ]),
                ft.Column([
                ft.Row([
                   ft.Text(
                       'Доступные версии:',
                       color='white',
                       size=25,
                       weight=ft.FontWeight.W_700
                   ) 
                ]),
                ft.Row([
                    version_dropdown_more
                ])
                ]),
                ft.Column([
                ft.Row([
                    ft.Text(
                       'Директории:',
                       color='white',
                       size=25,
                       weight=ft.FontWeight.W_700
                   ) 
                ]),
                ft.Row([
                    directory_dropdown
                ])
                
                ]),
                
            ],offset=ft.transform.Offset(0.01,0.2)),
            
            ft.Column([
                ft.Row([
                    minecraft_is_run
                ],alignment=ft.MainAxisAlignment.CENTER,expand=True)
            ])
        ])
        
class InstallerButton(ft.Container):
    def __init__(self,click):
        super().__init__()
        self.width=175
        self.height=75
        self.border_radius=15
        self.bgcolor=ft.colors.LIGHT_GREEN_800
        self.content=ft.Row([
            ft.Text(
                'Install',
                size=25,
                weight=ft.FontWeight.W_500,
                color='white'
            )
        ],alignment=ft.MainAxisAlignment.CENTER)
        self.on_click=click
        
class RunButton(ft.Container):
    def __init__(self,click):
        super().__init__()
        self.width=175
        self.height=75
        self.border_radius=15
        self.bgcolor=ft.colors.LIGHT_GREEN_800
        self.content=ft.Row([
            ft.Text(
                'Run',
                size=25,
                weight=ft.FontWeight.W_500,
                color='white'
            )
        ],alignment=ft.MainAxisAlignment.CENTER)
        self.on_click=click
        
