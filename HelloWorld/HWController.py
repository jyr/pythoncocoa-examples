from Foundation import *
from AppKit import *
import objc
class HWController(NSObject):
    message = objc.IBOutlet()

    @objc.IBAction
    def view_(self, sender):
		print self.message.stringValue()

