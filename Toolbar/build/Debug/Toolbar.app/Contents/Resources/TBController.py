from Foundation import *
from AppKit import *
import objc
class TBController (NSObject):
    message = objc.IBOutlet()

    @objc.IBAction
    def runText_(self, sender):
		self.message.setStringValue_('Text')
		print "Text"

    @objc.IBAction
    def runPhoto_(self, sender):
		self.message.setStringValue_('Photo')
		print "Photo"
		
    @objc.IBAction
    def runQuote_(self, sender):
		self.message.setStringValue_('Quote')
		print "Quote"
		
    @objc.IBAction
    def runLink_(self, sender):
		self.message.setStringValue_('Link')
		print "Link"
		
    @objc.IBAction
    def runChat_(self, sender):
		self.message.setStringValue_('Chat')
		print "Chat"
		
    @objc.IBAction
    def runAudio_(self, sender):
		self.message.setStringValue_('Audio')
		print "Audio"
		
    @objc.IBAction
    def runVideo_(self, sender):
		self.message.setStringValue_('Video')
		print "Video"
