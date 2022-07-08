myscreenMg = '''
ScreenManager:
    SetPinScreen:
    ReenterSetPinScreen:
    EnterPinScreen:
    MainScreen:
    ProfileScreen:
    MessagesScreen:
    SettingsScreen:
    HelpScreen:
    ContactScreen:
    AboutScreen:

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

<MainScreen>:
    name: 'home'
    id: homepage
    Screen:
        MDNavigationLayout:
            ScreenManager:
                Screen:
                    BoxLayout:
                        orientation: 'vertical'
                        MDToolbar:
                            title: 'Categories'
                            #md_bg_color: app.theme_cls.custom_color
                            left_action_items: [["menu", lambda x: nav_drawer.set_state("open")]]
                            right_action_items: [["magnify"], ["dots-vertical", lambda x: nav_ldrawer.set_state("open")]]
                        BoxLayout:
                            ScrollView:
                                MDGridLayout:
                                    id: panel_container 
                                    cols: 1
                                    size_hint_y: None
                                    height: self.minimum_height                
                                    widget: app.category_content()

                    MDBottomAppBar:
                        MDToolbar:
                            left_action_items: [["message", lambda x: app.message_dialog_alert()]]
                            type: 'bottom'
                            mode: 'free-end'
                            icon: 'plus'
                            on_action_button: app.addCategory_dialog_pop()

            MDNavigationDrawer:
                id: nav_drawer
                size_hint: (0.7, 0.6)
                pos_hint: {'center_y':0.59}
                BoxLayout:
                    orientation: 'vertical'
                    spacing: '5dp'
                    Image:
                        source: 'user.png'
                        size_hint: (0.5, 0.5)
                        pos_hint: {'center_x':0.5, 'center_y':0.05}

                    MDLabel:
                        text: 'Shoma'
                        size_hint_y: None
                        font_size: 27
                        height: self.texture_size[1]
                        size_hint_x: None
                        height: self.texture_size[1]
                        pos_hint: {'center_x':0.5, 'center_y':0.2}

                    ScrollView:
                        MDList:
                            OneLineIconListItem:
                                text: 'Edit Profile'
                                on_press: root.manager.current = 'profile'
                                IconLeftWidget:
                                    icon: 'account'
                            OneLineIconListItem:
                                text: 'Messages  +10'
                                on_press: root.manager.current = 'notification'
                                IconLeftWidget:
                                    icon: 'message-alert-outline'
                            OneLineIconListItem:
                                text: 'Settings'
                                on_press: root.manager.current = 'settings'
                                IconLeftWidget:
                                    icon: 'tools'
                            OneLineIconListItem:
                                text: 'Exit'
                                on_press: app.show_simple_dialog()
                                IconLeftWidget:
                                    icon: 'logout'

            MDNavigationDrawer:
                id: nav_ldrawer
                anchor: 'right'
                size_hint: (0.7, 0.5)
                pos_hint: {'center_y':0.64}
                BoxLayout:
                    md_bg_color: 'dark'
                    orientation: 'vertical'
                    ScrollView:
                        MDList:
                            OneLineIconListItem:
                                text: 'Help'
                                on_press: root.manager.current = 'help'
                                IconLeftWidget:
                                    icon: 'chat-question'
                            OneLineIconListItem:
                                text: 'Feedback'
                                IconLeftWidget:
                                    icon: 'chat'
                            OneLineIconListItem:
                                text: 'Contact Us'
                                on_press: root.manager.current = 'contact'
                                IconLeftWidget:
                                    icon: 'phone'
                            OneLineIconListItem:
                                text: 'About Us'
                                on_press: root.manager.current = 'about'
                                IconLeftWidget:
                                    icon: 'history'
                            OneLineIconListItem:
                                text: 'Rate Us'
                                IconLeftWidget:
                                    icon: 'star'
                            OneLineIconListItem:
                                text: 'More Apps'
                                IconLeftWidget:
                                    icon: 'apps'
                            OneLineIconListItem:
                                text: 'Share App'
                                on_release: app.show_share_grid_bottom_sheet()
                                IconLeftWidget:
                                    icon: 'share-variant-outline'
                 
                        
<ProfileScreen>:
    name: 'profile'
    Screen:
        MDNavigationLayout:
            ScreenManager:
                Screen: 
                    BoxLayout:
                        orientation: 'vertical'
                        MDToolbar:
                            title: 'My Profile'
                            left_action_items: [["arrow-left", lambda x: root.manager.current(notification)]]
                            right_action_items: [["pencil-box-multiple-outline"]]
                        
                        BoxLayout:
                            orientation: 'vertical'
                            spacing: '5dp'
                            Image:
                                source: 'user.png'
                                size_hint: .5, .5
                                pos_hint: {'center_x':0.5}

                            MDTextField:
                                hint_text: "Gideon"
                                size_hint_x: 0.7
                                pos_hint: {'center_x':0.5}
                                icon_right: 'account'
                                #icon_right: 'pencil-box-multiple-outline'
                        
                            MDTextField:
                                hint_text: "Email"
                                size_hint_x: 0.7
                                pos_hint: {'center_x':0.5}
                                icon_right: 'email'
                        
                            MDTextField:
                                hint_text: "Contact"
                                size_hint_x: 0.7
                                pos_hint: {'center_x':0.5}
                                icon_right: 'phone'
                        
                            MDTextField:
                                hint_text: "Business Position"
                                size_hint_x: 0.7
                                pos_hint: {'center_x':0.5}
                                icon_right: 'account-check'
                        
                            MDTextField:
                                hint_text: "Business Name"
                                size_hint_x: 0.7
                                pos_hint: {'center_x':0.5}
                                icon_right: 'google-my-business'

                            Button:
                                text: 'Save Changes'
                                size_hint_y: 0.08
                                size_hint_x: 0.5
                                pos_hint: {'center_x':0.5}
                                background_color: (100/255, 222/255, 24/255)
                                color: 'teal'
                                on_release: app.show_popup()

<MessagesScreen>                
    name: 'notification'
    Screen:
        MDNavigationLayout:
            ScreenManager:
                Screen: 
                    BoxLayout:
                        orientation: 'vertical'
                        MDToolbar:
                            title: 'Messages'
                            left_action_items: [["arrow-left"]]
                            right_action_items: [["magnify"], ["dots-vertical"]]
                        Widget:
                        
                    

<SettingsScreen>:
    name: 'settings'
    Screen:
        MDNavigationLayout:
            ScreenManager:
                Screen: 
                    BoxLayout:
                        orientation: 'vertical'
                        MDToolbar:
                            title: 'Settings'
                            left_action_items: [["arrow-left"]]
                            right_action_items: [["dots-vertical"]]

                        BoxLayout:
                            orientation: 'vertical'
                            spacing: '10dp'
                            ScrollView:
                                MDList:
                                    spacing: '10dp'
                                    OneLineIconListItem:
                                        padding: '5dp'
                                        text: 'Edit Acount'
                                        on_press: root.manager.current = 'profile'
                                        IconLeftWidget:
                                            icon: 'account'
                                    OneLineIconListItem:
                                        text: 'Change Theme'
                                        on_release: app.show_themepicker()
                                        IconLeftWidget:
                                            icon: 'theme-light-dark'
                                    OneLineIconListItem:
                                        text: 'Change Pin'
                                        IconLeftWidget:
                                            icon: 'shield-key'
                                    OneLineIconListItem:
                                        text: 'Change ProgressBar'
                                        IconLeftWidget:
                                            icon: 'progress-check'
                                    OneLineIconListItem:
                                        text: 'Customize Toolbar'
                                        IconLeftWidget:
                                            icon: 'tooltip-account'
                                    OneLineIconListItem:
                                        text: 'Customize Pinscreen'
                                        IconLeftWidget:
                                            icon: 'fullscreen'
                                    OneLineIconListItem:
                                        text: 'Creat Buckup '
                                        IconLeftWidget:
                                            icon: 'google-drive'
                                    OneLineIconListItem:
                                        text: 'Allow Notifications'
                                        IconLeftWidget:
                                            icon: 'bell-outline'
                                    OneLineIconListItem:
                                        text: 'Customize Categories Page'
                                        color: 'grey'
                                        IconLeftWidget:
                                            icon: 'shopping'
                            MDLabel:
                                text: 'myappsdevs@2022'
                                size_hint_y: 0.05
                                pos_hint: {'center_x':0.5, 'center_y':0.5}
                                size_hint_x: 0.5
                                halign: 'center'
                                color: 'lime'
                                font_style: 'Overline'        

<HelpScreen>:
    name: 'help'
    Screen:
        MDNavigationLayout:
            ScreenManager:
                Screen: 
                    BoxLayout:
                        orientation: 'vertical'
                        MDToolbar:
                            title: 'Help'
                            left_action_items: [["arrow-left"]]
                            right_action_items: [["magnify"], ["dots-vertical"]]

                        BoxLayout:
                            orientation: 'vertical'
                            ScrollView:
                                MDList:
                                    OneLineListItem:
                                        text: 'How To Get Started?'
                                        color: 'gray'
                                        font_style: 'Caption'
                                        
                                    OneLineListItem:
                                        text: 'How To Add Category?'
                                        color: 'gray'
                                        font_style: 'Caption'
                                        
                                    OneLineListItem:
                                        text: 'How Does The App Work?'
                                        color: 'gray'
                                        font_style: 'Caption'
                                        
                                    OneLineListItem:
                                        text: 'What if I loose My phone can I find my data?'
                                        color: 'gray'
                                        font_style: 'Caption'
                                        
                                    OneLineListItem:
                                        text: 'contact the designers of this App?'
                                        on_press: root.manager.current = 'contact'
                                        color: 'gray'
                                        font_style: 'Caption'
                                         
                                    OneLineListItem:
                                        text: 'Who are the users of this App?'
                                        color: 'gray'
                                        font_style: 'Caption'
                                
                                    OneLineListItem:
                                        text: 'What are the benefits of using this app?'
                                        color: 'gray'
                                        font_style: 'Caption'
                                    
                                    OneLineListItem:
                                        text: 'How can I log in using my google accoungt?'
                                        color: 'gray'
                                        font_style: 'Caption'

                                    OneLineListItem:
                                        text: 'Can this app realize increse or decrease of stock?'
                                        color: 'gray'
                                        font_style: 'Caption'

                                    OneLineListItem:
                                        text: 'How Can I know there is a decrease in stock?'
                                        color: 'gray'
                                        font_style: 'Caption'

<ContactScreen>:
    name: 'contact'
    Screen:
        MDNavigationLayout:
            ScreenManager:
                Screen: 
                    BoxLayout:
                        orientation: 'vertical'
                        MDToolbar:
                            title: 'Contact Us'
                            left_action_items: [["arrow-left"]]
                            right_action_items: [["magnify"], ["dots-vertical"]]

                        BoxLayout:
                            orientation: 'vertical'
                            GridLayout:
                                cols: 1
                                ScrollView:
                                    MDList:
                                        OneLineIconListItem:
                                            text: '0712345678'
                                            color: 'gray'
                                            font_style: 'Caption'
                                            IconLeftWidget:
                                                icon: 'phone'
                                        OneLineIconListItem:
                                            text: 'www.myappweb.com'
                                            color: 'gray'
                                            font_style: 'Caption'
                                            IconLeftWidget:
                                                icon: 'web'
                                        OneLineIconListItem:
                                            text: 'P.O.Box 6-600'
                                            color: 'gray'
                                            font_style: 'Caption'
                                            IconLeftWidget:
                                                icon: 'home-account'
                                        OneLineIconListItem:
                                            text: 'Embu - Kenya'
                                            color: 'gray'
                                            font_style: 'Caption'
                                            IconLeftWidget:
                                                icon: 'map-marker-radius-outline'
                                        OneLineIconListItem:
                                            text: 'MyAppFAcount'
                                            color: 'gray'
                                            font_style: 'Caption'
                                            IconLeftWidget:
                                                icon: 'facebook'
                                        OneLineIconListItem:
                                            text: 'MyApp@Twitter'
                                            color: 'gray'
                                            font_style: 'Caption'
                                            IconLeftWidget:
                                                icon: 'twitter'
                                        OneLineIconListItem:
                                            text: 'myapp@gmail.com'
                                            color: 'gray'
                                            font_style: 'Caption'
                                            IconLeftWidget:
                                                icon: 'email'
                                        OneLineIconListItem:
                                            text: 'MyAppdevs@linkedin'
                                            color: 'gray'
                                            font_style: 'Caption'
                                            IconLeftWidget:
                                                icon: 'linkedin'
                                        OneLineIconListItem:
                                            text: 'myappdevs.github.com'
                                            color: 'gray'
                                            font_style: 'Caption'
                                            IconLeftWidget:
                                                icon: 'github'

                                MDLabel:
                                    text: 'myappsdevs@2022'
                                    size_hint_y: None
                                    valign: 'center'
                                    size_hint_x: 0.5
                                    halign: 'center'
                                    color: 'lime'
                                    font_style: 'Overline'

<AboutScreen>:
    name: 'about'
    Screen:
        MDNavigationLayout:
            ScreenManager:
                Screen: 
                    BoxLayout:
                        orientation: 'vertical'
                        MDToolbar:
                            title: 'About Us'
                            left_action_items: [["arrow-left"]] 

                        BoxLayout:
                            ScrollView:
                                GridLayout:
                                    padding: '10dp'
                                    spacing: '10dp'
                                    cols: 1
                                    size_hint: 1, None
                                    height: self.minimum_size[1]
                                    MDCard:
                                        orientation: 'vertical'
                                        size_hint: 0.8, None
                                        height: self.minimum_size[1]
                                        radius: [50, ]
                                        spacing: '5dp'
                                        padding: '5dp'
                                        Image:
                                            source: 'user.png'
                                            size_hint: 0.5, None
                                            height: self.texture_size[1]
                                            pos_hint: {'center_x':0.5}
                                        MDLabel:
                                            text: 'Trizer Kwamboka'
                                            color: 'red'
                                            font_style: 'H6'
                                            size_hint_y: None
                                            height: self.texture_size[1]
                                            size_hint_x: 0.7
                                            pos_hint: {'center_x':0.5}
                                            

                                        MDLabel:
                                            text: 'University of Embu'
                                            color: 'gray'
                                            font_style: 'Caption'
                                            size_hint_y: None
                                            height: self.texture_size[1]
                                            size_hint_x: 0.5
                                            pos_hint: {'center_x':0.5}

                                        MDLabel:
                                            text: '0712345678'
                                            color: 'gray'
                                            font_style: 'Caption'
                                            size_hint_y: None
                                            height: self.texture_size[1]
                                            size_hint_x: 0.5
                                            pos_hint: {'center_x':0.5}

                                        MDLabel: 
                                            text: 'BSc. Information Tech'
                                            color: 'gray'
                                            font_style: 'Caption'
                                            size_hint_y: None
                                            height: self.texture_size[1]
                                            size_hint_x: 0.5
                                            pos_hint: {'center_x':0.5}
                                    MDCard:
                                        orientation: 'vertical'
                                        size_hint: 0.8, None
                                        height: self.minimum_size[1]
                                        radius: [50, ]
                                        spacing: '5dp'
                                        padding: '10dp'
                                        Image:
                                            source: 'user.png'
                                            size_hint: 0.5, None
                                            height: self.texture_size[1]
                                            pos_hint: {'center_x':0.5}
                                        MDLabel:
                                            text: 'Gideon Kirui'
                                            color: 'red'
                                            font_style: 'H6'
                                            size_hint_y: None
                                            height: self.texture_size[1]
                                            size_hint_x: 0.5
                                            pos_hint: {'center_x':0.5}
                                            

                                        MDLabel:
                                            text: 'University of Embu'
                                            color: 'gray'
                                            font_style: 'Caption'
                                            size_hint_y: None
                                            height: self.texture_size[1]
                                            size_hint_x: 0.5
                                            pos_hint: {'center_x':0.5}

                                        MDLabel:
                                            text: '0712345678'
                                            color: 'gray'
                                            font_style: 'Caption'
                                            size_hint_y: None
                                            height: self.texture_size[1]
                                            size_hint_x: 0.5
                                            pos_hint: {'center_x':0.5}

                                        MDLabel: 
                                            text: 'BSc. Information Tech'
                                            color: 'gray'
                                            font_style: 'Caption'
                                            size_hint_y: None
                                            height: self.texture_size[1]
                                            size_hint_x: 0.5
                                            pos_hint: {'center_x':0.5}

                                    MDCard:
                                        orientation: 'vertical'
                                        size_hint: 0.8, None
                                        height: self.minimum_size[1]
                                        radius: [50, ]
                                        spacing: '5dp'
                                        padding: '10dp'
                                        Image:
                                            source: 'user.png'
                                            size_hint: 0.5, None
                                            height: self.texture_size[1]
                                            pos_hint: {'center_x':0.5}
                                        MDLabel:
                                            text: 'Summy '
                                            color: 'red'
                                            font_style: 'H6'
                                            size_hint_y: None
                                            height: self.texture_size[1]
                                            size_hint_x: 0.5
                                            pos_hint: {'center_x':0.5}
                                            

                                        MDLabel:
                                            text: 'University of Embu'
                                            color: 'gray'
                                            font_style: 'Caption'
                                            size_hint_y: None
                                            height: self.texture_size[1]
                                            size_hint_x: 0.5
                                            pos_hint: {'center_x':0.5}

                                        MDLabel:
                                            text: '0712345678'
                                            color: 'gray'
                                            font_style: 'Caption'
                                            size_hint_y: None
                                            height: self.texture_size[1]
                                            size_hint_x: 0.5
                                            pos_hint: {'center_x':0.5}

                                        MDLabel: 
                                            text: 'BSc. Information Tech'
                                            color: 'gray'
                                            font_style: 'Caption'
                                            size_hint_y: None
                                            height: self.texture_size[1]
                                            size_hint_x: 0.5
                                            pos_hint: {'center_x':0.5}  

<Content>
    orientation: "vertical"
    spacing: "10dp"
    size_hint_y: None
    height: "60dp"
    MDTextField:
        hint_text: "Enter Category name"

<Mycontent>
    size_hint: 1, None
    #height: self.minimum_height
    adaptive_height: True
    orientation: 'vertical'
    MDGridLayout:
        cols: 3
        spacing: '10dp'
        size_int: 1, 1
        #pos_hint: {'center_x':0.5}
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
                    height: self.texture_size[1]
                Button:
                    text: 'sell'
                    size_hint: None, None
                    height: self.texture_size[1]
                Button:
                    text: 'sell'
                    size_hint: None, None
                    height: self.texture_size[1]      

    MDFloatingActionButton:
        id: button
        icon: "plus"
        pos_hint: {'center_x':0.9,'center_y':1}
        target_radius: '25dp'
        #on_release: app.tap_target_start()


    
'''             
