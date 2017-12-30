__version__ = '0.1'

from kivy.app import App

from kivy.uix.widget import Widget
from kivy.clock import Clock
from jnius import autoclass
from android.runnable import run_on_ui_thread


WebView = autoclass('android.webkit.WebView')
WebViewClient = autoclass('android.webkit.WebViewClient')
activity = autoclass('org.renpy.android.PythonActivity').mActivity


class Wv(Widget):
    def __init__(self, **kwargs):
        super(Wv, self).__init__(**kwargs)
        Clock.schedule_once(self.create_webview, 0)

    @run_on_ui_thread
    def create_webview(self, *args):
        webview = WebView(activity)
        settings = webview.getSettings()
        settings.setJavaScriptEnabled(True)
        settings.setUseWideViewPort(True) # enables viewport html meta tags
        settings.setLoadWithOverviewMode(True) # uses viewport
        settings.setSupportZoom(True) # enables zoom
        settings.setBuiltInZoomControls(True) # enables zoom controls
        wvc = WebViewClient()
        webview.setWebViewClient(wvc)
        activity.setContentView(webview)
        webview.loadUrl('http://localhost:23948')  # use 10.0.2.2 on Android emulators instead of localhost

class WebviewApp(App):
    def build(self):
        return Wv()

class WebserverService(App):
    def build(self):
        self.start_service()

    def start_service(self):
        from android import AndroidService
        service = AndroidService('ZimAndroidWebserver', 'running')  # this will launch what is in the folder service/main.py as a service
        service.start('ZimAndroidWebserver service started')
        self.service = service

    def stop_service(self):
        if self.service:
            self.service.stop()
            self.service = None


if __name__ == '__main__':
    WebserverService().run()
    WebviewApp().run()
