#
#  main.py
#  FullScreen
#
#  Created by Jair Gaxiola on 16/08/11.
#  Copyright __MyCompanyName__ 2011. All rights reserved.
#

#import modules required by application
import objc
import Foundation
import AppKit

from PyObjCTools import AppHelper

# import modules containing classes required to start application and load MainMenu.nib
import FullScreenAppDelegate

from WindowController import WindowController

# pass control to AppKit
AppHelper.runEventLoop()
