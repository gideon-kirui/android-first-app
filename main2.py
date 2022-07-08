from turtle import home
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen, ScreenManager
from screen_nav import screen_helper
from kivy.metrics import dp
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from kivymd.uix.datatables import MDDataTable
from kivymd.uix.textfield import MDTextField
from kivymd.uix.boxlayout import MDBoxLayout


Window.size = (300, 580) 

class SetpinScreen(Screen):
    pass

class RenenterScreen(Screen):
    pass

class PinScreen(Screen):
    pass

class HomeScreen(Screen):
    pass

class AddcategoryScreen(Screen):
    pass
class ProfileScreen(Screen):  
    pass

class NotifyScreen(Screen):
    pass

class SettingsScreen(Screen):
    pass

class HelpScreen(Screen):
    pass

class ContactScreen(Screen):
    pass

class AboutScreen(Screen):
    pass

class CattegoryScreen(Screen):
    def on_button_click(self):
        print("button clicked")
        


sm = ScreenManager()
sm.add_widget(SetpinScreen(name='home'))
sm.add_widget(RenenterScreen(name='home'))
sm.add_widget(HomeScreen(name='home'))
sm.add_widget(AddcategoryScreen(name='addcat'))
sm.add_widget(ProfileScreen(name='profile'))
sm.add_widget(NotifyScreen(name='notification'))
sm.add_widget(SettingsScreen(name='settings'))
sm.add_widget(HelpScreen(name='help'))
sm.add_widget(ContactScreen(name='contact'))
sm.add_widget(AboutScreen(name='about'))
sm.add_widget(CattegoryScreen(name='indcat'))
sm.add_widget(PinScreen(name='indcat'))

class SMSApp(MDApp):    

    def build(self):
        screen = Builder.load_string(screen_helper)
        return screen
    
    dialog = None
    def show_simple_dialog(self):
        if not self.dialog:
            self.dialog = MDDialog(
            title="Exit This App?",
            text="By clicking Exit you will close this App. Are you sure you want to proceed?",
            buttons=[
                MDFlatButton(
                    text="Cancel",
                    theme_text_color="Custom",
                     
                ),
                MDFlatButton(
                    text="Exit",
                    theme_text_color="Custom",
                    
                ),
            ],
        )
        self.dialog.open()


SMSApp().run()
