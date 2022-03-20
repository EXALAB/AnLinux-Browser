#!/usr/bin/python3
# -*- coding: utf-8 -*-
import configparser
from pathlib import Path

from pgi import require_version

require_version('Gtk', '3.0')
require_version('WebKit2', '4.0')
config = configparser.ConfigParser()

from pgi.repository import Gtk, WebKit2

current_path = Path(__file__).parent.resolve()


class Browser:
    def __init__(self):
        self.builder = Gtk.Builder()

        self.builder.add_from_file("core/browser.glade")
        self.builder.connect_signals(self)

        self.toolbar1 = self.builder.get_object("toolbar1")
        self.back = self.builder.get_object("back")
        self.forward = self.builder.get_object("forward")
        self.refresh = self.builder.get_object("refresh")
        self.stop = self.builder.get_object("stop")
        self.url = self.builder.get_object("url")
        self.spinner = self.builder.get_object("spinner")
        self.progressbar = self.builder.get_object("progressbar")
        self.window = self.builder.get_object("window1")
        self.window.connect('destroy', lambda w: Gtk.main_quit())
        self.scrolled_window = self.builder.get_object("scrolledwindow")
        self.window.show_all()

        self.webview = WebKit2.WebView()
        self.scrolled_window.add(self.webview)
        self.webview.load_uri(config.get("DEFAULT", "HomePage", fallback="https://start.starinc.xyz"))
        # self.webview.connect('title-changed', self.change_title)
        # self.webview.connect('load-committed', self.change_url)
        # self.webview.connect('load-committed', self.spinner_on)
        # self.webview.connect('load_finished', self.spinner_off)
        # self.webview.connect('load-committed', self.progress_on)
        # self.webview.connect('load-progress-changed', self.progress_change)
        # self.webview.connect('document_load_finished',self.progress_off)
        self.webview.show()

    def on_url_activate(self, widget):
        url = widget.get_text()
        if url.startswith('http://') or url.startswith('https://'):
            self.webview.load_uri(url)
        else:
            url = 'https://' + url
            self.url.set_text(url)
            self.webview.load_uri(url)

    def on_refresh_clicked(self, widget):
        self.webview.reload()

    def on_back_clicked(self, widget):
        self.webview.go_back()

    def on_forward_clicked(self, widget):
        self.webview.go_forward()

    def on_stop_clicked(self, widget):
        self.webview.stop_loading()

    def change_title(self, widget, frame, title):
        self.window.set_title(title + ' - AnLinux-Browser')

    def change_url(self, widget, frame):
        uri = frame.get_uri()
        self.url.set_text(uri)
        self.back.set_sensitive(self.webview.can_go_back())
        self.forward.set_sensitive(self.webview.can_go_forward())

    def spinner_on(self, widget, frame):
        self.spinner.start()

    def spinner_off(self, widget, frame):
        self.spinner.stop()

    # def progress_on(self,widget,frame):
    # self.progressbar.pulse()

    # def progress_change(self,wiget,frame):
    #  self.progressbar.set_pulse_step(.5)

    # def progress_off(self,widget,frame):
    # self.progressbar.set_pulse_step(0)


def main():
    app = Browser()
    Gtk.main()


if __name__ == "__main__":
    main()
