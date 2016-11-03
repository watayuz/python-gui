from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.config import Config

# window settings
Config.set('graphics', 'width', '400')
Config.set('graphics', 'height', '800')

class TestApp(App):
    def build(self):
        self.title = 'test'
        # self.icon = 'FILENAME'
        return Label(text='hello world')

if __name__ == '__main__':
    TestApp().run()