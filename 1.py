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
        
        self.button1 = Gtk.Button(label='Free up space')
        self.button1.connect('clicked', self.on_button1_clicked)
        self.box.pack_start(self.button1, True, True, 0)

        self.button2 = Gtk.Button(label='Upgrade APT')
        self.button2.connect('clicked', self.on_button2_clicked)
        self.box.pack_start(self.button2, True, True, 0)
        
        self.button3 = Gtk.Button(label='Reboot')
        self.button3.connect('clicked', self.on_button3_clicked)
        self.box.pack_start(self.button3, True, True, 0)
        
        self.button4 = Gtk.Button(label='Shutdown')
        self.button4.connect('clicked', self.on_button4_clicked)
        self.box.pack_start(self.button4, True, True, 0)
        
        self.button5 = Gtk.Button(label='Raspberry \n Pi Config')
        self.button5.connect('clicked', self.on_button5_clicked)
        self.box.pack_start(self.button5, True, True, 0)
        
        self.temperature = 0
        self.button6 = Gtk.Button(label= f'Temperature: {self.temperature}')
        self.button6.connect('clicked', self.on_button6_clicked)
        self.box.pack_start(self.button6, True, True, 0)
#         
#         self.temptext = Gtk.Text(label='asdas')
#         self.box.pack_start(self,temptext, True, True, 0)
        
    def on_button1_clicked(self, widget):
        os.system('echo Cleaning APT...')
        os.system('sudo apt -y autoremove && sudo apt-get purge && sudo apt clean')
        os.system('echo APT cleaning successful')        
 
    def on_button2_clicked(self, widget):
        os.system('echo Updating APT... This may take a long time.')
        os.system('sudo apt-get update && sudo apt -y upgrade')
        os.system('echo APT upgrade successful')
        
    def on_button3_clicked(self,widget):
        os.system('sudo reboot')
    
    def on_button4_clicked(self,widget):
        os.system('sudo shutdown')
        
    def on_button5_clicked(self,widget):
        os.system('bash /home/pi/Pi-Quick-Tools/rpicnfgscrpt.sh')

    def on_button6_clicked(self,widget):
        def measure_temp():
            temp = os.popen("vcgencmd measure_temp").readline()
            return (temp.replace("temp=",""))
        
        while True:
            self.temperature = measure_temp()
            self.button6 = Gtk.Button(label= f'Temperature: {self.temperature}')
            time.sleep(1)



win = window()
win.connect('destroy', Gtk.main_quit)
win.show_all()
Gtk.main()


