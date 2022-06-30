#!/usr/bin/env python
# -*- coding: utf-8 -*-

from math import sqrt

from Data.point import Point
from Data.bbox import BBox

class Line(object):
    def __init__(self, start_point=Point(), end_point=Point()):
        self.start_point = start_point
        self.end_point = end_point

        self.diff_point = None
        self.bbox = BBox()
        self.k = None
        self.update()
        return

    def updateDiffPoint(self):
        x_diff = self.end_point.x - self.start_point.x
        y_diff = self.end_point.y - self.start_point.y
        z_diff = self.end_point.z - self.start_point.z
        self.diff_point = Point(x_diff, y_diff, z_diff)
        return True

    def updateBBox(self):
        x_min = min(self.start_point.x, self.end_point.x)
        y_min = min(self.start_point.y, self.end_point.y)
        z_min = min(self.start_point.z, self.end_point.z)
        x_max = max(self.start_point.x, self.end_point.x)
        y_max = max(self.start_point.y, self.end_point.y)
        z_max = max(self.start_point.z, self.end_point.z)

        if not self.bbox.updateBBox(x_min, y_min, z_min, x_max, y_max, z_max):
            print("[ERROR][Line::updateBBox]")
            print("\t updateBBox failed!")
            return False
        return True

    def updateK(self):
        if self.diff_point.x == 0:
            if self.diff_point.y == 0:
                self.k = None
                return True

            self.k = float("inf")
            return True

        self.k = self.diff_point.y / self.diff_point.x
        return True

    def update(self):
        if not self.updateDiffPoint():
            print("[ERROR][Line::update]")
            print("\t updateDiffPoint failed!")
            return False
        if not self.updateBBox():
            print("[ERROR][Line::update]")
            print("\t updateBBox failed!")
            return False
        if not self.updateK():
            print("[ERROR][Line::update]")
            print("\t updateK failed!")
            return False
        return True

    def getLength(self):
        x_diff = self.end_point.x - self.start_point.x
        y_diff = self.end_point.y - self.start_point.y
        length2 = x_diff * x_diff + y_diff * y_diff
        return sqrt(length2)

    def isPoint(self):
        if self.bbox.diff_point.x == 0 and self.bbox.diff_point.y == 0:
            return True
        return False

