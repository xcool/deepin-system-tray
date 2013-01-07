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


import math

def cairo_rounded_rectangle(cr, x, y, width, height, radius):
    cr.move_to (x + radius, y)
    cr.arc (x + width - radius, 
            y + radius, 
            radius, 
            math.pi * 1.5,
            math.pi * 2)
    cr.arc (x + width - radius,
            y + radius,
            radius,
            0,
            math.pi * 0.5)
    cr.arc (x + radius,
            y + height - radius,
            radius,
            math.pi * 0.5,
            math.pi)
    cr.arc (x + radius,
            y + radius,
            radius,
            math.pi,
            math.pi * 1.5)
    cr.close_path()

def cairo_popover (widget, 
                   cr, w, h, 
                   arrow_width=20, arrow_height=10):
    w = w - 20
    h = h - 20
    offs = 30
    p_x = widget.window.get_origin()[0]
    alloc = widget.get_allocation()
    #
    #offs = (p_x + alloc.x) - w_x + this.get_
    offs = -1
    if (offs + 50) > (w + 20):
        offs = (w + 20) - 15 - arrow_width
    if (offs < 17):
        offs = 17
    # draw.
    cr.arc (x + radius,
            y + arrow_height + radius,
            radius,
            math.pi,
            math.pi * 1.5)
    cr.line_to(offs, y + arrow_height)
    cr.rel_line_to(arrow_width / 2.0, -arrow_height)
    cr.rel_line_to(arrow_width / 2.0, arrow_height)
    cr.arc (x + w - radius,
            y + arrow_height + radius,
            radius,
            math.pi * 1.5,
            math.pi * 2.0)
    cr.arc(x + w - radius,
           y + h - radius,
           radius,
           0,
           math.pi * 0.5)
    cr.arc(x + w - radius,
           y + h - radius,
           radius,
           math.pi * 0.5,
           math.pi)
    
    cr.close_path()

