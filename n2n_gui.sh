#!/bin/sh
zenity --list --width=300 --height=300 \
      	--title="N2N hosts" \
      	--column="hostname" --column="IP" --column="Online" \
	luca-server 	10.1.3.1 "YES"  \
	luca-desktop	10.1.3.2 "."	\
	pj		10.1.3.3 "YES"	\
	peter		10.2.3.4 "."	
