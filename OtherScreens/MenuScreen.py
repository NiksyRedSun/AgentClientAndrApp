from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition, WipeTransition, SwapTransition, CardTransition, SlideTransition, ShaderTransition
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.uix.button import Button
import datetime




class MenuScreen(Screen):
    def __init__(self, **kwargs):
        super(MenuScreen, self).__init__(**kwargs)


        self.grid = GridLayout(cols=1)

        self.grid.add_widget(Label(text="[color=03A062]Добро пожаловать в наше приложение про клиентов и агентов[/color]",
                                   size_hint=(1, 2.5), max_lines=10, text_size=(Window.width*0.3, None), halign="center",
                                   font_size=22, markup=True, font_name="Lucida Console"))

        self.agents_button = Button(text="[color=black]Агенты[/color]", font_size=32, font_name="Lucida Console",
                                    background_color=(3/255, 168/255, 98/255, 0.8), markup=True, background_normal="")

        self.clients_button = Button(text="[color=black]Клиенты[/color]", font_size=32, font_name="Lucida Console",
                                     background_color=(3/255, 168/255, 98/255, 0.8), markup=True, background_normal="")

        self.events_button = Button(text="[color=black]События[/color]", font_size=32, font_name="Lucida Console",
                                    background_color=(3/255, 168/255, 98/255, 0.8), markup=True, background_normal="")

        self.stock_button = Button(text="[color=black]Биржа[/color]", font_size=32, font_name="Lucida Console",
                                    background_color=(3/255, 168/255, 98/255, 0.8), markup=True, background_normal="")

        self.trash_button = Button(text="[color=black]Уборка мусора[/color]", font_size=32, font_name="Lucida Console",
                                    background_color=(3/255, 168/255, 98/255, 0.8), markup=True, background_normal="")

        self.exit_button = Button(text="[color=black]Выход[/color]", font_size=32, font_name="Lucida Console",
                                  background_color=(3/255, 168/255, 98/255, 0.8), markup=True, background_normal="")

        self.agents_button.bind(on_press=self.screen_transition_to_agents)
        self.clients_button.bind(on_press=self.screen_transition_to_clients)
        self.events_button.bind(on_press=self.screen_transition_to_events)
        self.stock_button.bind(on_press=self.screen_transition_to_stock)
        self.trash_button.bind(on_press=self.screen_transition_to_trash)
        self.exit_button.bind(on_press=self.exit)

        self.grid.add_widget(self.agents_button)
        self.grid.add_widget(self.clients_button)
        self.grid.add_widget(self.events_button)
        self.grid.add_widget(self.stock_button)
        self.grid.add_widget(self.trash_button)
        self.grid.add_widget(self.exit_button)


        self.add_widget(self.grid)


    def screen_transition_to_agents(self, *args):
        self.manager.current = "AgentsScreen"

    def screen_transition_to_clients(self, *args):
        self.manager.current = "ClientsScreen"

    def screen_transition_to_events(self, *args):
        self.manager.current = "EventsScreen"

    def screen_transition_to_stock(self, *args):
        self.manager.current = "StockScreen"

    def screen_transition_to_trash(self, *args):
        self.manager.current = "TrashScreen"

    def exit(self, *args):
        App.get_running_app().stop()


