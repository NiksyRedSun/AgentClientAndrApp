from kivy.app import App
from kivy.core.text import LabelBase
from kivy.uix.screenmanager import ScreenManager, SlideTransition

from kivy.core.window import Window
import AgentScreens
import TrashScreens
import ClientScreens
import OtherScreens
import EventScreens

Window.size = (300, 585)



LabelBase.register(name='Lucida Console',
                      fn_regular='C:\\repos\\AgentClientAndrApp\\lucida-console.ttf')



class ScreenManagement(ScreenManager):
    def __init__(self, **kwargs):
        super(ScreenManagement, self).__init__(**kwargs)




class Application(App):
    def build(self):
        self.config.width=300
        self.config.height=300
        sm = ScreenManagement(transition=SlideTransition())

        sm.add_widget(OtherScreens.MenuScreen.MenuScreen(name="MenuScreen"))
        sm.add_widget(AgentScreens.AgentsScreen.AgentsScreen(name="AgentsScreen"))
        sm.add_widget(AgentScreens.AgentScreen.AgentScreen(name="AgentScreen"))
        sm.add_widget(ClientScreens.ClientsScreen.ClientsScreen(name="ClientsScreen"))
        sm.add_widget(ClientScreens.ClientScreen.ClientScreen(name="ClientScreen"))
        sm.add_widget(EventScreens.EventsScreen.EventsScreen(name="EventsScreen"))
        sm.add_widget(EventScreens.EventScreen.EventScreen(name="EventScreen"))
        sm.add_widget(ClientScreens.ContractAgentsScreen.ContractAgentsScreen(name="ContractAgentsScreen"))
        sm.add_widget(ClientScreens.ContractScreen.ContractScreen(name="ContractScreen"))
        sm.add_widget(ClientScreens.ResultScreen.ResultScreen(name="ResultScreen"))
        sm.add_widget(OtherScreens.StockScreen.StockScreen(name="StockScreen"))
        sm.add_widget(TrashScreens.TrashScreen.TrashScreen(name="TrashScreen"))
        sm.add_widget(TrashScreens.TrashCleaningScreen.TrashCleaningScreen(name="TrashCleaningScreen"))
        sm.add_widget(TrashScreens.TrashCleanerScreen.TrashCleanerScreen(name="TrashCleanerScreen"))
        sm.add_widget(TrashScreens.TrashContractScreen.TrashContractScreen(name="TrashContractScreen"))
        sm.add_widget(TrashScreens.TrashResultScreen.TrashResultScreen(name="TrashResultScreen"))

        return sm


if __name__ == "__main__":
    Application().run()
