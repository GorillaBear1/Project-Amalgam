from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.clock import Clock
import time

# CONFIG: Deep Crimson Background
from kivy.core.window import Window
Window.clearcolor = (0.1, 0, 0, 1)

class SovereignNodeApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical', padding=50)
        
        # TIME DISPLAY
        self.time_label = Label(
            text='[b]INITIALIZING...[/b]', 
            font_size='50sp',
            markup=True, 
            color=(0, 1, 1, 1) # Cyan
        )
        
        # DATE DISPLAY
        self.date_label = Label(
            text='', 
            font_size='20sp',
            markup=True, 
            color=(0.8, 0.8, 0.8, 1) # Light Grey
        )

        self.layout.add_widget(self.time_label)
        self.layout.add_widget(self.date_label)

        # Update every 1 second (1.0)
        Clock.schedule_interval(self.update_time, 1.0)
        
        return self.layout

    def update_time(self, dt):
        # Get current time
        current_time = time.strftime("%H:%M:%S")
        current_date = time.strftime("%A, %B %d, %Y")
        
        # Update text
        self.time_label.text = f'[b]{current_time}[/b]'
        self.date_label.text = current_date

if __name__ == '__main__':
    SovereignNodeApp().run()
