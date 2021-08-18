##################################################
#-Pi Quick Tools
#-Coded on 18/08/21
#-Made by Splocko
#-https://github.com/Splocko
#################################################

import os
import gi
import time
gi.require_version('Gtk','3.0')
from gi.repository import Gtk
class window(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self,title='Pi Quick Tools')
        Gtk.Window.set_default_size(self, 640, 480)
        
        self.box = Gtk.Box(spacing=6)
        self.add(self.box)

        self.addButton('Free up space', 'sudo apt -y autoremove\nsudo apt purge\nsudo apt clean', 'Cleaning APT...')
        self.addButton('Update All Packages', 'sudo apt update\nsudo apt -y upgrade', 'Updating all packages... This may take a long time.')
        self.addButton('Reboot', 'sudo reboot')
        self.addButton('Shutdown', 'sudo shutdown now')
        self.addButton('Raspberry Pi Config', f'bash {script_dir}/rpicnfgscrpt.sh')

        
        self.temperature = 0
        self.tempButton = Gtk.Button(label= f'Temperature: {self.temperature}')
        self.tempButton.connect('clicked', self.on_tempButton_clicked)
        self.box.pack_start(self.tempButton, True, True, 0)
#         
#         self.temptext = Gtk.Text(label='asdas')
#         self.box.pack_start(self,temptext, True, True, 0)
    
    def runCommands(self, button, commands, successText, failText, startMessage = None) -> None:
        if startMessage:
            print(startMessage)
        failed = False
        for command in commands:
            if os.system(command.strip()) != 0:
                failed = True
        if failed:
            print(failText)
        else:
            print(successText)

    def addButton(self, buttonName, action, startMessage = None, successText = None, failText = None) -> None:
        
        if not failText:
            failText = f'{buttonName} failed...'
        if not successText:
            successText = f'{buttonName} successful...'

        if str(type(action)) == "<class 'function'>":
            button = Gtk.Button(label = buttonName)
            button.connect('clicked', action)
            self.box.pack_start(button, True, True, 0)
        else:
            button = Gtk.Button(label = buttonName)
            if not type(action) == list:
                if '\n' in action:
                    converted = action.split('\n')
                else:
                    converted = [action]
            else:
                converted = action
            button.connect('clicked', self.runCommands, converted, successText, failText, startMessage)
            self.box.pack_start(button, True, True, 0)      

    def on_tempButton_clicked(self, widget):
        def measure_temp() -> str:
            temp = os.popen("vcgencmd measure_temp").readline()
            return (temp.replace("temp=",""))
        
        while True:
            self.temperature = measure_temp()
            self.tempButton = Gtk.Button(label= f'Temperature: {self.temperature}')
            time.sleep(1)

script_dir = os.path.abspath(os.getcwd())

win = window()
win.connect('destroy', Gtk.main_quit)
win.show_all()
Gtk.main()


