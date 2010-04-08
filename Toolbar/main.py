#
#  main.py
#  Toolbar
#
#  Created by Jair Gaxiola on 08/04/10.
#  Copyright __MyCompanyName__ 2010. All rights reserved.
#

#import modules required by application
import objc
import Foundation
import AppKit

from PyObjCTools import AppHelper

import TBController
# import modules containing classes required to start application and load MainMenu.nib
import ToolbarAppDelegate

# pass control to AppKit
AppHelper.runEventLoop()
