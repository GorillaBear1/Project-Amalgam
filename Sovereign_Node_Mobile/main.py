from kivy.app import App
from kivy.uix.label import Label
from kivy.core.window import Window

# CONFIG: Bevi's Aesthetics
# Background: Deep Crimson/Black (RGB: 0.1, 0, 0)
Window.clearcolor = (0.1, 0, 0, 1)

class SovereignNodeApp(App):
    def build(self):
        # Text: Cyan Blue (RGB: 0, 1, 1)
        return Label(
            text='[b]SOVEREIGN NODE\nONLINE[/b]', 
            font_size='40sp',
            markup=True, 
            color=(0, 1, 1, 1),
            halign='center'
        )

if __name__ == '__main__':
    SovereignNodeApp().run()
