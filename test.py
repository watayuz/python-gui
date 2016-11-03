from kivy.app import App
from kivy.config import Config

from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

from kivy.uix.gridlayout import GridLayout

# about layout
# 全体をFloatLayoutのorientationをvertical
# 下はGridLayout
# 上はFloatLayoutのorientationをhorizontal

class RootWidget(GridLayout):

    def buttonClicked(self, instance):
        print('press button')

    def __init__(self, **kwargs):
        super(RootWidget, self).__init__(cols=1)

        textinput = TextInput()
        label = Label(text='label')
        button = Button(text='push Button',
            height=30)
        button.bind(on_press=self.buttonClicked)

        self.add_widget(textinput)
        self.add_widget(label)
        self.add_widget(button)

class TestApp(App):
    def build(self):

        # window settings
        Config.set('graphics', 'width', '300')
        Config.set('graphics', 'height', '800')

        self.root = RootWidget()

        self.title = 'test title'
        # self.icon = 'FILE NAME'
        return self.root

if __name__ == '__main__':
    TestApp().run()