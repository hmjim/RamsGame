from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
import socketio

sio = socketio.Client()

Builder.load_string('''
<MenuScreen>:
    BoxLayout:
        orientation: 'vertical'
        padding: 50
        spacing: 20
        Label:
            text: "РАМС ОНЛАЙН"
            font_size: '30sp'
        Button:
            text: "ИГРАТЬ"
            on_release: root.manager.current = 'game'
        Button:
            text: "РЕЙТИНГ"
            on_release: root.manager.current = 'leaderboard'

<GameScreen>:
    BoxLayout:
        orientation: 'vertical'
        Label:
            text: "Игровой стол: Ожидание игроков..."
        Button:
            text: "Выход"
            size_hint_y: 0.2
            on_release: root.manager.current = 'menu'

<LeaderboardScreen>:
    BoxLayout:
        orientation: 'vertical'
        Label:
            text: "ТОП-10 ИГРОКОВ"
            size_hint_y: 0.2
        ScrollView:
            GridLayout:
                id: container
                cols: 3
                row_default_height: 40
        Button:
            text: "Назад"
            size_hint_y: 0.1
            on_release: root.manager.current = 'menu'
''')


class MenuScreen(Screen):
    pass


class GameScreen(Screen):
    pass


class LeaderboardScreen(Screen):
    pass


class RamsApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MenuScreen(name='menu'))
        sm.add_widget(GameScreen(name='game'))
        sm.add_widget(LeaderboardScreen(name='leaderboard'))
        return sm


if __name__ == '__main__':
    # Вставь сюда адрес своего сервера, когда запустишь его в облаке
    # sio.connect('https://твой_логин.pythonanywhere.com')
    # Для теста можно использовать локальный IP, если телефон в той же сети
    # sio.connect('http://192.168.1.5:5000') 
    RamsApp().run()

