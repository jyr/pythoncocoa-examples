#
#  main.py
#  TransparentWindow
#
#  Created by Jair Gaxiola on 25/09/11.
#  Copyright __MyCompanyName__ 2011. All rights reserved.
#

#import modules required by application
import objc
import Foundation
import AppKit

from PyObjCTools import AppHelper

# import modules containing classes required to start application and load MainMenu.nib
import TransparentWindowAppDelegate

# pass control to AppKit
AppHelper.runEventLoop()
