from kivy.app import App
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.core.window import Window

from kivy.uix.gridlayout import GridLayout

Window.clearcolor = (.9, .9, .9, 1)

class CalculatorCubovApp(App):
    def build(self):
        bl = GridLayout(cols=2, padding=[50], spacing=[50])
        self.empty1 = (Label(text='1'))
        self.empty2 = (Label(text='1'))
        self.empty = (Label(text='1'))
        self.l = (Label(text='Длина в мм', color='black'))
        self.length = (TextInput(hint_text='Введите длину...', multiline=False, size_hint_x=10))
        self.w = (Label(text='Ширина в мм', color='black'))
        self.width = (TextInput(hint_text='Введите ширину...', multiline=False))
        self.h = (Label(text='Высота в мм', color='black'))
        self.height = (TextInput(hint_text='Введите высоту...', multiline=False))
        self.n = (Label(text='Кол-во штук', color='black'))
        self.number = (TextInput(hint_text='Введите количество...', multiline=False))
        self.pr = (Label(text='Цена за куб', color='black'))
        self.price = (TextInput(hint_text='Введите цену за куб...', multiline = False))

        self.reset = (Button(text='Сброс', background_color='red', size_hint_x=None, width=250, on_press=self.restart))
        self.operation = (Button(text='Расчёт', background_color='blue', size_hint_x=None, width=700, on_press=self.calculate))

        self.v = Label(text='Кол-во кубов: ', color='black')
        self.p = Label(text='Цена: ', color='black')

        bl.add_widget(self.empty1)
        bl.add_widget(self.empty2)
        bl.add_widget(self.l)
        bl.add_widget(self.length)
        bl.add_widget(self.w)
        bl.add_widget(self.width)
        bl.add_widget(self.h)
        bl.add_widget(self.height)
        bl.add_widget(self.n)
        bl.add_widget(self.number)
        bl.add_widget(self.pr)
        bl.add_widget(self.price)
        bl.add_widget(self.reset)
        bl.add_widget(self.operation)
        bl.add_widget(self.v)

        bl.add_widget(self.p)

        return bl

    def calculate(self,instance):
        a = int(self.length.text)
        b = int(self.width.text)
        c = int(self.height.text)
        d = int(self.number.text)
        e = int(self.price.text)
        v = a*b*c
        s = a*b*c*d/1000000000
        p = (v*e/1000000000)*d
        self.v.text = 'Кол-во кубов: ' + str(s) + ' куб.м.'
        self.p.text = 'Цена: ' + str(p) + ' за ' + str(d) + ' шт.'

    def restart(self, instance):
        self.length.text = ''
        self.width.text = ''
        self.height.text = ''
        self.number.text = ''
        self.price.text = ''
        self.v.text = 'Кол-во кубов: '
        self.p.text = 'Цена: '


if __name__ == "__main__":
    CalculatorCubovApp().run()