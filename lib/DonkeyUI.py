#!/usr/bin/env python

from gi.repository import Gtk,Pango
import threading

class DonkeyWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Donkey")

        self.set_default_size(350, 350)

        self.grid = Gtk.Grid()
        self.add(self.grid)

        self.create_textview()


    def create_textview(self):
        scrolledwindow = Gtk.ScrolledWindow()
        scrolledwindow.set_hexpand(True)
        scrolledwindow.set_vexpand(True)
        self.grid.attach(scrolledwindow, 0, 1, 3, 1)

        self.textview = Gtk.TextView()
        self.textview.set_wrap_mode(3)
        self.textbuffer = self.textview.get_buffer()
        self.textbuffer.set_text("This is some text inside of a Gtk.TextView. "
            + "Select text and click one of the buttons 'bold', 'italic', "
            + "or 'underline' to modify the text accordingly.")

        scrolledwindow.add(self.textview)
        

        self.tag_bold = self.textbuffer.create_tag("bold",
            weight=Pango.Weight.BOLD)
        self.tag_italic = self.textbuffer.create_tag("italic",
            style=Pango.Style.ITALIC)
        self.tag_underline = self.textbuffer.create_tag("underline",
            underline=Pango.Underline.SINGLE)
        self.tag_found = self.textbuffer.create_tag("found",
            background="yellow")

if __name__ == '__main__':
    win = DonkeyWindow()    
    win.connect("delete-event", Gtk.main_quit)
    win.show_all()
    t = threading.Thread(target=Gtk.main)
    t.daemon = False
    t.start()
    print "whatever"
    t.join()
    