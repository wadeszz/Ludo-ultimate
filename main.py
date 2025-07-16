from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock
import random

class LudoGame(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', **kwargs)
        self.die_label = Label(text='🎲 Нажми "Бросить"', font_size=40, size_hint=(1, 0.4))
        self.roll_button = Button(text='Бросить кубик', font_size=30, size_hint=(1, 0.3))
        self.status_label = Label(text='', font_size=24, size_hint=(1, 0.3))

        self.roll_button.bind(on_press=self.roll_die)

        self.add_widget(self.die_label)
        self.add_widget(self.roll_button)
        self.add_widget(self.status_label)

    def roll_die(self, instance):
        self.die_label.text = '🎲 Крутим...'
        Clock.schedule_once(self.finish_roll, 0.5)

    def finish_roll(self, dt):
        value = random.randint(1, 6)
        self.die_label.text = f'🎲 Выпало: {value}'
        self.status_label.text = 'Выбери фишку (пока не реализовано)'

class LudoApp(App):
    def build(self):
        return LudoGame()

if __name__ == '__main__':
    LudoApp().run()
