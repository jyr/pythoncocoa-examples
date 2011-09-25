#
#   TransparentWindow.py
#
#   Created by Jair Gaxiola on 25/09/11.
#   Copyright 2011 __MyCompanyName__. All rights reserved.
#

from Foundation import *
from AppKit import *
import objc
class TransparentWindow (NSWindow):

	def initWithContentRect_styleMask_backing_defer_(self, contentRect, aStyle, bufferingType, flag):
		self = super(TransparentWindow, self).initWithContentRect_styleMask_backing_defer_( \
		contentRect, NSBorderlessWindowMask, NSBackingStoreBuffered, YES)
		
		if self:
			self.setAlphaValue_(1.0)
			print dir(self)
			self.setBackgroundColor_(NSColor.clearColor())
			self.setOpaque_(NO)
		
		return self



