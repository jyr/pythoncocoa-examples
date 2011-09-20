#
#  SheetAppDelegate.py
#  Sheet
#
#  Created by Jair Gaxiola on 20/09/11.
#  Copyright __MyCompanyName__ 2011. All rights reserved.
#

from Foundation import *
from AppKit import *
#from WindowController import WindowController
from Window import Window

class SheetAppDelegate(NSObject):
    def applicationDidFinishLaunching_(self, sender):
        NSLog("Application did finish launching.")
