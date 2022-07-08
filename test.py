from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.expansionpanel import MDExpansionPanel, MDExpansionPanelOneLine
from kivymd import images_path

KV = '''
<Content>
    adaptive_height: True
    MDGridLayout:
        cols: 4
        spacing: '10dp'
        size_int: 0.8, None
        adaptive_height: True
        MDLabel:
            text: 'Item'
            size_hint: None, None
            height: self.texture_size[1]
        MDLabel:
            text: 'Qnty'
            size_hint: None, None
            height: self.texture_size[1]
        MDLabel:
            text: 'Action'
            size_hint: None, None
            height: self.texture_size[1]
        MDLabel:
            text: 'Status'
            size_hint: None, None
            height: self.texture_size[1]
        MDLabel:
            text: 'Onions'
            size_hint: None, None
            height: self.texture_size[1]
        MDLabel:
            text: '200 balls'
            size_hint: None, None
            height: self.texture_size[1]
        Button:
            text: 'sell'
            size_hint: None, None
            height: self.texture_size[1]
            
        MDProgressBar:
            value: 50
            orientation: "vertical"
            size_hint_x: None 
            height: '40dp'
        MDLabel:
            text: 'Onions'
            size_hint: None, None
            height: self.texture_size[1]
        MDLabel:
            text: '200 balls'
            size_hint: None, None
            height: self.texture_size[1]
        Button:
            text: 'sell'
            size_hint: None, None
            height: self.texture_size[1]
            
        MDProgressBar:
            value: 50
            orientation: "vertical"
            size_hint_x: None 
            height: '40dp'
        MDLabel:
            text: 'Onions'
            size_hint: None, None
            height: self.texture_size[1]
        MDLabel:
            text: '200 balls'
            size_hint: None, None
            height: self.texture_size[1]
        Button:
            text: 'sell'
            size_hint: None, None
            height: self.texture_size[1]
            
        MDProgressBar:
            value: 50
            orientation: "vertical"
            size_hint_x: None 
            height: '40dp'
        MDLabel:
            text: 'Onions'
            size_hint: None, None
            height: self.texture_size[1]
        MDLabel:
            text: '200 balls'
            size_hint: None, None
            height: self.texture_size[1]
        Button:
            text: 'sell'
            size_hint: None, None
            height: self.texture_size[1]
            
        MDProgressBar:
            value: 50
            orientation: "vertical"
            size_hint_x: None 
            height: '40dp'
ScrollView:
    MDGridLayout:
        id: box
        cols: 1
        adaptive_height: True
'''

class Content(MDBoxLayout):
    '''Custom content.'''
class Test(MDApp):
    def build(self):
        return Builder.load_string(KV)

    def on_start(self):
        for i in range(5):
            self.root.ids.box.add_widget(
                MDExpansionPanel(
                    icon="soda.jpg",
                    content=Content(),
                    panel_cls=MDExpansionPanelOneLine(
                        text="Vegetables",
                    )
                )
            )

Test().run()