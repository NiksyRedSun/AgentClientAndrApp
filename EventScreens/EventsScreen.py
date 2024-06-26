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
from reqs import get_all_active_agents, get_all_clients, get_all_events, attempt, get_agent, get_client, get_event, \
    get_trash_event
import datetime
from functools import partial




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

                self.events_grid.add_widget(
                    Button(text="[color=black]Отчет[/color]", size_hint=(0.20, 1), font_name="Lucida Console",
                           background_color=(3 / 255, 168 / 255, 98 / 255, 0.8), markup=True, background_normal="",
                           on_press=partial(self.screen_transition_to_event, event["id"], "Клиент"), font_size=14))
            else:
                self.events_grid.add_widget(Label(text=f"[color=03A062]Уборка мусора, статус: {event['status']}\n"
                                                       f"Дата и время: {datetime.datetime.fromtimestamp(event['time'])}[/color]",
                                                  size_hint=(0.80, 1), text_size=(Window.width * 0.75, None), halign="left",
                                                  markup=True, font_name="Lucida Console"))

                self.events_grid.add_widget(
                    Button(text="[color=black]Отчет[/color]", size_hint=(0.20, 1), font_name="Lucida Console",
                           background_color=(3 / 255, 168 / 255, 98 / 255, 0.8), markup=True, background_normal="",
                           on_press=partial(self.screen_transition_to_event, event["id"], "Мусор"), font_size=14))





    def screen_transition_to_event(self, *args):

        if args[1] == "Клиент":
            event = get_event(args[0])
            agent = get_agent(event['agent'])
            client = get_client(event['client'])

            if event['status'] == 1:
                info = f"[color=03A062]Наш агент по кличке {agent['nickname']} блестяще выполнил свою работу.\n" \
                       f"{client['first_name']} {client['last_name']} - бесследно исчез.\n\n" \
                       f"Опыт за убийство: {client['exp']}\n" \
                       f"Награда за убийство: {client['price']}\n\n" \
                       f"Дата и время: {datetime.datetime.fromtimestamp(event['time'])}[/color]"

            elif event['status'] == 2:
                info = f"[color=03A062]Наш агент по кличке {agent['nickname']} провалил всю операцию.\n" \
                       f"{client['first_name']} {client['last_name']} - ускользнул.\n\n" \
                       f"Однако, агенту удалось сохранить свою личность в тайне, что позволяет ему остаться в круге единомышленников.\n\n" \
                       f"Дата и время: {datetime.datetime.fromtimestamp(event['time'])}[/color]"

            elif event['status'] == 3:
                info = f"[color=03A062]Наш агент по кличке {agent['nickname']} провалил всю операцию.\n" \
                       f"{client['first_name']} {client['last_name']} - ускользнул.\n\n" \
                       f"Агенту не удалось сохранить свою личность в тайне. Мы будем отрицать все контакты с ним.\n" \
                       f"Кроме того, в скором времени, на агента будет открыта охота с целью замести следы.\n\n" \
                       f"Дата и время: {datetime.datetime.fromtimestamp(event['time'])}[/color]"

            elif event['status'] == 4:
                info = f"[color=03A062]Наш агент по кличке {agent['nickname']} - мертв.\n" \
                       f"{client['first_name']} {client['last_name']} - ускользнул.\n\n" \
                       f"В ходе операции наш агент был раскрыт и убит.\n" \
                       f"Мы будет отрицать всякие контакты с ним. Однако нам не придется тратить время, чтобы замести следы.\n\n" \
                       f"Дата и время: {datetime.datetime.fromtimestamp(event['time'])}[/color]"

        elif args[1] == "Мусор":
            event = get_trash_event(args[0])
            agent = get_agent(event['agent'])
            target = get_agent(event['target'])

            if event['status'] == 1:
                info = f"[color=03A062]Наш агент по кличке \"{agent['nickname']}\" блестяще выполнил свою работу.\n" \
                       f"{target['first_name']} \"{target['nickname']}\" {target['last_name']} - не представляет опасности для нас.\n\n" \
                       f"Опыт за убийство: {int(target['exp'] // 4)}\n" \
                       f"Награда за убийство: {int(target['money'] // 4)}\n\n" \
                       f"Дата и время: {datetime.datetime.fromtimestamp(event['time'])}[/color]"

            elif event['status'] == 2:
                info = f"[color=03A062]Наш агент по кличке \"{agent['nickname']}\" провалил уборку мусора.\n" \
                       f"{target['first_name']} \"{target['nickname']}\" {target['last_name']} - ускользнул.\n\n" \
                       f"Однако, агенту удалось сохранить свою личность в тайне, что позволяет ему остаться в круге единомышленников.\n\n" \
                       f"Дата и время: {datetime.datetime.fromtimestamp(event['time'])}[/color]"

            elif event['status'] == 3:
                info = f"[color=03A062]Наш агент по кличке {agent['nickname']} провалил уборку мусора.\n" \
                       f"{target['first_name']} \"{target['nickname']}\" {target['last_name']} - ускользнул.\n\n" \
                       f"В ходе операции личность уборщика также была раскрыта. Нам придется открыть охоту и на него.\n\n" \
                       f"Дата и время: {datetime.datetime.fromtimestamp(event['time'])}[/color]"


            elif event['status'] == 4:
                info = f"[color=03A062]Наш агент по кличке {agent['nickname']} - мертв.\n" \
                       f"{target['first_name']} \"{target['nickname']}\" {target['last_name']} - ускользнул оставив после себя труп.\n\n" \
                       f"Мы будет отрицать всякие контакты с нашим агентом. Нам не придется тратить время, чтобы замести следы." \
                       f"Но нужно будет организовать еще одну уборку мусора\n\n" \
                       f"Дата и время: {datetime.datetime.fromtimestamp(event['time'])}[/color]"

        self.manager.get_screen("EventScreen").info_label.text = info
        self.manager.current = "EventScreen"

