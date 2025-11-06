from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.label import Label
from kivy.clock import Clock
from kivy.animation import Animation
from random import randint, uniform
try:
    from kivy_garden.webview import WebView
except Exception:
    WebView = None
from modules.convert_systems import convert_number
from modules.horoscope import get_horoscope

class HomeScreen(Screen): pass
class ConvertScreen(Screen): pass
class HoroscopeScreen(Screen): pass
class MusicScreen(Screen): pass

class RineApp(App):
    def convert(self, number, from_base, to_base):
        try:
            f, t = int(from_base), int(to_base)
            return convert_number(number, f, t)
        except:
            return "⚠️ Dữ liệu không hợp lệ!"

    def horoscope(self, sign):
        try:
            s = int(sign)
            return get_horoscope(s)
        except:
            return "⚠️ Nhập số 1–12!"

    def spawn_hearts_once(self, *args):
        # spawn a few hearts when called
        screen = self.root.get_screen("home")
        for _ in range(randint(6, 10)):
            heart = Label(text="💖", font_size=uniform(24, 48))
            try:
                x = randint(20, int(screen.width) - 40)
                y = randint(80, int(screen.height) - 120)
            except Exception:
                x, y = 100, 200
            heart.pos = (x, y)
            screen.add_widget(heart)
            anim = Animation(y=screen.height + 80, duration=uniform(3.5, 6.0), opacity=0)
            anim.bind(on_complete=lambda *a, h=heart: (h.parent.remove_widget(h) if h.parent else None))
            anim.start(heart)

    def spawn_hearts_periodic(self, dt):
        # called periodically to add subtle hearts
        self.spawn_hearts_once()

    def play_youtube(self, url):
        screen = self.root.get_screen("music")
        if not url or not url.strip():
            return
        if not url.startswith("http"):
            url = "https://" + url
        # if WebView available, load inside app; otherwise open external browser
        try:
            if WebView and hasattr(screen.ids, 'webview'):
                screen.ids.webview.url = url
            else:
                import webbrowser
                webbrowser.open(url)
        except Exception:
            import webbrowser
            webbrowser.open(url)

    def build(self):
        sm = ScreenManager()
        sm.add_widget(HomeScreen(name="home"))
        sm.add_widget(ConvertScreen(name="convert"))
        sm.add_widget(HoroscopeScreen(name="horoscope"))
        sm.add_widget(MusicScreen(name="music"))
        # spawn initial hearts and schedule periodic subtle hearts
        Clock.schedule_once(self.spawn_hearts_once, 1)
        Clock.schedule_interval(self.spawn_hearts_periodic, 12)
        return sm

if __name__ == '__main__':
    RineApp().run()
