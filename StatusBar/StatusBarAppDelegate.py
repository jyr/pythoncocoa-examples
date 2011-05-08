#
#  StatusBarAppDelegate.py
#  StatusBar
#
#  Created by Jair Gaxiola on 07/05/11.
#  Copyright __MyCompanyName__ 2011. All rights reserved.
#

from Foundation import *
from AppKit import *

class StatusBarAppDelegate(NSObject):
    statusMenu = objc.IBOutlet()
    def applicationDidFinishLaunching_(self, sender):
        NSLog("Application did finish launching.")

    def awakeFromNib(self):		
        statusItem = NSStatusBar.systemStatusBar().statusItemWithLength_(NSVariableStatusItemLength).retain()
        statusItem.setMenu_(self.statusMenu)
        statusItem.setTitle_("MNPP")
        statusItem.setHighlightMode_(YES)
