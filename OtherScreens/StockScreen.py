from kivy.app import App
from kivy.core.text import LabelBase
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.config import Config
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
from kivy.uix.scrollview import ScrollView
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition, WipeTransition, SwapTransition, CardTransition, SlideTransition, ShaderTransition
from reqs import get_all_active_agents, get_all_clients, get_all_events, new_client, new_agent
import datetime


class StockScreen(Screen):
    def __init__(self, **kwargs):
        super(StockScreen, self).__init__(**kwargs)


        self.grid = GridLayout(cols=1)

        self.grid.add_widget(
            Button(text="[color=black]Вернуться[/color]", size_hint=(1, .15), font_size=24, font_name="Lucida Console",
                   background_color=(3 / 255, 168 / 255, 98 / 255, 0.8), markup=True, background_normal="",
                   on_press=self.back))

        self.name_label = Label(text="[color=03A062]Биржа[/color]", size_hint=(1, .6),
                                    max_lines=2,
                                    text_size=(Window.width * 0.3, Window.height * 0.35), halign="center", valign="top",
                                    font_size=28, markup=True, font_name="Lucida Console")

        self.grid.add_widget(self.name_label)

        self.info_label = Label(text="[color=03A062]Здесь будет непосредственно информация[/color]", size_hint=(1, .5),
                                max_lines=2,
                                text_size=(Window.width * 0.35, Window.height * 0.90), halign="left", valign="top",
                                font_size=18, markup=True, font_name="Lucida Console")

        self.grid.add_widget(self.info_label)

        self.grid.add_widget(
            Button(text="[color=black]Найти клиента[/color]", size_hint=(1, .15), font_size=24, font_name="Lucida Console",
                   background_color=(3 / 255, 168 / 255, 98 / 255, 0.8), markup=True, background_normal="", on_press=self.new_agent))

        self.grid.add_widget(
            Button(text="[color=black]Найти агента[/color]", size_hint=(1, .15), font_size=24, font_name="Lucida Console",
                   background_color=(3 / 255, 168 / 255, 98 / 255, 0.8), markup=True, background_normal="", on_press=self.new_client))


        self.add_widget(self.grid)


    def back(self, *args):
        self.manager.current = "MenuScreen"


    def new_client(self, *args):
        client = new_client()
        info = f"[color=03A062]Мы подыскали хорошего клиента, его имя {client['first_name']} {client['last_name']}[/color]"
        self.info_label.text = info

    def new_agent(self, *args):
        agent = new_agent()
        info = f"[color=03A062]Свежая кровь поступила в нашу организацию, его имя {agent['first_name']} {agent['last_name']}," \
               f"позывной - {agent['nickname']}[/color]"
        self.info_label.text = info



