from importlib.resources import contents
from logging import root
from msilib.schema import Icon
from turtle import home, onscreenclick, title
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen, ScreenManager
from sma_screen_nav import myscreenMg 
from kivymd.uix.expansionpanel import MDExpansionPanel, MDExpansionPanelOneLine
from kivy.uix.gridlayout import GridLayout
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton, MDRaisedButton
from kivymd.toast import toast
from kivymd.uix.bottomsheet import MDGridBottomSheet
from kivy.clock import Clock
from kivymd.uix.boxlayout import BoxLayout
from kivymd.uix.textfield import MDTextField
from kivymd.uix.picker import MDThemePicker
from kivymd.theming import ThemeManager
from kivymd import images_path

Window.size = (300, 580)

class SetPinScreen(Screen): 
    def button_value(self, number):
        prev_number = self.ids.input_box.text

        if prev_number == '':
            self.ids.input_box.text = ''
            self.ids.input_box.text = f"{number}"
        else:
            self.ids.input_box.text = f"{prev_number}{number}"[0:4]

    def remove_last(self):
        prev_number = self.ids.input_box.text
        prev_number = prev_number[:-1]
        self.ids.input_box.text = prev_number

class ReenterSetPinScreen(Screen):
    def button_value2(self, number):
        prev_number = self.ids.input_box2.text

        if prev_number == '':
            self.ids.input_box2.text = ''
            self.ids.input_box2.text = f"{number}"
        else:
            self.ids.input_box2.text = f"{prev_number}{number}"[0:4]

    def remove_last2(self):
        prev_number = self.ids.input_box2.text
        prev_number = prev_number[:-1]
        self.ids.input_box2.text = prev_number
 
    def check_pin(self):
        pinset_1 = SetPinScreen.ids.input_box.text
        pinset_2 = self.ids.input_box2.text

        if pinset_1 == pinset_2:
            self.ids.conf_btn.disabled
        else:
            self.ids.conf_btn.disabled = True
            toast('the two pins did not much consider trying again')


class EnterPinScreen(Screen):
    def button_value3(self, number):
        prev_number = self.ids.input_box3.text

        if prev_number == '':
            self.ids.input_box3.text = ''
            self.ids.input_box3.text = f"{number}"
        else:
            self.ids.input_box3.text = f"{prev_number}{number}"[0:4]

    def remove_last3(self):
        prev_number = self.ids.input_box3.text
        prev_number = prev_number[:-1]
        self.ids.input_box3.text = prev_number
sm = ScreenManager()

class Mycontent(BoxLayout):
    pass

class MainScreen(Screen): 
    pass

class ProfileScreen(Screen):
    pass

class MessagesScreen(Screen):
    pass

class SettingsScreen(Screen):
    pass

class HelpScreen(Screen):
    pass

class ContactScreen(Screen):
    pass

class AboutScreen(Screen): 
    pass

class Content(BoxLayout):
    pass



sm.add_widget(SetPinScreen(name='setpinscreen'))
sm.add_widget(ReenterSetPinScreen(name='reenterpinscreen'))
sm.add_widget(EnterPinScreen(name='enterpinscreen'))
sm.add_widget(MainScreen(name='home'))
sm.add_widget(ProfileScreen(name='profile'))
sm.add_widget(MessagesScreen(name='notification'))
sm.add_widget(SettingsScreen(name='settings'))
sm.add_widget(HelpScreen(name='help'))
sm.add_widget(ContactScreen(name='contact'))
sm.add_widget(AboutScreen(name='about'))

class ShoMaApp(MDApp):
    
    def build(self):
        screen = Builder.load_string(myscreenMg)
        return screen

    #theme_cls = ThemeManager()
    #def on_start(self):
    #    Clock.schedule_once(self.category_content, 5)

    def category_content(self, *kwargs):
        names = ['Vegetables', 'Snacks',]
       
        for name in names:
            #self.root.ids.panel_container.add_widget(
                MDExpansionPanel( 
                    icon='soda.jpg', 
                    content=Mycontent(),
                    panel_cls=MDExpansionPanelOneLine(
                        text=name,
                    )
                )
       #     )

    dialog = None
    def show_simple_dialog(self):
        if not self.dialog:
            self.dialog1 = MDDialog(
            title="Exit This App?",
            text="By clicking Exit you will close this App. Are you sure you want to proceed?",
            auto_dismiss=False,
            buttons=[
                MDRaisedButton(
                    text="Cancel",
                    theme_text_color="Hint", 
                    on_release = self.close_popup_dialogue1, 
                ),
                MDFlatButton(
                    text="Exit",
                    theme_text_color="Hint",
                ),
            ],
        )
        self.dialog1.open()

    def message_dialog_alert(self):
        if not self.dialog:
            self.dialog2 = MDDialog(
            title="Message Notification",
            text="You have 1 unread message",
            auto_dismiss=False,
            buttons=[
                MDFlatButton(
                    text="Cancel",
                    theme_text_color="Custom",
                    text_color=self.theme_cls.primary_color,
                    on_release = self.close_popup_dialogue2, 
                ),
                MDFlatButton(
                    text="See Messages",
                    theme_text_color="Custom",
                    text_color=self.theme_cls.primary_color,
                ),
            ],
        )
        self.dialog2.open()

    def addCategory_dialog_pop(self):
        if not self.dialog:
            self.dialog3 = MDDialog(
            title="Add Category",
            type = 'custom',
            content_cls=Content(),
            auto_dismiss=False,
            buttons=[
                MDFlatButton(
                    text="Cancel",
                    theme_text_color="Custom",
                    text_color=self.theme_cls.primary_color,
                    on_release = self.close_popup_dialogue3,  
                ), 
                MDFlatButton(
                    text="Add Category",
                    theme_text_color="Custom",
                    text_color=self.theme_cls.primary_color,
                ),
            ],
        )
        self.dialog3.open()

    def show_popup(self):
        toast('Profile Updated succesfully')
        pass
    
    def close_popup_dialogue1(self,obj):
        self.dialog1.dismiss()
    def close_popup_dialogue2(self,obj):
        self.dialog2.dismiss()
    def close_popup_dialogue3(self,obj):
        self.dialog3.dismiss()


    def callback_for_menu_items(self, *args):
        toast(args[0])

    def show_share_grid_bottom_sheet(self):
        bottom_sheet_menu = MDGridBottomSheet(
            radius_from='top',
            bg_color= self.theme_cls.primary_color,
            #size_hint_y= None,
            #height= "200dp",
        )
        data = {
            "Facebook": "facebook",
            "Whatsapp": "whatsapp",
            "Twitter": "twitter",
            "Da Cloud": "cloud-upload",
            "Email": "email",
            "Message": "android-messages",
            "Bluetooth": "bluetooth",
        }
        for item in data.items():
            bottom_sheet_menu.add_item(
                item[0],
                lambda x, y=item[0]: self.callback_for_menu_items(y),
                icon_src=item[1],
            )
        bottom_sheet_menu.open()

ShoMaApp().run()