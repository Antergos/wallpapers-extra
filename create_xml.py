#!/bin/python

import os

file_names = []
for dpath, d, files in os.walk('.'):
    for fname in files:
        if fname.endswith(".jpg") or fname.endswith(".png"):
            file_names.append(fname)

with open("antergos-extra-backgrounds-4-3.xml", "w") as xml:
    xml.write('<?xml version="1.0" encoding="UTF-8"?>\n')
    xml.write('<!DOCTYPE wallpapers SYSTEM "gnome-wp-list.dtd">\n')
    xml.write('<wallpapers>\n')

    for name in file_names:
        xml.write('<wallpaper>\n')
        xml.write('<name>{}</name>\n'.format(name))
        xml.write('<filename>/usr/share/antergos/wallpapers-extra/{}</filename>\n'.format(name))
        xml.write('<options>zoom</options>\n')
        xml.write('<pcolor>#ffffff</pcolor>\n')
        xml.write('<scolor>#ffffff</scolor>\n')
        xml.write('<shade_type>solid</shade_type>\n')
        xml.write('</wallpaper>\n\n')

    xml.write('</wallpapers>\n')
