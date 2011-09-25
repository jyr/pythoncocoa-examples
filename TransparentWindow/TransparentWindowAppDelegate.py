#
#   TransparentWindowAppDelegate.py
#
#   Created by Jair Gaxiola on 25/09/11.
#   Copyright 2011 __MyCompanyName__. All rights reserved.
#

from Foundation import *
from AppKit import *
import objc

from TransparentWindow import TransparentWindow

class TransparentWindowAppDelegate (NSObject):
    window = objc.IBOutlet()

    def applicationDidFinishLaunching_(self, sender):
        NSLog("Application did finish launching.")
