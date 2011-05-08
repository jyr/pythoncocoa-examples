#
#  main.py
#  StatusBar
#
#  Created by Jair Gaxiola on 07/05/11.
#  Copyright __MyCompanyName__ 2011. All rights reserved.
#

#import modules required by application
import objc
import Foundation
import AppKit

from PyObjCTools import AppHelper

# import modules containing classes required to start application and load MainMenu.nib
import StatusBarAppDelegate

# pass control to AppKit
AppHelper.runEventLoop()
