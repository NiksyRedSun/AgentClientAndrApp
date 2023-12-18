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
from reqs import get_all_active_agents, get_all_clients, get_all_events
import datetime




class EventsScreen(Screen):
    def __init__(self, **kwargs):
        super(EventsScreen, self).__init__(**kwargs)

        self.grid = GridLayout(cols=1)

        self.scroll_view = ScrollView(size_hint=(1, 0.75), pos=(0, 0))


        self.grid.add_widget(Button(text="[color=black]Вернуться[/color]", size_hint=(1, .10),
                                                     font_size=24, font_name="Lucida Console", background_color=(3/255, 168/255, 98/255, 0.8),
                                                     markup=True, background_normal="", on_press=self.back))


        self.grid.add_widget(Label(text="[color=03A062]События[/color]", size_hint=(1, .10), max_lines=10,
                                   text_size=(Window.width*0.8, None), halign="center",
                                   font_size=28, markup=True, font_name="Lucida Console"))

        # Здесь будет сетка для объектов
        self.events_grid = GridLayout(cols=2, size_hint=(1, None), row_force_default=True, row_default_height=70)
        self.events_grid.bind(minimum_height=self.events_grid.setter("height"))

        self.new_event_list()

        self.scroll_view.add_widget(self.events_grid)
        self.grid.add_widget(self.scroll_view)
        self.add_widget(self.grid)


    def back(self, *args):
        self.manager.current = "MenuScreen"



    def on_pre_enter(self, *args):
        self.new_event_list()


    def new_event_list(self):
        self.events_grid.clear_widgets()

        self.events = get_all_events()


        for event in self.events:
            if "client" in event:
                self.events_grid.add_widget(Label(text=f"[color=03A062]Покушение на клиента, статус: {event['status']}\n"
                                                       f"Дата и время: {datetime.datetime.fromtimestamp(event['time'])}[/color]",
                                                  size_hint=(0.80, 1), text_size=(Window.width * 0.75, None), halign="left",
                                                  markup=True, font_name="Lucida Console"))
            else:
                self.events_grid.add_widget(Label(text=f"[color=03A062]Уборка мусора, статус: {event['status']}\n"
                                                       f"Дата и время: {datetime.datetime.fromtimestamp(event['time'])}[/color]",
                                                  size_hint=(0.80, 1), text_size=(Window.width * 0.75, None), halign="left",
                                                  markup=True, font_name="Lucida Console"))

            self.events_grid.add_widget(Button(text="[color=black]Отчет[/color]", size_hint=(0.20, 1), font_name="Lucida Console",
                                  background_color=(3/255, 168/255, 98/255, 0.8), markup=True, background_normal="", font_size=14))
