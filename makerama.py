#Script to read data and produce ramachandran plot
#Data needs to be two columns and ONLY floats
#x data in first column and coupled Y data in second
from Tkinter import *
import sys
import re

#the data file
data=str(sys.argv[1])
#the number of bins
bin=int(sys.argv[2])
#Graph title "Ramachandran plot of..."
title="Ramachandran plot of "+str(sys.argv[3])

if 360 % bin!=0:
	print 'Second argument needs to divide evenly into 360'
	sys.exit()

increments=360/bin

xbin=[]

for xincrep in range(1,bin+1):
	xbin=xbin+[int((xincrep*increments)-180)]

ybin=[]

for yincrep in range(1,bin+1):
	ybin=ybin+[int((yincrep*increments)-180)]	

thearrays=[]
pushx=-180
pushy=-180
linecount=0
for y in range(len(ybin)):
	pushx=-180
	for x in range(len(xbin)):
		count=0
		with open(data) as f:
			for line in f:
				linecount=linecount+1
				splitline=line.split()
				if (float(pushx) <= float(splitline[0])<float(xbin[x])) & (float(pushy) <=float(splitline[1])<float(ybin[y])):
					count=count+1
			thearrays=thearrays+['x'+str(x)+' '+'y'+str(y)+' '+str(count)]
			pushx=pushx+int(increments)
	pushy=pushy+int(increments)

histarray=[]
#thearray number * increment value -180 = degree position
for combo in thearrays:
	combosplit=combo.split()
	histarray=histarray+["x"+str((int(re.search(r'\d+', combosplit[0]).group())*increments)-180)+"y"+str((int(re.search(r'\d+', combosplit[1]).group())*increments)-180)+' '+combosplit[2]]

print histarray

file=open('arraybins.txt','w')
for editarray in histarray:
	file.write(editarray+"\n")
#control rama output (shitty colouring)
sys.exit()
reallinecount= linecount/(len(ybin)*len(xbin))

master = Tk()
w = Canvas(master, width=1070, height=920)
w.pack()
w.configure(background='black')
w.create_line(100, 100, 100, 820)
w.create_line(820, 820, 100, 820)

for entry in thearrays:
	splitentry=entry.split()
	thecolour=(float(splitentry[2])/float(reallinecount))
	colorpercent=255-(thecolour*255)
	mycolor= '#%02x%02x%02x' % (colorpercent, colorpercent, colorpercent)
	w.create_rectangle(((float(splitentry[0][1:])*(increments))*2+100), ((float(splitentry[1][1:])*(increments))*2+100), ((float(splitentry[0][1:])*(increments))*2+100+(2*increments)), ((float(splitentry[1][1:])*(increments))*2+100+(2*increments)),fill=mycolor, outline="")
w.create_line(100, 460, 820, 460, dash=(4, 4))
w.create_line(460, 100, 460, 820, dash=(4, 4))	
w.create_text(460, 850, fill="white", font="Times 20 italic bold", text="Phi")
w.create_text(50, 460, fill="white", font="Times 20 italic bold", text="Psi")
w.create_text(80, 820, fill="white", font="Times 12 bold", text="-180")
w.create_text(80, 460, fill="white", font="Times 12 bold", text="0")
w.create_text(80, 100, fill="white", font="Times 12 bold", text="180")
w.create_text(100, 830, fill="white", font="Times 12 bold", text="-180")
w.create_text(460, 830, fill="white", font="Times 12 bold", text="-0")
w.create_text(820, 830, fill="white", font="Times 12 bold", text="180")

w.create_rectangle(895, 160, 995, 760,fill='white', outline="")
w.create_rectangle(895, 160, 995, 220,fill='#%02x%02x%02x' % (25.5, 25.5, 25.5))
w.create_rectangle(895, 220, 995, 280,fill='#%02x%02x%02x' % (51, 51, 51))
w.create_rectangle(895, 280, 995, 340,fill='#%02x%02x%02x' % (76.5, 76.5, 76.5))
w.create_rectangle(895, 340, 995, 400,fill='#%02x%02x%02x' % (102, 102, 102))
w.create_rectangle(895, 400, 995, 460,fill='#%02x%02x%02x' % (127.5, 127.5, 127.5))
w.create_rectangle(895, 460, 995, 520,fill='#%02x%02x%02x' % (153, 153, 153))
w.create_rectangle(895, 520, 995, 580,fill='#%02x%02x%02x' % (178.5, 178.5, 178.5))
w.create_rectangle(895, 580, 995, 640,fill='#%02x%02x%02x' % (204, 204, 204))
w.create_rectangle(895, 640, 995, 700,fill='#%02x%02x%02x' % (229.5, 229.5, 229.5))
w.create_rectangle(895, 700, 995, 760,fill='#%02x%02x%02x' % (255, 255, 255))
								  
w.create_text(460, 60, fill="white", font="Times 35 bold", text=title)

mainloop()
