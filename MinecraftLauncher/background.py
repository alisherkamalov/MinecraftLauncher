import flet as ft 


class Background(ft.Image):
    def __init__(self):
        super().__init__()
        self.src='background.png'
        self.expand=True
        
class BlackOut(ft.Container):
    def __init__(self):
        super().__init__()
        self.bgcolor=ft.colors.BLACK45
        self.expand=True
        self.height=9999