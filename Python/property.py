#!/usr/bin/python3

###############################################################################
#
#study to use @property
#
#############################################################################


class Screen(object):
    @property
    def wdith(self):
        return self.wdith

    @wdith.setter
    def wdith(self, value):
        self._wdith = value

    @property
    def heigh(self):
        return heigh
    @heigh.setter
    def heigh(self, value):
        self._heigh = value

    @property
    def resolution(self):
        return self._heigh * self._wdith
