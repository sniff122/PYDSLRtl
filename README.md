
# PYDSLRtl

[YouTube tutorial comming soon]

A DSLR time-lapse application written in python to make time lapses using a DSLR (script provided to stitch frames together into an AVI file).

This works on any Linux based device whether its a raspberry pi or a full blown laptop or desktop running Linux. 

First, you need to clone this GitHub repository. To do this, you need to make sure you have 'git' installed (see below)

> sudo apt install git

 Now after installing git if it is not already installed, you can type 'git clone https://github.com/PYDSLRtl' and it should download all files into 'PYDSLRtl'

Second, you need to install the requires dependencies. To do so, you need to run the depend.sh file to install the required dependencies (gphoto2 from apt and yaspin from pip).

Third, you need to check if your camera is supported, connect your DSLR to your chosen Linux device (can be a normal computer or if you want to be portable, you can use a raspberry pi (any version is supported)). After connecting via USB and making sure your camera is turned on, type:

    ./timelapse.py --detect

 The script should display your camera model and how it is connected to your Linux device. If your camera is not detected, check that your camera is properly connected to your Linux device and is turned on, if you have checked both of these and it is still not detected, your camera may not be supported. Please check [here](http://gphoto.org/proj/libgphoto2/support.php) for a list of supported cameras. 
Here is the output when a camera is not detected:

    lewis@lewis-HP-Notebook:~/Desktop/PYDSLRtl$ ./timelapse.py --detect
    Model                          Port    
    ---------------------------------------------------------- 
                                          
Here is an example of the output when a camera is detected properly:

    lewis@lewis-HP-Notebook:~/Desktop/DSLR-timelapse$ ./timelapse.py --detect
    Model                          Port                                            
    ----------------------------------------------------------
    Nikon DSC D80 (PTP mode)       usb:003,012   

Now when you have verified that your camera is supported and detected, you can now give the script a test with:

    ./timelapse.py --no-photos 5 --delay 1 -c -l
If you have everything hooked up properly, you should hear/see your camera take 5 pictures with about a 1 second delay between them. If not, double check your USB connection and if your camera is turned on and set up correctly.

# Now its time to get it set up!

You now need to set up the camera on a tripod in your desired location pointing at your desired subject, remember to be creative! Some setup is dependent on the make/model of the camera but is mostly the same. So you can go the easy focus setup and go full auto-focus, the medium method, use auto-focus to focus at the start before shooting and switching to manual focus before starting the script or the hardest method, going full manual focus. Each focus setup does depend on your usage case but that is what experimentation is for. For camera settings, you can use whatever settings you wish and the script will not care. You could go full manual and tune each setting to your hearts desire, aperture priority so your camera will adjust the shutter speed with the light levels or shutter priority were the camera adjusts the aperture to the light levels but you can use whatever mode you wish, again a perfect opportunity to experiment with settings. Now after you have gotten your camera setup how you wish, you can now setup the Linux device with your camera, oh wait, you don't need to! All you need to do is to connect your camera over USB and provide now many images you want to take. 

# Stitching the images together
I have provided a bash script to process all of the JPEG images and turn them into a single uncompressed AVI file. To use this script, make a folder anywhere on your Linux device and copy all images you took for your time lapse into that new folder along with the 'stitch-images.sh' file (make sure stitch-images.sh is in the same folder as all of the JPEG images) and run it by typing

    ./stitch-images.sh
and the script will automatically rename all files so they are in the proper order for processing, then it will resize all the images to 1920*1080 and then use FFMPEG to take all of the renamed and resized images and convert them all into a single 25fps uncompressed AVI file. If you find that the uncompressed file is too much for your device, you can use a program like handbrake to compress the AVI into a smaller, compressed, MPEG4 encoded file. If you have any issues with the script, make an issue [here](https://github.com/sniff122/PYDSLRtl/issues/new).

# What would happen if?

The camera battery died?
	If you are quick enough, you can have a spare fully charged battery and do a quick swap of batteries or
	you could run the camera from an AC adaptor.
My SD card filled up?
	Your camera would stop taking images and do what it normally does when you fill up the SD card and stop
	taking images. To help prevent this, you could save the images as a JPEG file and not a RAW file what can 
	massively cut down on space usage, you will need to check your cameras manufacturer's manual if you 
	are not sure how to (you will need to as the script to make the images into a video file only works with 
	JPEG images)


