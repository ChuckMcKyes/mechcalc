"""
	mechcalc, mechanical engineering tools.
    Copyright (C) 2020, Chuck McKyes

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
# generated by wxGlade 0.8.3 on Thu Apr 23 11:59:03 2020
#

import wx


class Torque(wx.Panel):
    def __init__(self, notebook, wx_id, style):
        super().__init__(notebook, wx_id, style=style)

        # for Torque calculation
        self.text_ctrl_power_in = wx.TextCtrl(self, wx.ID_ANY, "20")
        self.text_ctrl_rpm_in = wx.TextCtrl(self, wx.ID_ANY, "1800")
        self.text_ctrl_torque_out = wx.TextCtrl(self, wx.ID_ANY, "", style=wx.TE_READONLY)
        self.text_ctrl_torque_out_metric = wx.TextCtrl(self, wx.ID_ANY, "", style=wx.TE_READONLY)

        # Bind event handlers
        self.text_ctrl_power_in.Bind(wx.EVT_TEXT, self.on_torque_calculate)
        self.text_ctrl_rpm_in.Bind(wx.EVT_TEXT, self.on_torque_calculate)

        self.__set_properties()
        self.__do_layout()

    def __set_properties(self):
        # begin wxGlade: MyFrame.__set_properties
        # only the top text control in the column needs a minsize
        self.text_ctrl_power_in.SetMinSize((160, 34))
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: MyFrame.__do_layout
        grid_sizer_1 = wx.FlexGridSizer(5, 3, 4, 4)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        label_1 = wx.StaticText(self, wx.ID_ANY, "Torque")
        label_1.SetMinSize((160, 40))
        grid_sizer_1.Add(label_1, 0, wx.EXPAND, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        label_2 = wx.StaticText(self, wx.ID_ANY, "Power", style=wx.ALIGN_RIGHT)
        label_2.SetMinSize((80, 34))
        grid_sizer_1.Add(label_2, 0, wx.EXPAND, 0)
        grid_sizer_1.Add(self.text_ctrl_power_in, 0, wx.EXPAND, 0)
        label_3 = wx.StaticText(self, wx.ID_ANY, "hp")
        label_3.SetMinSize((80, 34))
        grid_sizer_1.Add(label_3, 0, 0, 0)
        label_4 = wx.StaticText(self, wx.ID_ANY, "rpm", style=wx.ALIGN_RIGHT)
        label_4.SetMinSize((80, 34))
        grid_sizer_1.Add(label_4, 0, wx.EXPAND, 0)
        grid_sizer_1.Add(self.text_ctrl_rpm_in, 0, wx.EXPAND, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        label_5 = wx.StaticText(self, wx.ID_ANY, "Torque", style=wx.ALIGN_RIGHT)
        label_5.SetMinSize((80, 34))
        grid_sizer_1.Add(label_5, 0, wx.EXPAND, 0)
        grid_sizer_1.Add(self.text_ctrl_torque_out, 0, wx.EXPAND, 0)
        label_6 = wx.StaticText(self, wx.ID_ANY, u"ft\u2022lbf")
        label_6.SetMinSize((80, 34))
        grid_sizer_1.Add(label_6, 0, 0, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add(self.text_ctrl_torque_out_metric, 0, wx.EXPAND, 0)
        label_8 = wx.StaticText(self, wx.ID_ANY, u"N\u2022m")
        label_8.SetMinSize((80, 34))
        grid_sizer_1.Add(label_8, 0, 0, 0)

        self.SetSizer(grid_sizer_1)
        self.Layout()
        # end wxGlade

    def on_torque_calculate(self, event):  # wxGlade: MyFrame.<event_handler>
        """
        Numbers are entered into power and rpm fields. Non-numbers
        will not be accepted. Calculation is automatic upon entering
        valid numbers.
        """
        power = 0  # to prevent accessing variables before assignment
        rpm = 0
        str_power = (self.text_ctrl_power_in.GetValue())
        acceptable_characters = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '.']

        # If a character entered causes an error, then delete it from the text control
        if str_power:
            # if there are two decimals, delete the last one
            counter = 0
            for character in str_power:
                print(character)
                if character == ".":
                    counter += 1
            if counter > 1:
                str_power = str_power[0:-1]
                self.text_ctrl_power_in.SetValue(str_power)
            # If the entry is too long, delete last character
            if len(str_power) > 8:
                str_power = str_power[0:-1]
                self.text_ctrl_power_in.SetValue(str_power)
            if not (str_power[-1:] in acceptable_characters):
                str_power = str_power[0:-1]
                self.text_ctrl_power_in.SetValue(str_power)
            try:
                power = float(str_power)
            # This prevents more than one decimal "."
            except ValueError:
                print("Invalid input")
                return

        str_rpm = (self.text_ctrl_rpm_in.GetValue())
        if str_rpm:
            # if there are two decimals, delete the last one
            counter = 0
            for character in str_rpm:
                if character == ".":
                    counter += 1
            if counter > 1:
                str_rpm = str_rpm[0:-1]
                self.text_ctrl_rpm_in.SetValue(str_rpm)
            # If the entry is too long, delete last character
            if len(str_rpm) > 8:
                str_rpm = str_rpm[0:-1]
                self.text_ctrl_rpm_in.SetValue(str_rpm)
            if not (str_rpm[-1:] in acceptable_characters):
                str_rpm = str_rpm[0:-1]
                self.text_ctrl_rpm_in.SetValue(str_rpm)
            try:
                rpm = float(str_rpm)
            except ValueError:
                print("Invalid input")
                return

        if power and rpm:
            torque = power * 5252 / rpm
            torque_metric = torque * 1.3558
            torque = "{0:.2f}".format(torque)
            self.text_ctrl_torque_out.SetValue(torque)
            torque_metric = "{0:.2f}".format(torque_metric)
            self.text_ctrl_torque_out_metric.SetValue(torque_metric)
        else:
            self.text_ctrl_torque_out.SetValue("")
            self.text_ctrl_torque_out_metric.SetValue("")
# end class Torque