#
#   ScreenShotView.py
#
#   Created by Jair Gaxiola on 19/08/11.
#   Copyright 2011 __MyCompanyName__. All rights reserved.
#

from Foundation import *
from AppKit import *
from Quartz import *

import objc
class ScreenShotView (NSView):

    def init(self):
		self = super(ScreenShotController, self).initWithWindowNibName_("MainMenu")
		return self.frameSize

    def awakeFromNib(self):
		screenRect = NSScreen.mainScreen().frame()
		self.setFrameSize_(screenRect.size)
		self.screenshot()

    def screenshot(self):
		screenShot = CGWindowListCreateImage(CGRectInfinite, kCGWindowListOptionAll, kCGNullWindowID, kCGWindowImageDefault)
		self.setOutputImage(screenShot)

    def setOutputImage(self, screenShot):
		if screenShot:
			bitmapRep = NSBitmapImageRep.alloc().initWithCGImage_(screenShot)
			self.image = NSImage.alloc().init()
			self.image.addRepresentation_(bitmapRep)
			self.image.hasAlpha()

    def acceptsFirstResponder(self):
		return YES

    def mouseDown_(self, event):
		NSApp.terminate_(self)
		
    def drawRect_(self, rect):
		colorspace = CGColorSpaceCreateDeviceGray()
		maskContext = CGBitmapContextCreate(None, self.bounds().size.width, self.bounds().size.height, 8, self.bounds().size.width, colorspace, 0)
		CGColorSpaceRelease(colorspace)
		
		maskGraphicsContext = NSGraphicsContext.graphicsContextWithGraphicsPort_flipped_(maskContext, NO)
		NSGraphicsContext.saveGraphicsState()
		NSGraphicsContext.setCurrentContext_(maskGraphicsContext)
		
		NSColor.darkGrayColor().setFill()
		CGContextFillRect(maskContext, rect)
		
		NSGraphicsContext.restoreGraphicsState()
		alphaMask = CGBitmapContextCreateImage(maskContext)
		windowContext = NSGraphicsContext.currentContext().graphicsPort()
		
		CGContextFillRect(windowContext, rect)
		CGContextClipToMask(windowContext, NSRectToCGRect(self.bounds()), alphaMask)

		self.image.drawAtPoint_fromRect_operation_fraction_(NSZeroPoint, NSZeroRect, NSCompositeSourceOver, 1.0)



