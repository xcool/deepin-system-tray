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

import cairo
import gtk
import math
from vtk.utils import new_surface
from vtk.utils import cairo_popover 
from dtk_cairo_blur import gaussian_blur

SAHOW_VALUE = 3 
ARROW_WIDTH = 20

class TrayIcon(gtk.Window):
    def __init__(self):
        gtk.Window.__init__(self, gtk.WINDOW_TOPLEVEL)
        # init values.
        self.init_values()
        #    
        self.init_trayicon_settings()
        # test.
        self.main_vbox.pack_start(gtk.Button("test"), True, True)
        self.main_vbox.pack_start(gtk.Button("test"), True, True)
        self.main_vbox.pack_start(gtk.Button("test"), True, True)
        #
        self.init_trayicon_events()
        self.show_all()
         
    def init_values(self):
        self.surface = None
        self.old_w = 0
        self.old_h = 0
        self.trayicon_x = SAHOW_VALUE * 2  
        self.trayicon_y = SAHOW_VALUE * 2
        self.trayicon_border = 2.5
        self.radius = 5
        self.arrow_width = ARROW_WIDTH
        self.arrow_height = ARROW_WIDTH/2 
        self.offs = 0
        self.ali_size = 10
    
    def init_trayicon_settings(self):
        self.set_colormap(gtk.gdk.Screen().get_rgba_colormap())
        self.set_modal(True)
        self.set_decorated(False)
        self.set_app_paintable(True)
        self.set_skip_pager_hint(True)
        self.set_skip_taskbar_hint(True)
        self.set_position(gtk.WIN_POS_NONE)
        self.set_type_hint(gtk.gdk.WINDOW_TYPE_HINT_MENU)
        self.set_opacity(0.9)
        self.set_size_request(350, 290)
        self.main_vbox = gtk.VBox()
        self.draw = gtk.EventBox()
        self.ali  = gtk.Alignment(0, 0, 1, 1)
        self.ali.set_padding(self.ali_size + int(self.trayicon_x + self.arrow_height),
                             int(self.ali_size + self.trayicon_x),
                             int(self.ali_size + self.trayicon_x),
                             int(self.ali_size + self.trayicon_x))
        self.add(self.draw)
        self.draw.add(self.ali)
        self.ali.add(self.main_vbox)
    
    def init_trayicon_events(self):
        self.connect("size-allocate", self.on_size_allocate)
        self.draw.connect("expose-event", self.draw_expose_event)

    def draw_expose_event(self, widget, event):
        cr = widget.window.cairo_create()
        rect = widget.allocation
        #
        cr.rectangle(*rect)
        cr.set_source_rgba(1, 1, 1, 0.0)
        cr.set_operator(cairo.OPERATOR_SOURCE)
        cr.paint()

        cr = widget.window.cairo_create()
        x, y, w, h = rect
        self.expose_event_draw(cr)
        #
        try:
            widget.propagate_expose(widget.get_child(), event)
        except:
            pass
        return True

    def on_size_allocate(self, widget, alloc):
        x, y, w, h = self.allocation
        # !! no expose and blur.
        if (self.old_w == w and self.old_h == h):
            return False
        # 
        self.surface, self.surface_cr = new_surface(w, h)
        self.compute_shadow(w, h)
        self.old_w = w
        self.old_h = h

    def compute_shadow(self, w, h):
        # sahow.
        cairo_popover(self, self.surface_cr, 
                      self.trayicon_x, self.trayicon_y, 
                      w, h,
                      self.radius, self.arrow_width, self.arrow_height, self.offs)
        gaussian_blur(self.surface, SAHOW_VALUE)
        self.surface_cr.set_source_rgba(1.0, 0.0, 0.0, 0.9)
        self.surface_cr.fill_preserve()
        gaussian_blur(self.surface, SAHOW_VALUE)
        # border.
        self.surface_cr.clip()
        cairo_popover(self, self.surface_cr, 
                      self.trayicon_x + self.trayicon_border, self.trayicon_y + self.trayicon_border, 
                      w, h, 
                      self.radius, self.arrow_width, self.arrow_height, self.offs) 
        self.surface_cr.set_source_rgba(0, 0, 0, 1.0)
        self.surface_cr.set_line_width(self.border_width)
        self.surface_cr.fill_preserve()
        #
        self.surface_cr.clip()
        cairo_popover(self, self.surface_cr, 
                      self.trayicon_x + self.trayicon_border + 1, 
                      self.trayicon_y + self.trayicon_border + 1, 
                      w, h, 
                      self.radius, self.arrow_width, self.arrow_height, self.offs) 
        self.surface_cr.set_source_rgba(1, 1, 1, 1.0)
        self.surface_cr.set_line_width(self.border_width)
        self.surface_cr.fill()

    def expose_event_draw(self, cr):
        if self.surface:
            cr.set_source_surface(self.surface, 0, 0)
            #cr.paint_with_alpha(1.0)
            cr.paint()
        
if __name__ == "__main__":
    TrayIcon()
    gtk.main()