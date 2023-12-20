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
from reqs import get_all_active_agents, get_all_clients, get_all_events, get_agent, get_client, attempt, \
    trash_out_attempt
import datetime



class TrashContractScreen(Screen):
    def __init__(self, **kwargs):
        super(TrashContractScreen, self).__init__(**kwargs)

        self.client = None
        self.target = None

        self.grid = GridLayout(cols=1)

        self.grid.add_widget(
            Button(text="[color=black]Вернуться[/color]", size_hint=(1, .05), font_size=24, font_name="Lucida Console",
                   background_color=(3 / 255, 168 / 255, 98 / 255, 0.8), markup=True, background_normal="",
                   on_press=self.back))

        self.name_label = Label(text="[color=03A062]Уборка[/color]", size_hint=(1, .2),
                                    max_lines=2,
                                    text_size=(Window.width * 0.3, Window.height * 0.35), halign="center", valign="top",
                                    font_size=28, markup=True, font_name="Lucida Console")

        self.grid.add_widget(self.name_label)

        self.info_label = Label(text="[color=03A062]Здесь будет непосредственно информация[/color]", size_hint=(1, .2),
                                max_lines=2,
                                text_size=(Window.width * 0.35, Window.height * 0.90), halign="left", valign="top",
                                font_size=18, markup=True, font_name="Lucida Console")

        self.grid.add_widget(self.info_label)

        self.grid.add_widget(
            Button(text="[color=black]Вынести мусор[/color]", size_hint=(1, .05), font_size=24, font_name="Lucida Console",
                   background_color=(3 / 255, 168 / 255, 98 / 255, 0.8), markup=True, background_normal="",
                   on_press=self.trash_away))

        self.add_widget(self.grid)


    def back(self, *args):
        self.manager.current = "TrashCleanerScreen"


    def trash_away(self, *args):
        event = trash_out_attempt(self.agent, self.target)
        agent = get_agent(self.agent)
        target = get_agent(self.target)

        if event['status'] == 1:
            info = f"[color=03A062]Наш агент по кличке \"{agent['nickname']}\" блестяще выполнил свою работу.\n" \
                   f"{target['first_name']} \"{target['nickname']}\" {target['last_name']} - не представляет опасности для нас.\n\n" \
                   f"Опыт за убийство: {int(target['exp']//4)}\n" \
                   f"Награда за убийство: {int(target['money']//4)}[/color]"

        elif event['status'] == 2:
            info = f"[color=03A062]Наш агент по кличке \"{agent['nickname']}\" провалил уборку мусора.\n" \
                   f"{target['first_name']} \"{target['nickname']}\" {target['last_name']} - ускользнул.\n\n" \
                   f"Однако, агенту удалось сохранить свою личность в тайне, что позволяет ему остаться в круге единомышленников.[/color]"

        elif event['status'] == 3:
            info = f"[color=03A062]Наш агент по кличке {agent['nickname']} провалил уборку мусора.\n" \
                   f"{target['first_name']} \"{target['nickname']}\" {target['last_name']} - ускользнул.\n\n" \
                   f"В ходе операции личность уборщика также была раскрыта. Нам придется открыть охоту и на него.[/color]"

        elif event['status'] == 4:
            info = f"[color=03A062]Наш агент по кличке {agent['nickname']} - мертв.\n" \
                   f"{target['first_name']} \"{target['nickname']}\" {target['last_name']} - ускользнул оставив после себя труп.\n\n" \
                   f"Мы будет отрицать всякие контакты с нашим агентом. Нам не придется тратить время, чтобы замести следы." \
                   f"Но нужно будет организовать еще одну уборку мусора[/color]"


        self.manager.get_screen("TrashResultScreen").info_label.text = info
        self.manager.current = "TrashResultScreen"
