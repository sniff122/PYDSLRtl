#!/usr/bin/python3
import argparse
import sys
import time
from yaspin import yaspin
from yaspin.spinners import Spinners
import subprocess
import os
import datetime

parser = argparse.ArgumentParser(prog='Timelapse', description='Perform timelapses using GPhoto2 and a supported DSLR camera')

parser.add_argument('--no-photos', '-n', help='Number of Photos to be taken', dest='num_photos', type=int)
parser.add_argument('--delay', '-d', help='Delay between photos - Default delay is 1', dest='photo_delay', type=float, default=1)
parser.add_argument('-c', help="Don't prompt to continue after printing time going to take", action="store_true")
parser.add_argument('-l', help="Display GPhoto2 output", action="store_true")
parser.add_argument('--detect', help="Detect and list connected cameras", action="store_true")

if len(sys.argv)==1:
    parser.print_help(sys.stderr)
    sys.exit(1)

args = parser.parse_args()

detect = args.detect
if detect:
    os.system("gphoto2 --auto-detect")
    os._exit(0)

num_photos = args.num_photos
if num_photos is None:
    sys.stderr.write('ERROR: Please enter the number of photos\n')
    parser.print_help(sys.stderr)
photo_delay = args.photo_delay
cont = args.c
output = args.l



if cont:
    cont = "y"
else:
    cont = "n"

#print(num_photos)
#print(photo_delay)

os.system("gphoto2 --auto-detect")
print("NOTIFY - If you camera is not detected, control + c NOW and run 'gphoto2 --auto-detect, if not detected then, try reconnecting your DSLR!")

getPhotos = True
totalPhotos = num_photos
photodelay = photo_delay
totaltimesec = (totalPhotos * photodelay)
totaltimemin = int(round(((totalPhotos * photodelay) / 60), 0))
totaltimehor = int(round((((totalPhotos * photodelay) / 60) / 60), 0))
print("\nThis is going to take about {} seconds/{} minutes/{} hours!".format(totaltimesec, totaltimemin, totaltimehor))
if cont == "n":
    cont = input("Are you sure you want to continue (y/n)?: ")
    if cont != "y": 
        conti = True
        print("Exiting")
        os._exit(0)


currentPhotoCount = 0

try:
    with yaspin(Spinners.clock, text="Capturing", color="white") as spinner:
        while getPhotos:
            if (currentPhotoCount < totalPhotos):
                currentPhotoCount += 1
                if output:
                    os.system("gphoto2 --trigger-capture")
                else:
                    FNULL = open(os.devnull, 'w')
                    dispose = subprocess.call(["gphoto2", "--trigger-capture"], stdout=FNULL, stderr=subprocess.STDOUT)
                percentage = round(((currentPhotoCount / totalPhotos) * 100), 1)
                #print(percentage)
                message = "Current Photos: {} Remaining Photos: {} Total Photos: {} {}% Complete".format(currentPhotoCount,totalPhotos - currentPhotoCount , totalPhotos, percentage)
                spinner.text = "Capturing - {}".format(message)
                time.sleep(photodelay)
            else:
                spinner.text = "Capture Complete! - took {} photos".format(currentPhotoCount)
                spinner.ok("✅")
                getPhotos = False

	            #print("Done!")
	            #print("Time Lapse Finished")
	            #call(["gphoto2", "--get-all-files"])
	            #print("Photos Downloaded")
                #call(["gphoto2", "--delete-all-files"])
except KeyboardInterrupt:
        print("Exiting")
        os._exit(0)
