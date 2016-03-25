from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Color, Ellipse, Line


class MyPaintWidget(Widget):
    def on_touch_down(self, touch):
        with self.canvas:
            Color(1, 0, 1)
            # d is for diameter
            # (distance across center of circle)
            d = 10
            Ellipse(pos=(touch.x - d / 2, touch.y - d / 2),
                    size=(d, d))
            touch.ud['line'] = Line(
                points=(touch.x, touch.y),
                width=20)

    def on_touch_move(self, touch):
        touch.ud['line'].points += [touch.x, touch.y]

class MyPaintApp(App):
    def build(self):
        return MyPaintWidget()


if __name__ == '__main__':
    MyPaintApp().run()
