# from kivymd.app import MDApp
# from kivymd.uix.label import MDLabel
#
#
# class MortgageCalculatorApp(MDApp):
#     def build(self):
#         return MDLabel(text="MortgageCalculator", halign="center")
#
#
# MortgageCalculatorApp().run()


# from kivy.lang import Builder
# from kivy.properties import ObjectProperty
#
# from kivymd.app import MDApp
# from kivymd.uix.scrollview import MDScrollView
#
# KV = '''
# <ContentNavigationDrawer>
#
#     MDList:
#
#         OneLineListItem:
#             text: "Screen 1"
#             on_press:
#                 root.nav_drawer.set_state("close")
#                 root.screen_manager.current = "scr 1"
#
#         OneLineListItem:
#             text: "Screen 2"
#             on_press:
#                 root.nav_drawer.set_state("close")
#                 root.screen_manager.current = "scr 2"
#
#
# MDScreen:
#
#     MDTopAppBar:
#         pos_hint: {"top": 1}
#         elevation: 4
#         title: "MDNavigationDrawer"
#         left_action_items: [["menu", lambda x: nav_drawer.set_state("open")]]
#
#     MDNavigationLayout:
#
#         MDScreenManager:
#             id: screen_manager
#
#             MDScreen:
#                 name: "scr 1"
#
#                 MDLabel:
#                     text: "Screen 1"
#                     halign: "center"
#
#             MDScreen:
#                 name: "scr 2"
#
#                 MDLabel:
#                     text: "Screen 2"
#                     halign: "center"
#
#         MDNavigationDrawer:
#             id: nav_drawer
#             radius: (0, 16, 16, 0)
#
#             ContentNavigationDrawer:
#                 screen_manager: screen_manager
#                 nav_drawer: nav_drawer
# '''
#
#
# class ContentNavigationDrawer(MDScrollView):
#     screen_manager = ObjectProperty()
#     nav_drawer = ObjectProperty()
#
#
# class Example(MDApp):
#     def build(self):
#         self.theme_cls.primary_palette = "Orange"
#         self.theme_cls.theme_style = "Dark"
#         return Builder.load_string(KV)
#
#
# Example().run()

from kivy.lang import Builder

from kivymd.app import MDApp

KV = '''
<DrawerClickableItem@MDNavigationDrawerItem>
    focus_color: "#e7e4c0"
    text_color: "#4a4939"
    icon_color: "#4a4939"
    ripple_color: "#c5bdd2"
    selected_color: "#0c6c4d"


<DrawerLabelItem@MDNavigationDrawerItem>
    text_color: "#4a4939"
    icon_color: "#4a4939"
    focus_behavior: False
    selected_color: "#4a4939"
    _no_ripple_effect: True


MDScreen:

    MDNavigationLayout:

        MDScreenManager:

            MDScreen:

                MDTopAppBar:
                    title: "Mortgage Colculator"
                    elevation: 4
                    pos_hint: {"top": 1}
                    md_bg_color: "#e7e4c0"
                    specific_text_color: "#4a4939"
                    left_action_items: [["menu", lambda x: nav_drawer.set_state("open")]]
                          

        MDNavigationDrawer:
            id: nav_drawer
            radius: (0, 16, 16, 0)
            
            

            MDNavigationDrawerMenu:
            
                MDNavigationDrawerHeader:
                    id: avatar
                    source:"logo3-min.png"                     
                    spacing: "4dp"
                    padding: "12dp", 0, 0, "56dp"
                    size_hint:None, None
                    size: "56dp", "56dp"

                # MDNavigationDrawerHeader:
                #     #title: "Header text Mortgage Colculator"
                #     title_color: "#4a4939"
                #     text: "Mortgage Colculator"
                #     spacing: "4dp"
                #     padding: "12dp", 0, 0, "56dp"

                #MDNavigationDrawerLabel:
                    #text: "Mail"

                DrawerClickableItem:
                    icon: "folder"
                    right_text: "+99"
                    text_right_color: "#4a4939"
                    text: "My file"
                    
                DrawerClickableItem:
                    icon: "account-multiple"
                    right_text: "+99"
                    text_right_color: "#4a4939"
                    text: "Shared with me"

                DrawerClickableItem:
                    icon: "star"
                    text: "Starred"
                    
                DrawerClickableItem:
                    icon: "history"
                    text: "Recent"
                    
                DrawerClickableItem:
                    icon: "checkbox-marked"
                    text: "Shared with me"
                    
                DrawerClickableItem:
                    icon: "upload"
                    text: "Upload"

                MDNavigationDrawerDivider:

                # MDNavigationDrawerLabel:
                #     text: "Labels"
                # 
                # DrawerLabelItem:
                #     icon: "information-outline"
                #     text: "Label"
                # 
                # DrawerLabelItem:
                #     icon: "information-outline"
                #     text: "Label"
'''


class MortgageColculatorApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        return Builder.load_string(KV)


MortgageColculatorApp().run()