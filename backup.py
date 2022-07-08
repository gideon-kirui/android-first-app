KV='''
<SetPinScreen>:
    name: 'setpinscreen'
    AnchorLayout:
        size_hint: (0.82, 0.6)
        pos_hint: {'center_x':0.5, 'center_y':0.5}
        
        BoxLayout:
            orientation: 'vertical'
            padding: '20dp'
            spacing: '10dp'
        
            MDLabel:
                text: 'Set up your pin'
                halign: 'center'
                size_hint_y: None
                height: self.texture_size[1]
                font_style: 'H5' 
                color: 'teal'

            TextInput:
                id: input_box
                text: ''
                background_normal: ''
                background_color: 'white'
                outline: None
                multiline: False
                halign: 'center'
                size_hint: (0.7,0.12)
                pos_hint: {'center_x':0.5, 'center_y':0.2}

            GridLayout:
                cols: 3
                rows: 4
                spacing: '5dp'
                Button:
                    text: '1'
                    size_hint: (0.2,0.1)
                    background_normal: ''
                    background_color: 'white' #(117/255, 227/255, 247/255)
                    color: 'black'
                    on_press: root.button_value(1)

                Button:
                    text: '2'
                    size_hint: (0.2,0.1)
                    background_normal: ''
                    background_color: 'white' #(117/255, 227/255, 247/255)
                    color: 'black'
                    on_press: root.button_value(2)

                Button:
                    text: '3'
                    size_hint: (0.2,0.1)
                    background_normal: ''
                    background_color: 'white' #(117/255, 227/255, 247/255)
                    color: 'black'
                    on_press: root.button_value(3)

                Button:
                    text: '4'
                    size_hint: (0.2,0.1)
                    background_normal: ''
                    background_color: 'white' #(117/255, 227/255, 247/255)
                    color: 'black'
                    on_press: root.button_value(4)

                Button:
                    text: '5'
                    size_hint: (0.2,0.1)
                    background_normal: ''
                    background_color: 'white' #(117/255, 227/255, 247/255)
                    color: 'black'
                    on_press: root.button_value(5)

                Button:
                    text: '6'
                    size_hint: (0.2,0.1)
                    background_normal: ''
                    background_color: 'white' #(117/255, 227/255, 247/255)
                    color: 'black'
                    on_press: root.button_value(6)

                Button:
                    text: '7'
                    size_hint: (0.2,0.1)
                    background_normal: ''
                    background_color: 'white' #(117/255, 227/255, 247/255)
                    color: 'black'
                    on_press: root.button_value(7)

                Button:
                    text: '8'
                    size_hint: (0.2,0.1)
                    background_normal: ''
                    background_color: 'white' #(117/255, 227/255, 247/255)
                    color: 'black'
                    on_press: root.button_value(8)

                Button:
                    text: '9'
                    size_hint: (0.2,0.1)
                    background_normal: ''
                    background_color: 'white' #(117/255, 227/255, 247/255)
                    color: 'black'
                    on_press: root.button_value(9)

                Button:
                    text: 'Ok'
                    on_press: root.manager.current = 'reenterpinscreen'
                    size_hint: (0.2,0.1)
                    background_normal: ''
                    background_color: 'white' #(255/255, 201/255, 121/255)
                    color: 'gray'
                    font_size: 16
                Button:
                    text: '0'
                    size_hint: (0.2,0.1)
                    background_normal: ''
                    background_color: 'white' #(117/255, 227/255, 247/255)
                    color: 'black'
                    on_press: root.button_value(0)

                Button:
                    text: '\u00AB'
                    size_hint: (0.2,0.1)
                    background_normal: ''
                    background_color: 'white' #(255/255, 201/255, 121/255)
                    color: 'gray'
                    font_size: 16
                    on_press: root.remove_last()


<ReenterSetPinScreen>:
    name: 'reenterpinscreen'
    AnchorLayout:
        size_hint: (0.8, 0.6)
        pos_hint: {'center_x':0.5, 'center_y':0.5}
        
        BoxLayout:
            orientation: 'vertical'
            padding: '20dp'
            spacing: '10dp'
            MDLabel:
                text: 'Confirm your pin'
                halign: 'center'
                size_hint_y: None
                height: self.texture_size[1]
                font_style: 'H5' 
                color: 'violet'

            TextInput:
                id: input_box2
                text: ''
                background_normal: ''
                background_color: 'white'
                multiline: False
                halign: 'center'
                size_hint: (0.7,0.12)
                pos_hint: {'center_x':0.5, 'center_y':0.2}
                on_focus: root.check_pin
            GridLayout:
                cols: 3
                rows: 4
                spacing: '5dp'
                Button:
                    text: '1'
                    size_hint: (0.2,0.1)
                    background_normal: ''
                    background_color: 'white' # (255/255, 201/255, 121/255)
                    color: 'blue'
                    on_press: root.button_value2(1) 

                Button:
                    text: '2'
                    size_hint: (0.2,0.1)
                    background_normal: ''
                    background_color: 'white' # (255/255, 201/255, 121/255)
                    color: 'blue'
                    on_press: root.button_value2(2)

                Button:
                    text: '3'
                    size_hint: (0.2,0.1)
                    background_normal: ''
                    background_color: 'white' # (255/255, 201/255, 121/255)
                    color: 'blue'
                    on_press: root.button_value2(3)
                    

                Button:
                    text: '4'
                    size_hint: (0.2,0.1)
                    background_normal: ''
                    background_color: 'white' # (255/255, 201/255, 121/255)
                    color: 'blue'
                    on_press: root.button_value2(4)

                Button:
                    text: '5'
                    size_hint: (0.2,0.1)
                    background_normal: ''
                    background_color: 'white' # (255/255, 201/255, 121/255)
                    color: 'blue'
                    on_press: root.button_value2(5)

                Button:
                    text: '6'
                    size_hint: (0.2,0.1)
                    background_normal: ''
                    background_color: 'white' # (255/255, 201/255, 121/255)
                    color: 'blue'
                    on_press: root.button_value2(6)

                Button:
                    text: '7'
                    size_hint: (0.2,0.1)
                    background_normal: ''
                    background_color: 'white' # (255/255, 201/255, 121/255)
                    color: 'blue'
                    on_press: root.button_value2(7)

                Button:
                    text: '8'
                    size_hint: (0.2,0.1)
                    background_normal: ''
                    background_color: 'white' # (255/255, 201/255, 121/255)
                    color: 'blue'
                    on_press: root.button_value2(8)

                Button:
                    text: '9'
                    size_hint: (0.2,0.1)
                    background_normal: ''
                    background_color: 'white' # (255/255, 201/255, 121/255)
                    color: 'blue'
                    on_press: root.button_value2(9)

                Button:
                    id: conf_btn
                    text: 'Ok'
                    on_press: root.manager.current = 'enterpin'
                    size_hint: (0.2,0.1)
                    background_normal: ''
                    background_color: 'white' # (117/255, 227/255, 247/255)
                    color: 'black'
                    font_size: 16
                    disabled: False

                Button:
                    text: '0'
                    size_hint: (0.2,0.1)
                    background_normal: ''
                    background_color: 'white' # (255/255, 201/255, 121/255)
                    color: 'blue'
                    on_press: root.button_value2(0)

                Button:
                    text: '\u00AB'
                    size_hint: (0.2,0.1)
                    background_normal: ''
                    background_color: 'white' # (117/255, 227/255, 247/255)
                    color: 'black'
                    font_size: 16
                    on_press: root.remove_last2()

<EnterPinScreen>:
    name: 'enterpin'
    AnchorLayout:
        size_hint: (0.9, 0.7)
        pos_hint: {'center_x':0.5, 'center_y':0.5}
        
        BoxLayout:
            orientation: 'vertical'
            padding: '20dp'
            spacing: '10dp'
            Image:
                source: 'avata-user.jpg'
                size_hint: .5, .5
                pos_hint: {'center_x':0.5}
            
            MDLabel:
                text: 'Hi Shoma, Welcome back'
                halign: 'center'
                size_hint_y: None
                height: self.texture_size[1]
                font_style: 'H6' 
                color: 'green'

            MDLabel:
                text: 'Please Enter Pin'
                halign: 'center'
                size_hint_y: None
                height: self.texture_size[1]
                font_style: 'H5' 
                color: 'violet'

            TextInput:
                id: input_box3
                text: ''
                background_normal: ''
                background_color: 'white'
                multiline: False
                halign: 'center'
                size_hint: (0.5,0.2)
                pos_hint: {'center_x':0.5, 'center_y':0.2}

            GridLayout:
                cols: 3
                rows: 4
                spacing: '5dp'
                Button:
                    text: '1'
                    size_hint: (0.3,0.2)
                    background_normal: ''
                    background_color: 'white' #(255/255, 201/255, 121/255)
                    color: 'blue'
                    font_size: 16
                    on_press: root.button_value3(1)
                     

                Button:
                    text: '2'
                    size_hint: (0.3,0.2)
                    background_normal: ''
                    background_color: 'white' #(255/255, 201/255, 121/255)
                    color: 'blue'
                    font_size: 16
                    on_press: root.button_value3(2)      


                Button:
                    text: '3'
                    size_hint: (0.3,0.2)
                    background_normal: ''
                    background_color: 'white' #(255/255, 201/255, 121/255)
                    color: 'blue'
                    font_size: 16
                    on_press: root.button_value3(3)
                    
                    

                Button:
                    text: '4'
                    size_hint: (0.3,0.2)
                    background_normal: ''
                    background_color: 'white' #(255/255, 201/255, 121/255)
                    color: 'blue'
                    font_size: 16
                    on_press: root.button_value3(4)
                    

                Button:
                    text: '5'
                    size_hint: (0.3,0.2)
                    background_normal: ''
                    background_color: 'white' #(255/255, 201/255, 121/255)
                    color: 'blue'
                    font_size: 16
                    on_press: root.button_value3(5)
                    

                Button:
                    text: '6'
                    size_hint: (0.3,0.2)
                    background_normal: ''
                    background_color: 'white' #(255/255, 201/255, 121/255)
                    color: 'blue'
                    font_size: 16
                    on_press: root.button_value3(6)
                    

                Button:
                    text: '7'
                    size_hint: (0.3,0.2)
                    background_normal: ''
                    background_color: 'white' #(255/255, 201/255, 121/255)
                    color: 'blue'
                    font_size: 16
                    on_press: root.button_value3(7)
                    

                Button:
                    text: '8'
                    size_hint: (0.3,0.2)
                    background_normal: ''
                    background_color: 'white' #(255/255, 201/255, 121/255)
                    color: 'blue'
                    font_size: 16
                    on_press: root.button_value3(8)
                    

                Button:
                    text: '9'
                    size_hint: (0.3,0.2)
                    background_normal: ''
                    background_color: 'white' #(255/255, 201/255, 121/255)
                    color: 'blue'
                    font_size: 16
                    on_press: root.button_value3(9)
                    

                Button:
                    text: 'Ok'
                    on_press: root.manager.current = 'home'
                    size_hint: (0.3,0.2)
                    background_normal: ''
                    background_color: 'white' #(117/255, 227/255, 247/255)
                    color: 'black'
                    font_size: 16

                Button:
                    text: '0'
                    size_hint: (0.3,0.2)
                    background_normal: ''
                    background_color: 'white' #(255/255, 201/255, 121/255)
                    color: 'blue'
                    font_size: 16
                    on_press: root.button_value3(0)
                    

                Button:
                    text: '\u00AB'
                    size_hint: (0.3,0.2)
                    background_normal: ''
                    background_color: 'white' #(117/255, 227/255, 247/255)
                    color: 'black'
                    font_size: 16
                    on_press: root.remove_la
#####################################################################
               #MDBottomAppBar:
                        #    MDToolbar:
                        #        left_action_items: [["message", lambda x: app.message_dialog_alert()]]
                        #        type: 'bottom'
                        #        mode: 'free-end'
                        #        icon: 'plus'
                        #        on_action_button: app.addCategory_dialog_pop()

###########################################################################################################
MDBoxLayout:
                orientaion: 'vertical'
                MDGridLayout:
                    cols: 1
                    spacing: '10dp'
                    MDLabel:
                        text: 'Item'
                        size_hint: None, None
                        height: self.texture_size[1]

                    MDLabel:
                        text: 'Onions'
                        size_hint: None, None
                        height: self.texture_size[1]

                    MDLabel:
                        text: 'Onions'
                        size_hint: None, None
                        height: self.texture_size[1]

                    MDLabel:
                        text: 'Onions'
                        size_hint: None, None
                        height: self.texture_size[1]
                    
                    MDLabel:
                        text: 'Onions'
                        size_hint: None, None
                        height: self.texture_size[1]
                    
                    MDLabel:
                        text: 'Onions'
                        size_hint: None, None
                        height: self.texture_size[1]

                    MDLabel:
                        text: 'Onions'
                        size_hint: None, None
                        height: self.texture_size[1]

            MDBoxLayout:
                orientaion: 'vertical'
                MDGridLayout:
                    cols: 1
                    spacing: '10dp'
                    MDLabel:
                        text: 'Qnty'
                        size_hint: None, None
                        height: self.texture_size[1]

                    MDLabel:
                        text: '200 balls'
                        size_hint: None, None
                        height: self.texture_size[1]
                    MDLabel:
                        text: '200 balls'
                        size_hint: None, None
                        height: self.texture_size[1]
                    MDLabel:
                        text: '200 balls'
                        size_hint: None, None
                        height: self.texture_size[1]
                    MDLabel:
                        text: '200 balls'
                        size_hint: None, None
                        height: self.texture_size[1]

                    MDLabel:
                        text: '200 balls'
                        size_hint: None, None
                        height: self.texture_size[1]

                    MDLabel:
                        text: '200 balls'
                        size_hint: None, None
                        height: self.texture_size[1]

            MDBoxLayout:
                orientation: 'vertical'
                MDGridLayout:
                    cols: 1
                    spacing: '10dp'
                    MDLabel:
                        text: 'Action'
                        size_hint: None, None
                        height: self.texture_size[1]

                    Button:
                        text: 'sell'
                        on_release: root.ids.banner.show()
                        size_hint: None, None
                        height: self.texture_size[1]
                    Button:
                        text: 'sell'
                        size_hint: None, None
                        height: self.texture_size[1]
                    Button:
                        text: 'sell'
                        size_hint: None, None
                        height: self.texture_size[1]
                    Button:
                        text: 'sell'
                        size_hint: None, None
                        on_release: 
                        height: self.texture_size[1]
                    Button:
                        text: 'sell'
                        size_hint: None, None
                        height: self.texture_size[1]
                    Button:
                        text: 'sell'
                        size_hint: None, None
                        height: self.texture_size[1]      

'''