screen_helper = '''
ScreenManager:
    SetpinScreen
    RenenterScreen
    PinScreen:
    HomeScreen:
    CattegoryScreen:
    ProfileScreen:
    NotifyScreen:
    SettingsScreen:
    HelpScreen:
    ContactScreen:
    AboutScreen:
    AddcategoryScreen:

<SetpinScreen>:
    name: 'setpin'
    AnchorLayout:
        anchor_y: "center"
        anchor_x: "center"
        BoxLayout:
            orientation: 'vertical'
            size_hint: .9, .4
            spacing: '10dp'
            MDTextField:
                hint_text: 'Set your Pin'
                size_hint: (0.5,0.25)
                pos_hint: {'center_x':0.5, 'center_y':0.2}
                
             
            GridLayout:
                cols: 3
                rows: 4
                pos_hint: {'center_x':0.5}
                size_hint: .5, .6
                spacing: '10dp'
                Button:
                    text: '1'
                    size_hint: (0.5,0.3)
                    background_color: (1, 1, 1, 1)
                Button:
                    text: '2'
                    size_hint: (0.5,0.3)
                Button:
                    text: '3'
                    size_hint: (0.5,0.3)
                Button:
                    text: '4'
                    size_hint: (0.5,0.3)
                Button:
                    text: '5'
                    size_hint: (0.5,0.3)
                Button:
                    text: '6'
                    size_hint: (0.5,0.3)
                Button:
                    text: '7'
                    size_hint: (0.5,0.3)
                Button:
                    text: '8'
                    size_hint: (0.5,0.3)
                Button:
                    text: '9'
                    size_hint: (0.5,0.3)
                Button:
                    text: ''
                    size_hint: (0.5,0.3)
                Button:
                    text: '0'
                    size_hint: (0.5,0.3)
                Button:
                    text: u'\u00AB'
                    size_hint: (0.5,0.3)

            Button:
                text: 'Ok'
                on_press: root.manager.current = 'reenterpin'
                size_hint: (0.25,0.1)
                pos_hint: {'center_x':0.5, 'center_y':.9}

<RenenterScreen>:
    name: 'reenterpin'
    AnchorLayout:
        anchor_y: "center"
        anchor_y: "center"
        BoxLayout:
            orientation: 'vertical'
            size_hint: .9, .4
            spacing: '10dp'
            MDTextField:
                hint_text: 'Renter set Pin'
                size_hint: (0.5,0.25)
                pos_hint: {'center_x':0.5, 'center_y':0.2}
                
             
            GridLayout:
                cols: 3
                rows: 4
                pos_hint: {'center_x':0.5}
                size_hint: .5, .6
                spacing: '10dp'
                Button:
                    text: '1'
                    size_hint: (0.5,0.3)
                    background_color: (1, 1, 1, 1)
                Button:
                    text: '2'
                    size_hint: (0.5,0.3)
                Button:
                    text: '3'
                    size_hint: (0.5,0.3)
                Button:
                    text: '4'
                    size_hint: (0.5,0.3)
                Button:
                    text: '5'
                    size_hint: (0.5,0.3)
                Button:
                    text: '6'
                    size_hint: (0.5,0.3)
                Button:
                    text: '7'
                    size_hint: (0.5,0.3)
                Button:
                    text: '8'
                    size_hint: (0.5,0.3)
                Button:
                    text: '9'
                    size_hint: (0.5,0.3)
                Button:
                    text: ''
                    size_hint: (0.5,0.3)
                Button:
                    text: '0'
                    size_hint: (0.5,0.3)
                Button:
                    text: u'\u00AB'
                    size_hint: (0.5,0.3)

            Button:
                text: 'Ok'
                on_press: root.manager.current = 'pin'
                size_hint: (0.25,0.1)
                pos_hint: {'center_x':0.5, 'center_y':.9}


<PinScreen>:
    name: 'pin'
    AnchorLayout:
        anchor_y: "center"
        anchor_y: "center"
        BoxLayout:
            orientation: 'vertical'
            size_hint: .8, .6
            spacing: '5dp'
            Image:
                source: 'avata-user.jpg'
                size_hint: .5, .5
                pos_hint: {'center_x':0.5}
            MDLabel:
                text: 'Enter Your pin'
                size_hint: (0.5,0.2)
                pos_hint: {'center_x':0.55}
            MDTextField:
                size_hint: (0.5,0.29)
                pos_hint: {'center_x':0.5, 'center_y':0.2}
                
             
            GridLayout:
                cols: 3
                rows: 4
                pos_hint: {'center_x':0.5}
                size_hint: .5, .6
                spacing: '5dp'
                Button:
                    text: '1'
                    size_hint: (0.5,0.3)
                    background_color: (1, 1, 1, 1)
                Button:
                    text: '2'
                    size_hint: (0.5,0.3)
                Button:
                    text: '3'
                    size_hint: (0.5,0.3)
                Button:
                    text: '4'
                    size_hint: (0.5,0.3)
                Button:
                    text: '5'
                    size_hint: (0.5,0.3)
                Button:
                    text: '6'
                    size_hint: (0.5,0.3)
                Button:
                    text: '7'
                    size_hint: (0.5,0.3)
                Button:
                    text: '8'
                    size_hint: (0.5,0.3)
                Button:
                    text: '9'
                    size_hint: (0.5,0.3)
                Button:
                    text: ''
                    size_hint: (0.5,0.3)
                Button:
                    text: '0'
                    size_hint: (0.5,0.3)
                Button:
                    icon: 'backspaces-outline'
                    size_hint: (0.5,0.3)
                    
            Button:
                spacing: '10dp'
                text: 'Ok'
                on_press: root.manager.current = 'home'
                size_hint: (0.25,0.15)
                pos_hint: {'center_x':0.5, 'center_y':0.3}
<HomeScreen>:
    name: 'home'
    id: home_screen
    Screen:
        MDNavigationLayout:
            ScreenManager:
                Screen: 
                    BoxLayout:
                        orientation: 'vertical'
                        MDToolbar:
                            title: 'Categories'
                            left_action_items: [["menu", lambda x: nav_drawer.set_state("open")]]
                            right_action_items: [["magnify"], ["dots-vertical", lambda x: nav_ldrawer.set_state("open")]]
                        
                        
                        BoxLayout:
                            orientation: 'vertical'
                            ScrollView:
                                MDList:
                                    OneLineIconListItem:
                                        text: 'Vegetables'
                                        on_press: root.manager.current = 'indcat'
                                        icon_right: 'dots-vertical'
                                        ImageLeftWidget:
                                            source: 'Greens.jpg'
                                    OneLineIconListItem:
                                        text: 'Bread'
                                        ImageLeftWidget:
                                            source: 'Bread.jpg'
                                    OneLineIconListItem:
                                        text: 'Drinks'
                                        ImageLeftWidget:
                                            source: 'soda.jpg'
                                    OneLineIconListItem:
                                        text: 'Wheat Flour'
                                        ImageLeftWidget:
                                            source: 'WheatF.jpg'
                                    OneLineIconListItem:
                                        text: 'Eggs'
                                        ImageLeftWidget:
                                            source: 'eggs.jpg'
                                    OneLineIconListItem:
                                        text: 'Fresh Milk'
                                        ImageLeftWidget:
                                            source: 'fresh_milk.jpg'
                                    OneLineIconListItem:
                                        text: 'Indomie'
                                        ImageLeftWidget:
                                            source: 'indomie.jpg'
                                    OneLineIconListItem:
                                        text: 'Maize Flour'
                                        ImageLeftWidget:
                                            source: 'Maize flour.jpg'
                                    OneLineIconListItem:
                                        text: 'Sossi'
                                        ImageLeftWidget:
                                            source: 'sosi.jpg'
                                    OneLineIconListItem:
                                        text: 'Quality Rice'
                                        ImageLeftWidget:
                                            source: 'rice.jpg'
                                    OneLineIconListItem:
                                        text: 'Youghurt'
                                        ImageLeftWidget:
                                            source: 'youghurt.jpg'

                    MDBottomAppBar:
                        MDToolbar:
                            left_action_items: [["message", lambda x: nav_drawer.set_state("open")]]
                            type: 'bottom'
                            mode: 'free-end'
                            icon: 'plus'
                                

            MDNavigationDrawer:
                id: nav_drawer
                BoxLayout:
                    orientation: 'vertical'
                    spacing: '8dp'
                    padding: '8dp'
                    Image:
                        source: 'user.png'
                    MDLabel:
                        text: 'Gideon'
                        font_style: 'Subtitle1'
                        size_hint_y: None
                        height: self.texture_size[1]
                        pos_hint_x: .5
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
                                text: 'Add Category'
                                on_press: app.addcategory_dialog()
                                IconLeftWidget:
                                    icon: 'plus-circle-outline'
                            OneLineIconListItem:
                                text: 'Exit'
                                on_press: app.show_simple_dialog()
                                IconLeftWidget:
                                    icon: 'logout'
                                
                            
            MDNavigationDrawer:
                id: nav_ldrawer
                BoxLayout:
                    md_bg_color: 'dark'
                    orientation: 'vertical'
                    ScrollView:
                        MDList:
                            OneLineIconListItem:
                                text: 'Settings'
                                on_press: root.manager.current = 'settings'
                                IconLeftWidget:
                                    icon: 'dots-vertical'
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

<AddcategoryScreen>:
    id: 'mycatpage'
    name: 'addcat'
    orientation: "vertical"
    MDTextField:
        hint_text: "City"
    MDTextField:
        hint_text: "Street"

<CattegoryScreen>:
    name: 'indcat'
    Screen:
        MDNavigationLayout:
            ScreenManager:
                Screen: 
                    BoxLayout:
                        orientation: 'vertical'
                        MDToolbar:
                            title: 'Vegetables'
                            left_action_items: [["home", lambda x: app.manager.current('home')]]
                            right_action_items: [["magnify"], ["share-variant-outline"]]
                        
                    MDBottomAppBar:
                        MDToolbar:
                            left_action_items: [["message", lambda x: nav_drawer.set_state("open")]]
                            type: 'bottom'
                            mode: 'free-end'
                            icon: 'plus'

            MDNavigationDrawer:
                id: nav_drawer
                BoxLayout:
                    orientation: 'vertical'
                    spacing: '8dp'
                    padding: '8dp'
                    Image:
                        source: 'user.png'
                    MDLabel:
                        text: 'Gideon'
                        font_style: 'Subtitle1'
                        size_hint_y: None
                        height: self.texture_size[1]
                        pos_hint_x: .5
                    ScrollView:
                        MDList:
                            OneLineIconListItem:
                                text: 'Home'
                                on_press: root.manager.current = 'home'
                                IconLeftWidget:
                                    icon: 'home'
                            OneLineIconListItem:
                                text: 'Messages  +10'
                                on_press: root.manager.current = 'notification'
                                IconLeftWidget:
                                    icon: 'message-alert-outline'
                            OneLineIconListItem:
                                text: 'Add Category'
                                IconLeftWidget:
                                    icon: 'plus-circle-outline'
                            OneLineIconListItem:
                                text: 'Exit'
                                on_press: root.show_simple_dialog()
                                IconLeftWidget:
                                    icon: 'logout'
                                
                            
            MDNavigationDrawer:
                id: nav_ldrawer
                BoxLayout:
                    md_bg_color: 'dark'
                    orientation: 'vertical'
                    ScrollView:
                        MDList:
                            OneLineIconListItem:
                                text: 'Settings'
                                on_press: root.manager.current = 'settings'
                                IconLeftWidget:
                                    icon: 'dots-vertical'
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
                            left_action_items: [["home"]]
                            right_action_items: [["magnify"], ["share-variant-outline"]]
                        
                        BoxLayout:
                            orientation: 'vertical'
                            Image:
                                source: 'user.png'
                        
                            MDTextField:
                                hint_text: "Gideon"
                                size_hint: (0.7,0.25)
                                pos_hint: {'center_x':0.5}
                                icon_right: 'account'
                        
                            MDTextField:
                                hint_text: "Email"
                                size_hint: (0.7,0.25)
                                pos_hint: {'center_x':0.5}
                                icon_right: 'email'
                        
                            MDTextField:
                                hint_text: "Contact"
                                size_hint: (0.7,0.25)
                                pos_hint: {'center_x':0.5}
                                icon_right: 'phone'
                        
                            MDTextField:
                                hint_text: "Business Position"
                                size_hint: (0.7,0.25)
                                pos_hint: {'center_x':0.5}
                                icon_right: 'account-check'
                        
                            MDTextField:
                                hint_text: "Business Name"
                                size_hint: (0.7,0.25)
                                pos_hint: {'center_x':0.5}
                                icon_right: 'google-my-business'
                            
                        

            MDNavigationDrawer:
                id: nav_drawer
                BoxLayout:
                    orientation: 'vertical'
                    spacing: '8dp'
                    padding: '8dp'
                    Image:
                        source: 'user.png'
                    MDLabel:
                        text: 'Gideon'
                        font_style: 'Subtitle1'
                        size_hint_y: None
                        height: self.texture_size[1]
                        pos_hint_x: .5
                    ScrollView:
                        MDList:
                            OneLineIconListItem:
                                text: 'Home'
                                on_press: root.manager.current = 'home'
                                IconLeftWidget:
                                    icon: 'home'
                            OneLineIconListItem:
                                text: 'Notifications  +10'
                                on_press: root.manager.current = 'notification'
                                IconLeftWidget:
                                    icon: 'message-alert-outline'
                            OneLineIconListItem:
                                text: 'Add Category'
                                IconLeftWidget:
                                    icon: 'plus-circle-outline'
                            OneLineIconListItem:
                                text: 'Exit'
                                on_press: root.show_simple_dialog()
                                IconLeftWidget:
                                    icon: 'logout'
                                
                            
            MDNavigationDrawer:
                id: nav_ldrawer
                BoxLayout:
                    orientation: 'vertical'
                    ScrollView:
                        MDList:
                            OneLineIconListItem:
                                text: 'Settings'
                                on_press: root.manager.current = 'settings'
                                IconLeftWidget:
                                    icon: 'dots-vertical'
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
                            left_action_items: [["home"]]
                            right_action_items: [["magnify"], ["share-variant-outline"]]

                        BoxLayout:
                            orientation: 'vertical'
                            ScrollView:
                                MDList:
                                    OneLineIconListItem:
                                        text: 'Settings'
                                        on_press: root.manager.current = 'settings'
                                        IconLeftWidget:
                                            icon: 'dots-vertical'
                                    OneLineIconListItem:
                                        text: 'Help'
                                        on_press: root.manager.current = 'help'
                                        IconLeftWidget:
                                            icon: 'chat-question'
                                    OneLineIconListItem:
                                        text: 'Feedback'
                                        on_press: root.manager.current = 'feedback'
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
                                        on_press: root.manager.current = 'apps'
                                        IconLeftWidget:
                                            icon: 'apps' 

            MDNavigationDrawer:
                id: nav_drawer
                BoxLayout:
                    orientation: 'vertical'
                    spacing: '8dp'
                    padding: '8dp'
                    Image:
                        source: 'user.png'
                    MDLabel:
                        text: 'Gideon'
                        font_style: 'Subtitle1'
                        size_hint_y: None
                        height: self.texture_size[1]
                        pos_hint_x: .5
                    ScrollView:
                        MDList:
                            OneLineIconListItem:
                                text: 'Home'
                                on_press: root.manager.current = 'home'
                                IconLeftWidget:
                                    icon: 'home'
                            OneLineIconListItem:
                                text: 'Notifications  +10'
                                on_press: root.manager.current = 'notification'
                                IconLeftWidget:
                                    icon: 'message-alert-outline'
                            OneLineIconListItem:
                                text: 'Add Category'
                                IconLeftWidget:
                                    icon: 'plus-circle-outline'
                            OneLineIconListItem:
                                text: 'Exit'
                                on_press: root.show_simple_dialog()
                                IconLeftWidget:
                                    icon: 'logout'
                                
                            
            MDNavigationDrawer:
                id: nav_ldrawer
                BoxLayout:
                    orientation: 'vertical'
                    ScrollView:
                        MDList:
                            OneLineIconListItem:
                                text: 'Settings'
                                on_press: root.manager.current = 'settings'
                                IconLeftWidget:
                                    icon: 'dots-vertical'
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
                            left_action_items: [["home"]]
                            right_action_items: [["magnify"], ["share-variant-outline"]]

                        
                        GridLayout:
                            padding: '10dp'
                            spacing: '10dp'
                            cols: 2
                            BoxLayout:
                                orientation: 'vertical'
                                Image:
                                    source: 'user.png'
                                MDLabel:
                                    text: 'Gideon Kirui'
                                    color: 'red'
                                    font_style: 'H6'
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    pos_hint_x: .5
                                MDLabel:
                                    text: 'University of Embu'
                                    color: 'gray'
                                    font_style: 'Caption'
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    pos_hint_x: .5
                                MDLabel:
                                    text: '0712345678'
                                    color: 'gray'
                                    font_style: 'Caption'
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    pos_hint_x: .5
                                MDLabel: 
                                    text: 'BSc. Information Tech'
                                    color: 'gray'
                                    font_style: 'Caption'
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    pos_hint_x: .5

                            BoxLayout:
                                orientation: 'vertical'
                                Image:
                                    source: 'user.png'
                                MDLabel:
                                    text: 'Gideon Kirui'
                                    color: 'red'
                                    font_style: 'H6'
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    pos_hint_x: .5
                                MDLabel:
                                    text: 'University of Embu'
                                    color: 'gray'
                                    font_style: 'Caption'
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    pos_hint_x: .5
                                MDLabel:
                                    text: '0712345678'
                                    color: 'gray'
                                    font_style: 'Caption'
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    pos_hint_x: .5
                                MDLabel: 
                                    text: 'BSc. Information Tech'
                                    color: 'gray'
                                    font_style: 'Caption'
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    pos_hint_x: .5

                            BoxLayout:
                                orientation: 'vertical'
                                Image:
                                    source: 'user.png'
                                MDLabel:
                                    text: 'Gideon Kirui'
                                    color: 'red'
                                    font_style: 'H6'
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    pos_hint_x: .5
                                MDLabel:
                                    text: 'University of Embu'
                                    color: 'gray'
                                    font_style: 'Caption'
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    pos_hint_x: .5
                                MDLabel:
                                    text: '0712345678'
                                    color: 'gray'
                                    font_style: 'Caption'
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    pos_hint_x: .5
                                MDLabel: 
                                    text: 'BSc. Information Tech'
                                    color: 'gray'
                                    font_style: 'Caption'
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    pos_hint_x: .5
            MDNavigationDrawer:
                id: nav_drawer
                BoxLayout:
                    orientation: 'vertical'
                    spacing: '8dp'
                    padding: '8dp'
                    Image:
                        source: 'user.png'
                    MDLabel:
                        text: 'Gideon'
                        font_style: 'Subtitle1'
                        size_hint_y: None
                        height: self.texture_size[1]
                        pos_hint_x: .5
                    ScrollView:
                        MDList:
                            OneLineIconListItem:
                                text: 'Home'
                                on_press: root.manager.current = 'home'
                                IconLeftWidget:
                                    icon: 'home'
                            OneLineIconListItem:
                                text: 'Notifications  +10'
                                on_press: root.manager.current = 'notification'
                                IconLeftWidget:
                                    icon: 'message-alert-outline'
                            OneLineIconListItem:
                                text: 'Add Category'
                                IconLeftWidget:
                                    icon: 'plus-circle-outline'
                            OneLineIconListItem:
                                text: 'Exit'
                                on_press: root.show_simple_dialog()
                                IconLeftWidget:
                                    icon: 'logout'
                                
                            
            MDNavigationDrawer:
                id: nav_ldrawer
                BoxLayout:
                    orientation: 'vertical'
                    ScrollView:
                        MDList:
                            OneLineIconListItem:
                                text: 'Settings'
                                on_press: root.manager.current = 'settings'
                                IconLeftWidget:
                                    icon: 'dots-vertical'
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


<NotifyScreen>:
    name: 'notification'
    Screen:
        MDNavigationLayout:
            ScreenManager:
                Screen: 
                    BoxLayout:
                        orientation: 'vertical'
                        MDToolbar:
                            title: 'Messages'
                            left_action_items: [["home"]]
                            right_action_items: [["magnify"], ["share-variant-outline"]]

                        BoxLayout:
                            orientation: 'vertical'
                            MDLabel:
                                text: 'Stock status Notifications'
                                pos_hint: {'center_x':0.5}
                                size_hint: .8, .1
                            
                            BoxLayout:
                                orientation: 'vertical'
                                padding: '20dp'
                                MDLabel:
                                    text: 'Hi vegetable stock is runing low!'
                                    size_hint_y:None
                                    height: self.texture_size[1]
                                MDLabel:
                                    text: 'Hi vegetable stock is runing low!'
                                    size_hint_y:None
                                    height: self.texture_size[1]
                                MDLabel:
                                    text: 'Hi vegetable stock is runing low!'
                                    size_hint_y:None
                                    height: self.texture_size[1]
                                MDLabel:
                                    text: 'Hi vegetable stock is runing low!'
                                    size_hint_y:None
                                    height: self.texture_size[1]
                                MDLabel:
                                    text: 'Hi vegetable stock is runing low!'
                                    size_hint_y:None
                                    height: self.texture_size[1]
                                MDLabel:
                                    text: 'Hi vegetable stock is runing low!'
                                    size_hint_y:None
                                    height: self.texture_size[1]
                                ScrollView:
                         

            MDNavigationDrawer:
                id: nav_drawer
                BoxLayout:
                    orientation: 'vertical'
                    spacing: '8dp'
                    padding: '8dp'
                    Image:
                        source: 'user.png'
                    MDLabel:
                        text: 'Gideon'
                        font_style: 'Subtitle1'
                        size_hint_y: None
                        height: self.texture_size[1]
                        pos_hint_x: .5
                    ScrollView:
                        MDList:
                            OneLineIconListItem:
                                text: 'Home'
                                on_press: root.manager.current = 'home'
                                IconLeftWidget:
                                    icon: 'home'
                            OneLineIconListItem:
                                text: 'Notifications  +10'
                                on_press: root.manager.current = 'notification'
                                IconLeftWidget:
                                    icon: 'message-alert-outline'
                            OneLineIconListItem:
                                text: 'Add Category'
                                IconLeftWidget:
                                    icon: 'plus-circle-outline'
                            OneLineIconListItem:
                                text: 'Exit'
                                on_press: root.show_simple_dialog()
                                IconLeftWidget:
                                    icon: 'logout'
                                
                            
            MDNavigationDrawer:
                id: nav_ldrawer
                BoxLayout:
                    orientation: 'vertical'
                    ScrollView:
                        MDList:
                            OneLineIconListItem:
                                text: 'Settings'
                                on_press: root.manager.current = 'settings'
                                IconLeftWidget:
                                    icon: 'dots-vertical'
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
                            left_action_items: [["home"]]
                            right_action_items: [["magnify"], ["share-variant-outline"]]

                        BoxLayout:
                            orientation: 'vertical'
                            ScrollView:
                                MDList:
                                    OneLineListItem:
                                        text: 'How To Get Started?'
                                        
                                    OneLineListItem:
                                        text: 'How To Add Category?'
                                        
                                    OneLineListItem:
                                        text: 'How Does The App Work?'
                                        
                                    OneLineListItem:
                                        text: 'What if I loose My phone find my data?'
                                        
                                    OneLineListItem:
                                        text: 'contact the designers of this App?'
                                        on_press: root.manager.current = 'contact'
                                        
                                        
                                    OneLineListItem:
                                        text: 'Who are the users of this App?'
                                
                                    OneLineListItem:
                                        text: 'What are the benefits of using this app?'
                                    
                                    OneLineListItem:
                                        text: 'How can I log in using my google accoungt?'

                                    OneLineListItem:
                                        text: 'How does the app realize increse and decrease of stock?'
                                        

            MDNavigationDrawer:
                id: nav_drawer
                BoxLayout:
                    orientation: 'vertical'
                    spacing: '8dp'
                    padding: '8dp'
                    Image:
                        source: 'user.png'
                    MDLabel:
                        text: 'Gideon'
                        font_style: 'Subtitle1'
                        size_hint_y: None
                        height: self.texture_size[1]
                        pos_hint_x: .5
                    ScrollView:
                        MDList:
                            OneLineIconListItem:
                                text: 'Home'
                                on_press: root.manager.current = 'home'
                                IconLeftWidget:
                                    icon: 'home'
                            OneLineIconListItem:
                                text: 'Notifications  +10'
                                on_press: root.manager.current = 'notification'
                                IconLeftWidget:
                                    icon: 'message-alert-outline'
                            OneLineIconListItem:
                                text: 'Add Category'
                                IconLeftWidget:
                                    icon: 'plus-circle-outline'
                            OneLineIconListItem:
                                text: 'Exit'
                                on_press: root.show_simple_dialog()
                                IconLeftWidget:
                                    icon: 'logout'
                                
                            
            MDNavigationDrawer:
                id: nav_ldrawer
                BoxLayout:
                    orientation: 'vertical'
                    ScrollView:
                        MDList:
                            OneLineIconListItem:
                                text: 'Settings'
                                on_press: root.manager.current = 'settings'
                                IconLeftWidget:
                                    icon: 'dots-vertical'
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
                            left_action_items: [["home"]]
                            right_action_items: [["magnify"], ["share-variant-outline"]]

                        BoxLayout:
                            orientation: 'vertical'
                            ScrollView:
                                MDList:
                                    OneLineIconListItem:
                                        text: '0712345678/0787654321'
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
 

            MDNavigationDrawer:
                id: nav_drawer
                BoxLayout:
                    orientation: 'vertical'
                    spacing: '8dp'
                    padding: '8dp'
                    Image:
                        source: 'user.png'
                    MDLabel:
                        text: 'Gideon'
                        font_style: 'Subtitle1'
                        size_hint_y: None
                        height: self.texture_size[1]
                        pos_hint_x: .5
                    ScrollView:
                        MDList:
                            OneLineIconListItem:
                                text: 'Home'
                                on_press: root.manager.current = 'home'
                                IconLeftWidget:
                                    icon: 'home'
                            OneLineIconListItem:
                                text: 'Notifications  +10'
                                on_press: root.manager.current = 'notification'
                                IconLeftWidget:
                                    icon: 'message-alert-outline'
                            OneLineIconListItem:
                                text: 'Add Category'
                                IconLeftWidget:
                                    icon: 'plus-circle-outline'
                            OneLineIconListItem:
                                text: 'Exit'
                                on_press: root.show_simple_dialog()
                                IconLeftWidget:
                                    icon: 'logout'
                                
                            
            MDNavigationDrawer:
                id: nav_ldrawer
                BoxLayout:
                    orientation: 'vertical'
                    ScrollView:
                        MDList:
                            OneLineIconListItem:
                                text: 'Settings'
                                on_press: root.manager.current = 'settings'
                                IconLeftWidget:
                                    icon: 'dots-vertical'
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
    


'''