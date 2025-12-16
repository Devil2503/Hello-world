from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.popup import Popup

class MainLayout(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', padding=20, spacing=15, **kwargs)
        self.add_widget(Label(text='Мощность комплектующих (W)', font_size=18))
        self.components_input = TextInput(multiline=False, input_filter='int')
        self.add_widget(self.components_input)
        self.add_widget(Label(text='Мощность блока питания (W)', font_size=18))
        self.psu_input = TextInput(multiline=False, input_filter='int')
        self.add_widget(self.psu_input)
        
        btn = Button(text='Рассчитать', size_hint=(1, 0.3))
        btn.bind(on_press=self.calculate)
        self.add_widget(btn)

    def calculate(self, instance):
        try:
            components = int(self.components_input.text)
            psu = int(self.psu_input.text)

            if components <= 0 or psu <= 0:
                raise ValueError

            recommended = int(components * 1.3)
            load_percent = int((components / psu) * 100)

            if load_percent <= 70:
                status = '🟢 Отлично'
            elif load_percent <= 85:
                status = '🟡 Допустимо'
            else:
                status = '🔴 Недостаточно'

            text = (
                f"Общее потребление: {components} W\n"
                f"Рекомендуемый БП: {recommended} W\n"
                f"Загрузка БП: {load_percent} %\n\n"
                f"Статус: {status}"
        )

            popup = Popup(title='Результат', content=Label(text=text, font_size=16),
                      size_hint=(0.8, 0.6))
            popup.open()

        except ValueError:
            Popup(title='Ошибка',
              content=Label(text='Введите корректные значения'),
              size_hint=(0.7, 0.4)).open()

class PSUCheckerApp(App):
    def build(self):
        self.title = 'PSU Checker'
        return MainLayout()

if __name__ == 'main':
    PSUCheckerApp().run()