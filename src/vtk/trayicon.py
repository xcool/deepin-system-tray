#! /usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (C) 2012 Deepin, Inc.
#               2012 Hailong Qiu
#
# Author:     Hailong Qiu <356752238@qq.com>
# Maintainer: Hailong Qiu <356752238@qq.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import sys
from Xlib import X, display, error, Xatom, Xutil
from Xlib.ext import shape
import Xlib.protocol.event
import gtk
from gtk import gdk
import gobject 
import select
import random
import cairo



class TrayIcon(gtk.Window):
    def __init__(self):
        gtk.Window.__init__(self)
        self.set_colormap(gtk.gdk.Screen().get_rgba_colormap())
        self.init_values()
        self.init_widgets()
        self.start()

    def init_values(self):
        self.xdisplay = display.Display()
        self.screen = self.xdisplay.screen()
        self.root = self.screen.root
        # init atom.
        self.opcode_atom = self.xdisplay.intern_atom("_NET_SYSTEM_TRAY_OPCODE")
        self.visual_atom = self.xdisplay.intern_atom("_NET_SYSTEM_TRAY_VISUAL")
        atom = "_NET_SYSTEM_TRAY_S%d" % (self.xdisplay.get_default_screen())
        self.manager_atom = self.xdisplay.intern_atom(atom) 
        #self.desktop_atom = self.xdisplay.intern_atom("_NET_WM_DESKTOP")
        #self.xembed_info_atom = self.xdisplay.intern_atom("_XEMBED_INFO")
        # manager.
        self.manager_win = self.xdisplay.get_selection_owner(self.manager_atom)
        #
        self.tray_win = self.xdisplay.create_resource_object("window", self.manager_win.id)
        self.tray_win.get_full_property(self.visual_atom, Xatom.VISUALID)

    def init_widgets(self):
        # setting tray window.
        self.add_events(gtk.gdk.ALL_EVENTS_MASK)
        self.set_decorated(False)
        self.set_app_paintable(True)
        self.set_skip_pager_hint(True)
        self.set_skip_taskbar_hint(True)
        self.set_size_request(120, 24)
        self.show()
        self.plug_xid = self.window.xid
        self.tray_widget_wind = self.xdisplay.create_resource_object("window", self.plug_xid)
        #
        self.show_all()

    def trayicon_motion_notify_evnet(self, widget, event):
        print "trayicon_motion_notify_evnet....."

    def trayicon_button_release_event(self, widget, event):
        print "trayicon_button_press_event......"

    def start(self):
        self.send_event_to_dock(
                        self.tray_win,
                        self.opcode_atom,
                        [X.CurrentTime, 0L, self.tray_widget_wind.id, 0L, 0L],
                        X.NoEventMask)
        self.xdisplay.flush()

    def send_event_to_dock(self,
                           manager_win, 
                           type, 
                           data, 
                           mask):
        data = (data + [0] * (5 - len(data)))[:5]
        # send client message.
        new_event = Xlib.protocol.event.ClientMessage(
                        window = manager_win.id,
                        client_type = type,
                        data = (32, (data)),
                        type = X.ClientMessage
                        )
        manager_win.send_event(new_event, event_mask = mask)
    
    ################################################################
    def get_geometry(self):
        
        return (x, y, w, h) 

        
            

if __name__ == "__main__":
    def tray_time_send(traytime, text, type):
        time_p = None
        if type == TRAY_TIME_12_HOUR:
            time_p = text[0]
        hour = text[0 + type]
        min = text[1 + type]
        #show_str = "%s %s:%s" % (time_p, hour, min)
        #new_trayicon.icon_image.set_label(show_str)

    tray_time = TrayTime()
    tray_time.connect("send-time", tray_time_send)
    new_trayicon = TrayIcon()
    gtk.main()




