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
from reqs import get_all_active_agents, get_all_clients, get_all_events, get_client
import datetime
from functools import partial



info_dict = {1: 'цель с минимальной охраной, неосведомлена о возможной опасности',
2: 'цель, которая может иметь небольшую охрану, но её легко обойти',
3: 'цель, защищена опытной охраной и базовыми техническими средствами',
4:'цель с высокой степенью защиты, включая физическую, электронную и техническую безопасность',
5: 'цель, охраняемая профессиональными телохранителями, современными системами безопасности и тщательной разведкой',
6: 'высокопоставленная личность, государственного значения, с максимальной защитой, '
   'включая военные силы, секретные службы и высокотехнологичные системы безопасности'}




class ClientsScreen(Screen):
    def __init__(self, **kwargs):
        super(ClientsScreen, self).__init__(**kwargs)

        self.grid = GridLayout(cols=1)

        self.scroll_view = ScrollView(size_hint=(1, 0.75), pos=(0, 0))


        self.grid.add_widget(Button(text="[color=black]Вернуться[/color]", size_hint=(1, .10), font_size=24,
                                  font_name="Lucida Console", background_color=(3/255, 168/255, 98/255, 0.8),
                                  markup=True, background_normal="", on_press=self.back))

        self.grid.add_widget(Label(text="[color=03A062]Наши клиенты[/color]", size_hint=(1, .10), max_lines=10,
                                   text_size=(Window.width*0.8, None), halign="center",
                                   font_size=28, markup=True, font_name="Lucida Console"))

        #Здесь будет сетка для объектов
        self.clients_grid = GridLayout(cols=2, size_hint=(1, None), row_force_default=True, row_default_height=70)
        self.clients_grid.bind(minimum_height=self.clients_grid.setter("height"))



        self.scroll_view.add_widget(self.clients_grid)
        self.grid.add_widget(self.scroll_view)
        self.add_widget(self.grid)


    def back(self, *args):
        self.manager.current = "MenuScreen"


    def on_pre_enter(self, *args):
        self.new_clients_list()


    def new_clients_list(self):
        self.clients_grid.clear_widgets()

        self.clients = get_all_clients()

        for client in self.clients:
            self.clients_grid.add_widget(Label(text=f"[color=03A062]{client['first_name']} {client['last_name']}\n"
                                                    f"Уровень защиты: {client['security_level']}, цена: {client['price']},"
                                                    f" опыт за убийство {client['exp']}[/color]",
                                               size_hint=(0.80, 0.9), text_size=(Window.width * 0.75, None), halign="left",
                                               markup=True, font_name="Lucida Console"))

            self.clients_grid.add_widget(Button(text="[color=black]Контракт[/color]", size_hint=(0.20, 1), font_name="Lucida Console",
                                  background_color=(3/255, 168/255, 98/255, 0.8), markup=True, background_normal="", font_size=12,
                                                on_press=partial(self.screen_transition_to_client, client["id"])))


    def screen_transition_to_client(self, *args):
        client = get_client(args[0])

        info = f"[color=03A062]Имя: {client['first_name']} {client['last_name']}\n" \
               f"Возраст: {client['age']},\n" \
               f"опыт за убийство: {client['exp']}, " \
               f"награда за убийство: {client['price']},\n\n" \
               f"Уровень защиты:\n" \
               f"{info_dict[client['security_level']]}[/color]"

        self.manager.get_screen("ContractScreen").client = args[0]
        self.manager.get_screen("ClientScreen").info_label.text = info
        self.manager.current = "ClientScreen"
