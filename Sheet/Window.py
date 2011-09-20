#
#   WindowController.py
#
#   Created by Jair Gaxiola on 20/09/11.
#   Copyright 2011 __MyCompanyName__. All rights reserved.
#

from Foundation import *
from AppKit import *

import objc

class Window (NSWindow):
    sheet = objc.IBOutlet()
    window = objc.IBOutlet()

    @objc.IBAction
    def doneSheet_(self, sender):
		self.sheet.orderOut_(self)
		NSApp.endSheet_(self.sheet)

    @objc.IBAction
    def showSheet_(self, sender):
		NSApp.beginSheet_modalForWindow_modalDelegate_didEndSelector_contextInfo_(self.sheet, self.window, self, None, None)


