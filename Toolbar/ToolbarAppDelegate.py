#
#  ToolbarAppDelegate.py
#  Toolbar
#
#  Created by Jair Gaxiola on 08/04/10.
#  Copyright __MyCompanyName__ 2010. All rights reserved.
#

from Foundation import *
from AppKit import *

class ToolbarAppDelegate(NSObject):
    def applicationDidFinishLaunching_(self, sender):
        NSLog("Application did finish launching.")
