#
#  ViewAnimationAppDelegate.py
#  ViewAnimation
#
#  Created by Jair Gaxiola on 16/08/11.
#  Copyright __MyCompanyName__ 2011. All rights reserved.
#

from Foundation import *
from AppKit import *
from ViewAnimationController import ViewAnimationController

class ViewAnimationAppDelegate(NSObject):
    def applicationDidFinishLaunching_(self, sender):
        NSLog("Application did finish launching.")
