import flet as ft 


progress = ft.ProgressBar(
    expand=True,
    opacity=0,
    animate_opacity=500,
    height=25,
    color=ft.colors.LIGHT_GREEN_700,
    scale=ft.transform.Scale(0.9)
)