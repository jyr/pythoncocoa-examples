#
#  ScreenShotAppDelegate.py
#  ScreenShot
#
#  Created by Jair Gaxiola on 19/08/11.
#  Copyright __MyCompanyName__ 2011. All rights reserved.
#

from Foundation import *
from AppKit import *
from ScreenShotController import ScreenShotController
from ScreenShotView import ScreenShotView

class ScreenShotAppDelegate(NSObject):
    def applicationDidFinishLaunching_(self, sender):
        NSLog("Application did finish launching.")
