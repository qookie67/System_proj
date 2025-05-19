from kivy.app import App
from kivy.lang import Builder

class Camera(App):
    def build(self):
        return Builder.load_file('cam.kv')

Camera().run()