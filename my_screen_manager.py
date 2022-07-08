my_screen_helper='''
ScreenManager:
    MDScreen:
        name: 'home'
        MDBottomNavigation:
            id: btmnav
            panel_color: 0.2, 1, 0.5, 0.05
            text_color_active: 0, 0, 0, 1
            text_color_normal: 0.5, 0.5, 0.5, 0.3
            MDBottomNavigationItem:
                name: 'home'
                text: 'Home'
                icon: 'home'
                badge_icon: "numeric-10"
                
                MDNavigationLayout:
                    ScreenManager:
                        Screen:
                            BoxLayout:
                                orientation: 'vertical'
                                MDToolbar:
                                    title: 'Categories'
                                    #md_bg_color: app.theme_cls.custom_color
                                    left_action_items: [["menu", lambda x: nav_drawer.set_state("open"), "Menu tab"]]
                                    right_action_items: [["magnify"], ["dots-vertical", lambda x: nav_ldrawer.set_state("open")]]
                                BoxLayout:
                                    orientation: 'vertical'
                                    adaptive_height: True
                                    ScrollView:
                                        MDGridLayout:
                                            id: panel_container
                                            cols: 1
                                            size_hint_y: None
                                            height: self.minimum_height

                                MDFloatingActionButton:
                                    id: button
                                    icon: "plus"
                                    md_bg_color: 0.2, 0.8, 0.5, 1
                                    size_hint: None, None
                                    pos_hint: {'center_x':0.9, 'center_y':0.2}
                                    on_release: app.addCategory_dialog_pop(),   

                    MDNavigationDrawer:
                        id: nav_drawer
                        top_right_radius: 20
                        size_hint: (0.6, 0.4)
                        pos_hint: {'center_y':0.68}
                        BoxLayout:
                            orientation: 'vertical'
                            spacing: '5dp'
                            Image:
                                source: 'user.png'
                                size_hint: (0.5, 0.5)
                                pos_hint: {'center_x':0.5, 'center_y':0.05}

                            MDLabel:
                                text: 'Owner'
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
                                        on_press: root.current ='profile'
                                        IconLeftWidget:
                                            icon: 'account'
                                   
                                    OneLineIconListItem:
                                        text: 'Exit'
                                        on_press: app.show_exit_dialog()
                                        IconLeftWidget:
                                            icon: 'logout'

                    MDNavigationDrawer:
                        id: nav_ldrawer
                        anchor: 'right'
                        size_hint: (0.7, 0.65)
                        pos_hint: {'center_y':0.55}
                        BoxLayout:
                            md_bg_color: 'dark'
                            orientation: 'vertical'
                            ScrollView:
                                MDList:
                                    OneLineIconListItem:
                                        text: 'Help'
                                        on_press: root.current = 'help'
                                        IconLeftWidget:
                                            icon: 'chat-question'
                                    OneLineIconListItem:
                                        text: 'Feedback'
                                        IconLeftWidget:
                                            icon: 'chat'
                                    OneLineIconListItem:
                                        text: 'Contact Us'
                                        on_press: root.current = 'contact'
                                        IconLeftWidget:
                                            icon: 'phone'
                                    OneLineIconListItem:
                                        text: 'About Us'
                                        on_press: root.current = 'about'
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

            MDBottomNavigationItem:
                name: 'settings'
                text: 'Settings'
                icon: 'cog'
                badge_icon: "numeric-5"
                BoxLayout:
                    orientation: 'vertical'
                    MDToolbar:
                        title: 'Settings'
                        right_action_items: [["magnify"],["dots-vertical"]]

                    BoxLayout:
                        orientation: 'vertical'
                        spacing: '10dp'
                        ScrollView:
                            MDList:
                                spacing: '10dp'
                                OneLineIconListItem:
                                    padding: '5dp'
                                    text: 'Edit Acount'
                                    on_press: root.current = 'profile'
                                    IconLeftWidget:
                                        icon: 'account'
                                OneLineIconListItem:
                                    text: 'Change Theme'
                                    #on_release: app.show_themepicker()
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

            MDBottomNavigationItem:
                name: 'messages'
                text: 'Messages'
                on_tab_press: #app.message_dialog_alert()
                icon: 'message-outline'
                badge_icon: 'numeric-5'

                BoxLayout:
                    orientation: 'vertical'
                    MDToolbar:
                        title: 'Messages'
                        right_action_items: [["magnify"], ["dots-vertical"]]

                    MDGridLayout:
                        cols: 1
                        padding: '5dp'
                        spacing: '1dp', '10dp'
                        MDCard:
                            md_bg_color: 0.5, 0.5, 0.5, 0.1
                            orientation: "vertical"
                            size_hint: 0.98, None
                            height: self.minimum_size[1]
                            radius: [20, ]
                            spacing: '5dp'
                            padding: '20dp'
                            #pos_hint_y: 'top'

                            MDLabel:
                                id: messagealart
                                text: "mesg_alart"
                                height: self.texture_size[1]
                                theme_text_color: 'Custom'
                                size_hint_y: None
                                # size_hint_x: None
                                bold: True
                                font_size: 13
                                color: [0, 0, 0, 1]
                                shorten: True
                                markup: True
                                shorten_from: 'right'
                                
                        MDCard:
                            md_bg_color: 0.5, 0.5, 0.5, 0.1
                            orientation: "vertical"
                            size_hint: 0.98, None
                            height: self.minimum_size[1]
                            radius: [20, ]
                            spacing: '5dp'
                            padding: '20dp'
                            #pos_hint_y: 'top'

                            MDLabel:
                                #id: lastMessage
                                text: "Your Kales stock is Runing low"
                                height: self.texture_size[1]
                                theme_text_color: 'Custom'
                                size_hint_y: None
                                # size_hint_x: None
                                bold: True
                                font_size: 13
                                color: [0, 0, 0, 1]
                                shorten: True
                                markup: True
                                shorten_from: 'right'
                    
    MDScreen:
        name: 'profile'
        BoxLayout:
            orientation: 'vertical'
            MDToolbar:
                title: 'My Profile'
                left_action_items: [["arrow-left", lambda x: app.Navigate_t0_homepage()]]
                right_action_items: [["pencil-box-multiple-outline"]]
            
            BoxLayout:
                orientation: 'vertical'
                spacing: '5dp'
                Image:
                    source: 'user.png'
                    size_hint: .5, .5
                    pos_hint: {'center_x':0.5}

                MDTextField:
                    hint_text: "Owner"
                    size_hint_x: 0.7
                    pos_hint: {'center_x':0.5}
                    icon_right: 'account'
                    #icon_right: 'pencil-box-multiple-outline'
                    mode: "rectangle"
            
                MDTextField:
                    hint_text: "ShopOnwer"
                    size_hint_x: 0.7
                    pos_hint: {'center_x':0.5}
                    icon_right: 'email'
                    mode: "rectangle"
            
                MDTextField:
                    hint_text: "0712345678"
                    size_hint_x: 0.7
                    pos_hint: {'center_x':0.5}
                    icon_right: 'phone'
                    mode: "rectangle"
            
                MDTextField:
                    hint_text: "Manager"
                    size_hint_x: 0.7
                    pos_hint: {'center_x':0.5}
                    icon_right: 'account-check'
                    mode: "rectangle"
            
                MDTextField:
                    hint_text: "SumGT Shop"
                    size_hint_x: 0.7
                    pos_hint: {'center_x':0.5}
                    icon_right: 'google-my-business'
                    mode: "rectangle"

                Button:
                    text: 'Save Changes'
                    size_hint_y: 0.08
                    size_hint_x: 0.5
                    pos_hint: {'center_x':0.5}
                    background_color: (100/255, 222/255, 24/255)
                    color: 'teal'
                    on_release: app.show_popup()

    MDScreen:
        id: help
        name: 'help'
        MDNavigationLayout:
            ScreenManager:
                Screen: 
                    BoxLayout:
                        orientation: 'vertical'
                        MDToolbar:
                            title: 'Help'
                            left_action_items: [["arrow-left", lambda x: app.Navigate_t0_homepage()]]
                            right_action_items: [["magnify"]]

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
                                        on_press: root.current = 'contact'
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

    MDScreen:
        name: 'contact'
        MDNavigationLayout:
            ScreenManager:
                Screen: 
                    BoxLayout:
                        orientation: 'vertical'
                        MDToolbar:
                            title: 'Contact Us'
                            left_action_items: [["arrow-left", lambda x: app.Navigate_t0_homepage()]]
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
                                            text: 'www.shopmanagerappweb.com'
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
                                            text: 'ShomanagerAppFAcount'
                                            color: 'gray'
                                            font_style: 'Caption'
                                            IconLeftWidget:
                                                icon: 'facebook'
                                        OneLineIconListItem:
                                            text: 'ShopmanagerApp@Twitter'
                                            color: 'gray'
                                            font_style: 'Caption'
                                            IconLeftWidget:
                                                icon: 'twitter'
                                        OneLineIconListItem:
                                            text: 'shopmangerapp@gmail.com'
                                            color: 'gray'
                                            font_style: 'Caption'
                                            IconLeftWidget:
                                                icon: 'email'
                                        OneLineIconListItem:
                                            text: 'shopmanagerAppdevs@linkedin'
                                            color: 'gray'
                                            font_style: 'Caption'
                                            IconLeftWidget:
                                                icon: 'linkedin'
                                        OneLineIconListItem:
                                            text: 'shopmanagerappdevs.github.com'
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

    MDScreen:
        name: 'about'
        MDNavigationLayout:
            ScreenManager:
                Screen: 
                    BoxLayout:
                        orientation: 'vertical'
                        MDToolbar:
                            title: 'About Us'
                            left_action_items: [["arrow-left", lambda x: app.Navigate_t0_homepage()]] 

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

<Mycontent>
    orientation: 'vertical'
    size_hint_y: None
    height: self.minimum_height
    MDGridLayout:
        cols: 1
        size_hint_y: None
        height: self.minimum_height
        TwoLineAvatarIconListItem:
            id: subcatname
            text: "Onions"
            secondary_text: root.quantity + " bulbs"
            

            IconLeftWidget:
                icon: "pencil-box-multiple-outline"
                on_release: app.editCategory_dialog_pop()

            IconRightWidget:
                icon: "minus-circle"
                on_release: root.stock_reg_snackbar()

    #TwoLineAvatarIconListItem:
    #    text: "Tomatoes"
    #    secondary_text: root.quantity + " balls"

    #    IconLeftWidget:
    #        icon: "pencil-box-multiple-outline"
    #        on_release: app.editCategory_dialog_pop()
                
    #    IconRightWidget:
    #        icon: "minus-circle"
    #        on_release: app.stock_reg_snackbar()
                

    #TwoLineAvatarIconListItem:
    #    text: "Kales"
    #    secondary_text:root.quantity + " bundles"#
    #    IconLeftWidget:
    #        icon: "pencil-box-multiple-outline"
    #        on_release: app.editCategory_dialog_pop()#
    #    IconRightWidget:
    #        icon: "minus-circle"
    #        on_release: app.stock_reg_snackbar()
            
    #TwoLineAvatarIconListItem:
    #    text: "Cabbages"
    #    secondary_text: "150 balls"#
    #    IconLeftWidget:
    #        icon: "pencil-box-multiple-outline"
    #        on_release: app.editCategory_dialog_pop()

    #    IconRightWidget:
    #        icon: "minus-circle"
    #        on_release: app.stock_reg_snackbar()
            
    #TwoLineAvatarIconListItem:
    #    text: "Carrot"
    #    secondary_text: "300 Roots"#
    #    IconLeftWidget:
    #        icon: "pencil-box-multiple-outline"
    #        on_release: app.editCategory_dialog_pop()

        #    IconRightWidget:
        #       icon: "minus-circle"
        #        on_release: app.stock_reg_snackbar()
              

        MDIconButton:
            icon: "plus-circle"
            on_release: app.addSubCategory_dialog_pop()
            pos_hint: {'center_x':0.9, 'center_y':0.2}
        

    #MDScreen:
    #    name: 'notification'
    #    MDCard:
    #        MDLabel:
    #            text: 'You have one New Message'
    #        BoxLayout:
    #            Button:
    #                text: 'Cancel'
    #            Button:
    #                text: 'See message'
    
        
<Content>
    orientation: "vertical"
    spacing: "10dp"
    size_hint_y: None
    height: "180dp"
    MDTextField:
        hint_text: "Enter  name"
        

    MDTextField:
        id: subcatQ
        hint_text: "Quantity"
        

    MDTextField:
        hint_text: "Quantity Description"
        helper_text: "e.g Kg, ltrs, roll, box, dozone e.t.c"
        helper_text_mode: "on_focus"
        
        
<Content2>
    id: addcat
    orientation: "vertical"
    spacing: "10dp"
    size_hint_y: None
    height: "60dp"
    MDTextField:
        text: ''
        hint_text: "Enter Category name"

<Content3>
    orientation: "vertical"
    spacing: "10dp"
    size_hint_y: None 
    height: "180dp"
    MDTextField:
        hint_text: "Onions"
        halign: 'center'
        

    MDTextField:
        hint_text: "200"
        

    MDTextField:
        hint_text: "bulbs"

'''