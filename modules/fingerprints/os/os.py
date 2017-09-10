#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Spaghetti: Web Application Security Scanner
#
# @url: https://github.com/m4ll0k/Spaghetti
# @author: Momo Outaadi (M4ll0k)
# @license: See the file 'doc/LICENSE'


import bsd
import linux
import mac
import solaris
import unix 
import windows

def Os(headers):
	return (
		bsd.Bsd().run(headers),
		windows.Windows().run(headers),
		linux.Linux().run(headers),
		solaris.Solaris().run(headers),
		unix.Unix().run(headers),
		mac.Mac().run(headers)
		)
