from Foundation import *
from AppKit import *
import objc

class MenusController(NSObject):
    message = objc.IBOutlet()

    @objc.IBAction
    def runItem1_(self, sender):
		self.message.setStringValue_('Item 1')

    @objc.IBAction
    def runItem2_(self, sender):
		self.message.setStringValue_('Item 2')
		
    @objc.IBAction
    def runItem3_(self, sender):
		self.message.setStringValue_('Item 3')