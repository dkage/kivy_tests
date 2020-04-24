from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget


class Container(Widget):
    pass


class MainApp(App):

    def build(self):
        self.title = '-- Kivy tests --'
        return Container()


if __name__ == "__main__":
    app = MainApp()
    app.run()
