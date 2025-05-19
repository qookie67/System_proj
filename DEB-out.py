from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

Builder.load_file('debout.kv')
Builder.load_file('cam.kv')

class HomeScreen(Screen):
    pass

class CameraScreen(Screen):
    pass

class DEBoutApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(HomeScreen(name='home'))
        sm.add_widget(CameraScreen(name='camera'))
        return sm

DEBoutApp().run()
