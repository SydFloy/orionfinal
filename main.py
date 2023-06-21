from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.app import MDApp
from kivymd.uix.dialog import MDDialog
from kivymd.uix.textfield import MDTextField
from kivymd.uix.button import MDRectangleFlatButton
import webbrowser
class HomeScreen(Screen):
    
    def log(self):##############################################################
        username = self.ids.user.text
        password= self.ids.passw.text
        self.close_btn=MDRectangleFlatButton(text='close',on_release=self.close)
        self.pop=MDDialog(title='Error',text='wrong username or password',
            size_hint=(0.7,1),
            buttons=[self.close_btn],
            radius=[20, 7, 20, 7]
            )
        if username == 'a' and password=='1':
            app = MDApp.get_running_app()
            app.root.current = 'about_screen' 
            self.manager.transition.direction='left'
        else:
            
          
            self.pop.open()
    def close(self, *args):
        self.pop.dismiss()
    
           
class AboutScreen(Screen):
    def logout(self):
        print(self.my_class_instance.username)
        
class FabScreen(Screen):
    
   
    def on_touch_move(self, touch):
        if touch.dx > 50:
            
            self.manager.transition.direction = 'right'
            self.manager.current = 'about_screen'
    def lunch_fab(self,link):
    
           webbrowser.open(link)
    

class DisScreen(Screen):
    def on_touch_move(self, touch):
        if touch.dx > 50:
            
            self.manager.transition.direction = 'right'
            self.manager.current = 'about_screen'
    def lunch_dis(self,link):
        webbrowser.open(link)
    
class GeaScreen(Screen):
    def on_touch_move(self, touch):
        if touch.dx > 50:
            
            self.manager.transition.direction = 'right'
            self.manager.current = 'about_screen'
    def lunch_gea(self,link):
        webbrowser.open(link)
class GraScreen(Screen):
    def on_touch_move(self, touch):
        if touch.dx > 50:
            
            self.manager.transition.direction = 'right'
            self.manager.current = 'gea_screen'
    def lunch_gra(self,link):
        webbrowser.open(link)
               
# Define screen manager
class GlattScreen(Screen):
    def on_touch_move(self, touch):
        if touch.dx > 50:
            
            self.manager.transition.direction = 'right'
            self.manager.current = 'about_screen'
    def lunch_glatt(self,link):
        webbrowser.open(link)

class HarroScreen(Screen):
    def on_touch_move(self, touch):
        if touch.dx > 50:
            
            self.manager.transition.direction = 'right'
            self.manager.current = 'about_screen'
    def lunch_harro(self,link):
        webbrowser.open(link)
class LastScreen(Screen):
    def on_touch_move(self, touch):
        if touch.dx > 50:
            
            self.manager.transition.direction = 'right'
            self.manager.current = 'about_screen'
    def lunch_last(self,link):
        webbrowser.open(link)

class MyScreenManager(ScreenManager):
    pass


# Create app
class MainApp(MDApp):
    def build(self):
        self.color='Light'
        self.theme_cls.primary_palette='Blue'
        self.theme_cls.primary_hue='300'
        self.theme_cls.theme_style="Light"
        Builder.load_file('main.kv')

        # Create screen manager and add screens
        sm = MyScreenManager()
        sm.add_widget(HomeScreen(name='home_screen'))
        sm.add_widget(AboutScreen(name='about_screen'))
        sm.add_widget(FabScreen(name='fab_screen'))
        sm.add_widget(DisScreen(name='dis_screen'))
        sm.add_widget(DisScreen(name='dis_screen'))
        
        return sm
    def log_out(self,button):
        self.root.current = 'home_screen' 
    
    
    

if __name__ == '__main__':
    MainApp().run()
