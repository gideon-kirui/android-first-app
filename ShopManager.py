from email import message
from logging import root
from my_screen_manager import my_screen_helper
from kivymd.app import MDApp
from kivymd.uix.expansionpanel import MDExpansionPanel, MDExpansionPanelOneLine
from kivymd.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivymd.uix.button import MDFlatButton, MDRaisedButton
from kivymd.uix.dialog import MDDialog
from kivy.core.window import Window
from kivymd.toast import toast
from kivymd.uix.bottomsheet import MDGridBottomSheet
from kivymd.uix.snackbar import Snackbar
from kivy.properties import StringProperty, BooleanProperty
from kivy.clock import Clock


Window.size = (300, 580)

class Content(BoxLayout):
    pass

class Content2(BoxLayout):
    pass

class Content3(BoxLayout):
    pass

class Mycontent(BoxLayout):
    
    count = 10 
    quantity = StringProperty('10')
    pcntrd = count
    decval = StringProperty('0')
    def stock_reg_snackbar(self):
        self.count -= 1
        self.quantity = str(self.count)
        deduct = self.count / self.pcntrd * 100
        self.decval = str(deduct)
        self.snackbar = Snackbar(
            text="[color=#000000]Your Stock has reduced by " + self.decval + " %",
            bg_color=(1, 1, 1, 1),
            snackbar_animation_dir="Top",
            font_size='16sp',
        )
        self.snackbar.open()
        
class ShopMaApp(MDApp):
    
    def build(self):
        return Builder.load_string(my_screen_helper)
        
    def on_start(self):

        #Clock.schedule_once(self.Navigate_t0_homepage, 5  )

        names = ['Vegetables', 'Sugar', 'Maize Flour', 'Snacks', 'Vegetable oil', 'Wheat Flour', 'Sugar', 'Snacks']
        for name in names:
            self.root.ids.panel_container.add_widget(
                MDExpansionPanel( 
                    icon='soda.jpg',
                    content=Mycontent(), 
                    panel_cls=MDExpansionPanelOneLine(
                        text=name,
                    )
                )
            )


    dialog = None
    def addSubCategory_dialog_pop(self):
        if not self.dialog:
            self.dialog4 = MDDialog(
            title="Add SubCategory",
            type = 'custom',
            content_cls=Content(),
            auto_dismiss=False,
            buttons=[
                MDFlatButton(
                    text="Cancel",
                    theme_text_color="Custom",
                    text_color=self.theme_cls.primary_color,
                    on_release = self.close_popup_dialogue4,  
                ), 
                MDFlatButton(
                    text="Add",
                    theme_text_color="Custom",
                    text_color=self.theme_cls.primary_color,
                ),
            ],
        )
        self.dialog4.open()

    def show_exit_dialog(self):
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
                    on_release = self.on_exit_click,
                ),
            ],
        )
        self.dialog1.open()

    def message_dialog_alert(self):
        self.root.current = 'notification'
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
                    #on_release = self.ids.btmnav
                ),
            ],
        )
        self.dialog2.open()
        
    
    def addCategory_dialog_pop(self):
        if not self.dialog:
            self.dialog3 = MDDialog(
            title="Add Category",
            type = 'custom',
            content_cls=Content2(),
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

    def editCategory_dialog_pop(self):
        if not self.dialog:
            self.dialog5 = MDDialog(
            title="Edit Category",
            type = 'custom',
            content_cls=Content3(),
            auto_dismiss=False,
            buttons=[
                MDFlatButton(
                    text="Cancel",
                    theme_text_color="Custom",
                    text_color=self.theme_cls.primary_color,
                    on_release = self.close_popup_dialogue5,  
                ), 
                MDFlatButton(
                    text="Save",
                    theme_text_color="Custom",
                    text_color=self.theme_cls.primary_color,
                ),
            ],
        )
        self.dialog5.open()

    def close_popup_dialogue1(self,obj):
        self.dialog1.dismiss()
    def close_popup_dialogue4(self,obj):
        self.dialog4.dismiss()
    def close_popup_dialogue2(self,obj):
        self.dialog2.dismiss()
    def close_popup_dialogue3(self,obj):
        self.dialog3.dismiss()
    def close_popup_dialogue5(self,obj):
        self.dialog5.dismiss()

    def callback_for_menu_items(self, *args):
        toast(args[0])

    def show_share_grid_bottom_sheet(self):
        bottom_sheet_menu = MDGridBottomSheet(
            radius_from='top',
            #bg_color= self.theme_cls.primary_color,
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
                lambda x, y='Sorry this functionality is not yet set': self.callback_for_menu_items(y),
                icon_src=item[1],
            )
        bottom_sheet_menu.open()

    def show_popup(self):
        toast('Profile Updated succesfully')
        pass

    def Navigate_t0_homepage(self):
        self.root.current = 'home'

    def on_exit_click(self, obj):
        self.MainApp.stop()
        
ShopMaApp().run()