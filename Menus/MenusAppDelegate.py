#
#  MenusAppDelegate.py
#  Menus
#
#  Created by Jair Gaxiola on 25/08/09.
#  Copyright __MyCompanyName__ 2009. All rights reserved.
#

from Foundation import *
from AppKit import *

class MenusAppDelegate(NSObject):
    def applicationDidFinishLaunching_(self, sender):
        NSLog("Application did finish launching.")
