import math
import flet as ft
from flet import TextField
from flet.core.control_event import ControlEvent
import random
import asyncio

angles = list(range(0, 361, 10))  


colors = [
    "#FF4D4D", "#FF1A75", "#FF66B2", "#FFB3D9", "#FF80BF",  # pink-reds
    "#FFAA00", "#FFC300", "#FFD700", "#FFE066", "#FFF275",  # yellows
    "#66FF66", "#33CC33", "#00FF7F", "#00E68A", "#99FF99",  # greens
    "#33CCFF", "#0099FF", "#1AC6FF", "#66D9FF", "#80E5FF",  # blues
    "#9966FF", "#B366FF", "#CC99FF", "#D580FF", "#E6B3FF",  # purples
    "#FF704D", "#FF8533", "#FF9966", "#FFAD33", "#FFCC80",  # oranges
    "#FF3399", "#FF6699", "#FF99CC", "#FFCCE5", "#FF66FF",  # pinks
    "#00FFFF", "#33FFFF", "#66FFFF", "#80FFFF", "#99FFFF",  # cyans
    "#C0C0C0", "#D9D9D9", "#BFBFBF", "#999999", "#FFFFFF",  # greys/white
]





class Sine(ft.ElevatedButton):
    def __init__(self, onclick):
        super().__init__()
        self.bgcolor = ft.Colors.BLUE_400
        self.color = ft.Colors.WHITE
        self.text = "Sine"
        self.on_click = onclick   

class Cosine(ft.ElevatedButton):
    def __init__(self, onclick):
        super().__init__()
        self.bgcolor = ft.Colors.PINK_600
        self.color = ft.Colors.WHITE
        self.text = "Cosine"
        self.on_click = onclick     


def main(page: ft.Page):
    page.title = "I am not a fan of sin cos tan."
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.theme_mode = "dark"
    scaling_factor = page.width / 360

    area = ft.Stack(expand=True)

    async def animation(function, ball):
        
        i = 0

        while True:
            if function == "sine":
                ball.top = 300 +  math.sin(math.radians(angles[i])) * 100
            elif function == "cosine":
                ball.top = 300  +  math.cos(math.radians(angles[i])) * 100

            ball.left = angles[i] * scaling_factor
            ball.update()
            i += 1
            if i >= len(angles): 
                i = 0
            await asyncio.sleep(0.03)


    def create_ball(e, func):

        color = random.choice(colors)

        top = random.randint(100, 300)
        left = random.randint(100, 300)
        ball = ft.Container(
            width=40,
            height=40,
            bgcolor=color,
            border_radius=100,
            left=left, 
            top=top,   
        )

        area.controls.append(ball)
        page.update()

        if func == "cosine":
            page.run_task(animation, "cosine", ball)
        elif func == "sine":
            page.run_task(animation, "sine", ball)

   


    page.add(
        ft.Row(
            [
                Sine(onclick=lambda e: create_ball(e, "sine")),
                Cosine(onclick=lambda e: create_ball(e, "cosine")),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        ),
        area
    )



    
ft.app(main)

