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


def tray_icon_expose_event(widget, event):
    cr = widget.window.cairo_create()
    rect = widget.allocation
    surface = 
    surface_cr.
    cairo_popover(w, h)
    # shadow.
    surface_cr.set_source_rgba(0, 0, 0, 0.9)
    surface_cr.fill_preserve()
    exponential_blur(6)
    curface_cr.clip()
    # background.
    # get_style_context()
    surface_cr.reset_clip()
    # border.
    cairo_popover(w, h)
    surface_cr.set_operator(cairo.OPERATOR_SOURCE)
    surface_cr.set_line_width(1)
    surface_cr.set_source_rgba(0, 0, 0, 0.9)
    surface_cr.stroke()
    # clear furface/
    cr.set_operator(cairo.OPERATOR_SOURCE)
    cr.set_source_rgba(0, 0, 0, 0.9)
    cr.paint()
    #
    cr.set_source_surface(surface, 0, 0)
    cr.patint()
    return False