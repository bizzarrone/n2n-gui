#!/usr/bin/env python

# Would like to show online status of hosts (useful for n2n vpn program )
 
import pygtk
pygtk.require('2.0')
import gtk
#import argparse
import os
#import stat

def pinger(host):
	#host = "google.com" #example
	response = os.system("ping -q -q -w 1 " + host + " > /dev/null ")

	if response == 0:
	  #print host, 'is up!'
	  out="ONLINE"
	else:
	  #print host, 'is down!'
	  out="offline"
        return out

class BasicListViewExample:
    def __init__(self):
        '''Create a new window'''
        # we create a top level window and we set some parameters on it
        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        self.window.set_title("N2N network status by Luca Carrozza")
        self.window.set_size_request(300, 400)
        self.window.set_border_width(10)
        self.window.set_position(gtk.WIN_POS_CENTER_ALWAYS)
 
        # Here we connect the "destroy" event to a signal handler.
        # This event occurs when we call gtk_widget_destroy() on the window,
        # or if we return FALSE in the "delete_event" callback.
        self.window.connect("destroy", self.destroy)
 
        # create a Vbox - a vertical container box
        # param: homogeneous, spacing
        vbox = gtk.VBox(False, 8)
 
        # create a scrollable window and integrate it into the vbox
        sw = gtk.ScrolledWindow()
        sw.set_shadow_type(gtk.SHADOW_ETCHED_IN)
        sw.set_policy(gtk.POLICY_AUTOMATIC, gtk.POLICY_AUTOMATIC)
        # def pack_start(child, expand=True, fill=True, padding=0)
        vbox.pack_start(sw, True, True, 0)
 
        # create a TreeView object which will work with our model (ListStore)
        hosts = self.create_model()
        treeView = gtk.TreeView(hosts)
        treeView.set_rules_hint(True)
 
        # add the TreeView to the scrolled window
        sw.add(treeView)
 
        # create the columns
        self.create_columns(treeView)
 	
        # add the vbox to the main window
        self.window.add(vbox)
 
        # show all
        self.window.show_all()
 
    
 
    def create_model(self):
	# inizializzo array      testdata = [(1, 'Mihai', 'Ion')]
	hostslist=dict()
	# Leggo file hosts
	nomefile="hosts"
	if not os.path.exists(nomefile):
		print "Attenzione: non esiste file ", nomefile	
		sys.exit(1)
	hostslist=[]
	in_file = open(nomefile,"r")
	for line in in_file:
		line3 = line.replace('\n', '')
	    	line2 = line3.split("\t")
		ip=line2[0]
		hostname=line2[1]
		stato = "unknow"
		stato = pinger(ip)
		hostslist.append([ip,hostname, stato])
	in_file.close()
	
        '''create the model - a ListHosts'''
        #hostslist = [(1, 'Mihai', 'Ion'), (2, 'John', 'Doe'), (3, 'Silvester', 'Rambo')]
        host = gtk.ListStore(str, str, str)
        for item in hostslist:
            host.append([item[0], item[1], item[2]])

	#print hostslist[2][2]
        return host
 
    

    def create_columns(self, treeView):
        ''' create the columns '''
        # CellRendererText = an object that renders text into a gtk.TreeView cell
        rendererText = gtk.CellRendererText()
        # column = a visible column in a gtk.TreeView widget
        # param: title, cell_renderer, zero or more attribute=column pairs
        # text = 0 -> attribute values for the cell renderer from column 0 in the treemodel
        column = gtk.TreeViewColumn("IP", rendererText, text=0)
        # the logical column ID of the model to sort
        column.set_sort_column_id(0)
        # append the column
        treeView.append_column(column)
 
        rendererText = gtk.CellRendererText()
        column = gtk.TreeViewColumn("hostname", rendererText, text=1)
        column.set_sort_column_id(1)    
        treeView.append_column(column)
 
        rendererText = gtk.CellRendererText()
        column = gtk.TreeViewColumn("Status", rendererText, text=2)
        column.set_sort_column_id(2)    
        treeView.append_column(column)
 
	
 
    def destroy(self, widget, data=None):
        '''close the window and quit'''
        gtk.main_quit()
        return False
 
    def main(self):
        '''All PyGTK applications must have a gtk.main(). Control ends here
        and waits for an event to occur (like a key press or mouse event).'''
        gtk.main()

 
 
if __name__ == "__main__":
    lvexample = BasicListViewExample()
    lvexample.main()
