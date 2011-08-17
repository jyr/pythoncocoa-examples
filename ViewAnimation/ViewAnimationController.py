#
#   ViewAnimationController.py
#
#   Created by Jair Gaxiola on 17/08/11.
#   Copyright 2011 __MyCompanyName__. All rights reserved.
#

from Foundation import *
from AppKit import *
import objc
class ViewAnimationController (NSObject):
    box = objc.IBOutlet()
    transitionSelector = objc.IBOutlet()
    view1 = objc.IBOutlet()
    view2 = objc.IBOutlet()

    def awakeFromNib(self):
		rect = self.box.bounds()
		
		"""
		Set up intermediary views and stick the views inside it. These views
		acts as viewports to the "real" views.
		"""
		tempView = NSView.alloc().initWithFrame_(rect)
		tempView.addSubview_(self.view1)
		tempView.setAutoresizingMask_(self.box.autoresizingMask())
		self.box.addSubview_(tempView)
		
		rect = tempView.bounds()
		self.view1.setFrame_(rect)
		self.view1 = tempView
		
		tempView = NSView.alloc().initWithFrame_(rect)
		tempView.addSubview_(self.view2)
		tempView.setAutoresizingMask_(self.box.autoresizingMask())
		self.box.addSubview_(tempView)
		
		rect = tempView.bounds()
		tempView.setHidden_(YES)
		self.view2.setFrame_(rect)
		self.view2 = tempView
	
    def prepSubviewOfView(self, view):
		subview = view.subviews().objectAtIndex_(0)
		subview.setFrameOrigin_(NSZeroPoint)
		"""
		Reset the mask and let each animation turn on whatever resizing options it needs
		"""
		subview.setAutoresizingMask_(NSViewNotSizable)

    def resetSubviewOfView(self, view):
		subview = view.subviews().objectAtIndex_(0)
		subview.setFrameOrigin_(NSZeroPoint)
		"""
		Allow the views to resize properly now that the animation is done.
		"""
		subview.setAutoresizingMask_(self.box.autoresizingMask())

    @objc.IBAction
    def doTransition_(self, sender):

		transitionType = self.transitionSelector.selectedTag()
		rect = self.box.bounds()

		if self.view1.isHidden():
			newView = self.view1
			oldView = self.view2
		else:
			newView = self.view2
			oldView = self.view1
		
		"""
		Unset the first responder. Can cause drawing artifacts since the blue glow extends beyond the view's bounds.
		"""
		self.box.window().makeFirstResponder_(None)
		
		"""
		Turn off all autoresizing for now. Will be twiddling these for different effects.
		"""
		self.prepSubviewOfView(newView)
		self.prepSubviewOfView(oldView)
		
		case = {0: self.dissolve, 1: self.move_in, 2: self.push, 3:self.reveal, \
				4:self.wipe, 5:self.down, 6:self.up, 7:self.down_up, 8:self.reveal_right, 9:self.push_right}
		
		animation = case[transitionType](oldView, newView, rect)
		
		animation.setAnimationBlockingMode_(NSAnimationBlocking)
		animation.startAnimation()
		#animation.release()
		
		"""
		Not all the animations above result in the old view being hidden so do it here
		"""
		oldView.setHidden_(YES)
		
		self.resetSubviewOfView(oldView)
		self.resetSubviewOfView(newView)


    def dissolve(self, oldView, newView, rect):
		newView.setFrame_(rect)
		"""
		Old view is set to fade out
		"""
		dictoldView = NSDictionary.dictionaryWithObjectsAndKeys_( \
		oldView, NSViewAnimationTargetKey, NSViewAnimationFadeOutEffect, NSViewAnimationEffectKey, None)
		"""
		New view is set to fade in
		"""
		dictnewView = NSDictionary.dictionaryWithObjectsAndKeys_( \
		newView, NSViewAnimationTargetKey, NSViewAnimationFadeInEffect, NSViewAnimationEffectKey, None)
		array = NSArray.arrayWithObjects_(dictoldView, dictnewView, None)

		"""
		Note: view does not need to be unhidden manually as in the other cases. This is because the fade in
		effect will do it for you.
		"""
		animation = NSViewAnimation.alloc().initWithViewAnimations_(array)
		
		return animation

    def move_in(self, oldView, newView, rect):
		"""
		Set the old view to be resizable on the right side. It will appear as if it's sitting still
		"""
		oldView.subviews().objectAtIndex_(0).setAutoresizingMask_(NSViewMaxXMargin)
		
		"""
		Set the new view to be out of bounds on the right side, ready to be animated in
		"""
		newView.setFrame_(NSMakeRect(NSMaxX(rect), NSMinY(rect), NSWidth(rect), NSHeight(rect)))
		"""
		If a previous animation resulted in a zero frame, it set it to hidden. We have to unhide it manually.
		"""
		newView.setHidden_(NO)
		
		"""
		The left "viewport" shrinks to zero-width on the left side
		"""
		dictoldView = NSDictionary.dictionaryWithObjectsAndKeys_( \
		oldView, NSViewAnimationTargetKey, NSValue.valueWithRect_( \
		NSMakeRect(NSMinX(rect), NSMinY(rect), 0.0, NSHeight(rect))), NSViewAnimationEndFrameKey, None)
		"""
		New view frame is just the viewable area. Since it is currently out of bounds, it will appear to slide
		in bounds.
		"""
		dictnewView = NSDictionary.dictionaryWithObjectsAndKeys_( \
		newView, NSViewAnimationTargetKey, NSValue.valueWithRect_(rect), NSViewAnimationEndFrameKey, None)
		
		array = NSArray.arrayWithObjects_(dictoldView, dictnewView, None)
		animation = NSViewAnimation.alloc().initWithViewAnimations_(array)

		return animation

    def push(self, oldView, newView, rect):
		"""
		Set old view to be resizable on the left side. It will appear to move to the left since the right margin is
		fixed.
		"""
		oldView.subviews().objectAtIndex_(0).setAutoresizingMask_(NSViewMinXMargin)
		
		"""
		Set the new view to be out of bounds on the right side, ready to be animated in
		"""
		newView.setFrame_(NSMakeRect(NSMaxX(rect), NSMinY(rect), NSWidth(rect), NSHeight(rect)))
		"""
		If a previous animation resulted in a zero frame, it set it to hidden. We have to unhide it manually.
		"""
		newView.setHidden_(NO)
		
		"""
		Old view frame gets moved to the left, out of bounds.
		"""
		dictoldView = NSDictionary.dictionaryWithObjectsAndKeys_( \
		oldView, NSViewAnimationTargetKey, NSValue.valueWithRect_( \
		NSMakeRect(NSMinX(rect), NSMinY(rect), NSMinY(rect), NSHeight(rect))), NSViewAnimationEndFrameKey, None)

		"""
		New view frame is just the viewable area. Since it is currently out of bounds, it will appear to slide
		in bounds. Note, this is the same as in the "Move In" case.
		"""
		dictnewView = NSDictionary.dictionaryWithObjectsAndKeys_( \
		newView, NSViewAnimationTargetKey, NSValue.valueWithRect_(rect), NSViewAnimationEndFrameKey, None)
		
		array = NSArray.arrayWithObjects_(dictoldView, dictnewView, None)
		animation = NSViewAnimation.alloc().initWithViewAnimations_(array)
		
		return animation

    def reveal(self, oldView, newView, rect):
		"""
		Set old view to be resizable on the left side. It will appear to move to the left since the right margin is
		fixed.
		"""
		oldView.subviews().objectAtIndex_(0).setAutoresizingMask_(NSViewMinXMargin)
		
		"""
		Set new view to be resizable on the right side. It will appear to sit still.
		"""
		newView.subviews().objectAtIndex_(0).setAutoresizingMask_(NSViewMinXMargin)
		
		"""
		Make the right viewport zero-width view on the right side. It will reveal the view as it expands to the left.
		"""
		newView.setFrame_(NSMakeRect(NSMaxX(rect), NSMinY(rect), 0.0, NSHeight(rect)))
		newView.setHidden_(NO)
		
		"""
		Make the subview such that it's right edge is flush with its superview/viewport.
		"""
		newView.subviews().objectAtIndex_(0).setFrame_( \
		NSMakeRect(NSMinX(rect) - NSWidth(rect), NSMinY(rect), NSWidth(rect), NSHeight(rect)))
		
		"""
		The left "viewport" shrinks to zero-width
		"""
		dictoldView = NSDictionary.dictionaryWithObjectsAndKeys_( \
		oldView, NSViewAnimationTargetKey, NSValue.valueWithRect_( \
		NSMakeRect(NSMinX(rect), NSMinY(rect), 0.0, NSHeight(rect))), NSViewAnimationEndFrameKey, None)
		"""
		The right view port expands to encompass the full bounds.
		"""
		dictnewView = NSDictionary.dictionaryWithObjectsAndKeys_( \
		newView, NSViewAnimationTargetKey, NSValue.valueWithRect_(rect), NSViewAnimationEndFrameKey, None)
		
		array = NSArray.arrayWithObjects_(dictoldView, dictnewView, None)
		animation = NSViewAnimation.alloc().initWithViewAnimations_(array)
		
		return animation

    def wipe(self, oldView, newView, rect):
		"""
		Set the old view to be resizable on the right side. It will appear as if it's sitting still
		"""
		oldView.subviews().objectAtIndex_(0).setAutoresizingMask_(NSViewMaxXMargin)
		
		"""
		Set new view to be resizable on the right side. It will appear to sit still.
		"""
		newView.subviews().objectAtIndex_(0).setAutoresizingMask_(NSViewMinXMargin)
		
		"""
		Make the right viewport zero-wdith
		"""
		newView.setFrame_(NSMakeRect(NSMaxX(rect), NSMinY(rect), 0.0, NSHeight(rect)))
		newView.setHidden_(NO)
		
		"""
		Make the subview such that it's right edge is flush with its superview/viewport.
		"""
		newView.subviews().objectAtIndex_(0).setFrame_(\
		NSMakeRect(NSMinX(rect) - NSWidth(rect), NSMinY(rect), NSWidth(rect), NSHeight(rect)))
		
		"""
		The left "viewport" shrinks to zero-width
		"""
		dictoldView = NSDictionary.dictionaryWithObjectsAndKeys_( \
		oldView, NSViewAnimationTargetKey, NSValue.valueWithRect_(NSMakeRect(NSMinX(rect), NSMinY(rect), 0.0, NSHeight(rect))), NSViewAnimationEndFrameKey, None)

		"""
		The right view port expands to encompass the full bounds.
		"""
		dictnewView = NSDictionary.dictionaryWithObjectsAndKeys_( \
		newView, NSViewAnimationTargetKey, NSValue.valueWithRect_(rect), NSViewAnimationEndFrameKey, None)
		
		array = NSArray.arrayWithObjects_(dictoldView, dictnewView, None)
		animation = NSViewAnimation.alloc().initWithViewAnimations_(array)
		
		return animation

    def down(self, oldView, newView, rect):
		"""
		Set old view to be resizable on the left side. It will appear to move to the left since the right margin is
		fixed.
		"""
		oldView.subviews().objectAtIndex_(0).setAutoresizingMask_(NSViewMinYMargin)
		
		"""
		Set the new view to be out of bounds on the right side, ready to be animated in
		"""
		newView.setFrame_(NSMakeRect(NSMinX(rect), NSMaxY(rect), NSWidth(rect), NSHeight(rect)))
		
		"""
		If a previous animation resulted in a zero frame, it set it to hidden. We have to unhide it manually.
		"""
		newView.setHidden_(NO)

		"""
		Old view frame gets moved to the left, out of bounds.
		"""
		dictoldView = NSDictionary.dictionaryWithObjectsAndKeys_( \
		oldView, NSViewAnimationTargetKey, NSValue.valueWithRect_(NSMakeRect(NSMinX(rect), - NSMaxY(rect), NSWidth(rect), NSHeight(rect))), NSViewAnimationEndFrameKey, None)

		"""
		New view frame is just the viewable area. Since it is currently out of bounds, it will appear to slide
		in bounds. Note, this is the same as in the "Move In" case.
		"""
		dictnewView = NSDictionary.dictionaryWithObjectsAndKeys_( \
		newView, NSViewAnimationTargetKey, NSValue.valueWithRect_(rect), NSViewAnimationEndFrameKey, None)
		array = NSArray.arrayWithObjects_(dictoldView, dictnewView, None)
		animation = NSViewAnimation.alloc().initWithViewAnimations_(array)
		
		return animation

    def down_up(self, oldView, newView, rect):
		"""
		Set old view to be resizable on the left side. It will appear to move to the left since the right margin is
		fixed.
		"""
		oldView.subviews().objectAtIndex_(0).setAutoresizingMask_(NSViewMinXMargin)
		
		"""
		Set the new view to be out of bounds on the right side, ready to be animated in
		"""
		newView.setFrame_(NSMakeRect(NSMinX(rect), NSMaxY(rect), NSWidth(rect), NSHeight(rect)))
		"""
		If a previous animation resulted in a zero frame, it set it to hidden. We have to unhide it manually.
		"""
		newView.setHidden_(NO)
		
		"""
		Old view frame gets moved to the left, out of bounds.
		"""
		dictoldView = NSDictionary.dictionaryWithObjectsAndKeys_( \
		oldView, NSViewAnimationTargetKey, NSValue.valueWithRect_( \
		NSMakeRect(NSMinX(rect), NSMaxY(rect), NSWidth(rect), NSHeight(rect))), NSViewAnimationEndFrameKey, None)
	
		"""
		New view frame is just the viewable area. Since it is currently out of bounds, it will appear to slide
		in bounds. Note, this is the same as in the "Move In" case.
		"""
		dictnewView = NSDictionary.dictionaryWithObjectsAndKeys_(\
		newView, NSViewAnimationTargetKey, NSValue.valueWithRect_(rect), NSViewAnimationEndFrameKey, None)
		
		array = NSArray.arrayWithObjects_(dictoldView, dictnewView, None)
		animation = NSViewAnimation.alloc().initWithViewAnimations_(array)
		
		return animation
		
    def up(self, oldView, newView, rect):
		"""
		Set old view to be resizable on the left side. It will appear to move to the left since the right margin is
		fixed.
		"""
		oldView.subviews().objectAtIndex_(0).setAutoresizingMask_(NSViewMaxXMargin)
		
		"""
		Set the new view to be out of bounds on the right side, ready to be animated in
		"""
		newView.setFrame_(NSMakeRect(NSMinX(rect), - NSMaxY(rect), NSWidth(rect), NSHeight(rect)))
		
		"""
		If a previous animation resulted in a zero frame, it set it to hidden. We have to unhide it manually.
		"""
		newView.setHidden_(NO)

		"""
		Old view frame gets moved to the left, out of bounds.
		"""
		dictoldView = NSDictionary.dictionaryWithObjectsAndKeys_( \
		oldView, NSViewAnimationTargetKey, NSValue.valueWithRect_( \
		NSMakeRect(NSMinX(rect),  NSMaxY(rect), NSWidth(rect), NSHeight(rect))), NSViewAnimationEndFrameKey, None)

		"""
		New view frame is just the viewable area. Since it is currently out of bounds, it will appear to slide
		in bounds. Note, this is the same as in the "Move In" case.
		"""
		dictnewView = NSDictionary.dictionaryWithObjectsAndKeys_( \
		newView, NSViewAnimationTargetKey, NSValue.valueWithRect_( \
		NSMakeRect(0.0,  0.0, NSWidth(rect), NSHeight(rect))), NSViewAnimationEndFrameKey, None)
		
		array = NSArray.arrayWithObjects_(dictoldView, dictnewView, None)
		animation = NSViewAnimation.alloc().initWithViewAnimations_(array)
		
		return animation

    def reveal_right(self, oldView, newView, rect):
		"""
		Set old view to be resizable on the left side. It will appear to move to the left since the right margin is
		fixed.
		"""
		oldView.subviews().objectAtIndex_(0).setAutoresizingMask_(NSViewMinXMargin)
		
		"""
		Set the new view to be out of bounds on the right side, ready to be animated in
		"""
		newView.setFrame_(NSMakeRect(-NSMaxX(rect), NSMinY(rect), NSWidth(rect), NSHeight(rect)))
		"""
		If a previous animation resulted in a zero frame, it set it to hidden. We have to unhide it manually.
		"""
		newView.setHidden_(NO)
		
		"""
		Old view frame gets moved to the left, out of bounds.
		"""
		dictoldView = NSDictionary.dictionaryWithObjectsAndKeys_( \
		oldView, NSViewAnimationTargetKey, NSValue.valueWithRect_( \
		NSMakeRect(NSMaxX(rect), NSMinY(rect), NSMinY(rect), NSHeight(rect))), NSViewAnimationEndFrameKey, None)

		"""
		New view frame is just the viewable area. Since it is currently out of bounds, it will appear to slide
		in bounds. Note, this is the same as in the "Move In" case.
		"""
		dictnewView = NSDictionary.dictionaryWithObjectsAndKeys_( \
		newView, NSViewAnimationTargetKey, NSValue.valueWithRect_(rect), NSViewAnimationEndFrameKey, None)
		
		array = NSArray.arrayWithObjects_(dictoldView, dictnewView, None)
		animation = NSViewAnimation.alloc().initWithViewAnimations_(array)
		
		return animation

    def push_right(self, oldView, newView, rect):
		"""
		Set old view to be resizable on the left side. It will appear to move to the left since the right margin is
		fixed.
		"""
		oldView.subviews().objectAtIndex_(0).setAutoresizingMask_(NSViewMinXMargin)
		
		"""
		Set the new view to be out of bounds on the right side, ready to be animated in
		"""
		newView.setFrame_(NSMakeRect(-NSMaxX(rect), NSMinY(rect), NSWidth(rect), NSHeight(rect)))
		"""
		If a previous animation resulted in a zero frame, it set it to hidden. We have to unhide it manually.
		"""
		newView.setHidden_(NO)
		
		"""
		Old view frame gets moved to the left, out of bounds.
		"""
		dictoldView = NSDictionary.dictionaryWithObjectsAndKeys_( \
		oldView, NSViewAnimationTargetKey, NSValue.valueWithRect_( \
		NSMakeRect(NSMaxX(rect) * 2, NSMinX(rect), NSMinY(rect), NSHeight(rect))), NSViewAnimationEndFrameKey, None)

		"""
		New view frame is just the viewable area. Since it is currently out of bounds, it will appear to slide
		in bounds. Note, this is the same as in the "Move In" case.
		"""
		dictnewView = NSDictionary.dictionaryWithObjectsAndKeys_( \
		newView, NSViewAnimationTargetKey, NSValue.valueWithRect_(rect), NSViewAnimationEndFrameKey, None)
		
		array = NSArray.arrayWithObjects_(dictoldView, dictnewView, None)
		animation = NSViewAnimation.alloc().initWithViewAnimations_(array)
		
		return animation