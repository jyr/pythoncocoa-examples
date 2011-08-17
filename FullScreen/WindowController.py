#
#   WindowController.py
#
#   Created by Jair Gaxiola on 17/08/11.
#   Copyright 2011 __MyCompanyName__. All rights reserved.
#

from Foundation import *
from AppKit import *
import objc

class WindowController (NSWindowController):

    def init(self):
		self = super(WindowController, self).initWithWindowNibName_("MainMenu")
		return self

    def awakeFromNib(self):
		screenRect = NSScreen.mainScreen().frame()

		self.window().setFrame_display_(screenRect, YES)
		self.window().setStyleMask_(NSBorderlessWindowMask)
		self.window().setLevel_(NSPopUpMenuWindowLevel)



