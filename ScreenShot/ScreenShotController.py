#
#   ScreenShotController.py
#
#   Created by Jair Gaxiola on 19/08/11.
#   Copyright 2011 __MyCompanyName__. All rights reserved.
#

from Foundation import *
from AppKit import *
import objc
from Quartz import *

class ScreenShotController (NSWindowController):

    def init(self):
		self = super(ScreenShotController, self).initWithWindowNibName_("MainMenu")
		return self

    def awakeFromNib(self):
		screenRect = NSScreen.mainScreen().frame()

		self.window().setFrame_display_(screenRect, YES)
		self.window().setStyleMask_(NSBorderlessWindowMask)
		self.window().setLevel_(NSPopUpMenuWindowLevel)


