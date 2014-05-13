import sublime_plugin
import sublime

def updateFlows(flows,text):
	print text
	return []

def donkey_update(flow2update):
	print flow2update


class CheckUrlsEventListener(sublime_plugin.EventListener):
	def __init__(self):
		super(sublime_plugin.EventListener, self).__init__()
		self.flows = {}
	def on_pre_save(self,view):
		flows2update = updateFlows(self.flows,view.substr(sublime.Region(0,view.size())))
		map(donkey_update,flows2update)	

