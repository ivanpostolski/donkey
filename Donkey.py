import sublime_plugin
import sublime
import subprocess
import os
import re

def get_name(declareFlow):
    return re.split("declare\((\n | \h)?(\s)*flow\(",declareFlow)[-1]

class DonkeyCommand(sublime_plugin.TextCommand):
    def run(self, edit, update=None):
        if (update != None):
            print "yippie kay yay motherfucker"
            return
        flows = self.view.find_all("declare\((\n | \h)?(\s)*flow\(\".*\\\"",0)
        self.flows_names = map(lambda region: get_name(self.view.substr(region)),flows)
        self.flows_names = map(lambda name: "Execute Donkey on : %s" % name, self.flows_names)
        self.view.window().show_quick_panel(self.flows_names, lambda index : self.executeDonkey(index), sublime.MONOSPACE_FONT)

    
    def executeDonkey(self,flowIndex):
        print flowIndex
        donkey = [os.path.join(sublime.packages_path(), 'Donkey', 'lib', "DonkeyUI.py")]
        print donkey
        proc = subprocess.Popen(donkey,stdout=subprocess.PIPE)
