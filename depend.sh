echo "This shell script requires root permissions - if prompted, please enter your user password and make sure your user account can run sudo commands"

echo "Installing 'gphoto2' using apt"
sudo apt install gphoto2 -y
echo "Installed gphoto2"
echo "Installing parallel"
sudo apt install parallel -y
echo "Installed parallel"
echo "Installing graphicsmagick"
sudo apt install graphicsmagick -y
echo "Installed graphicsmagick"
echo "Installing yaspin using pip3"
sudo pip3 install yaspin
echo "Installed yaspin"

echo "Installed everything"
echo "To run the timelapse application, type ./timelapse.py plus the arguments"

echo "Printing help message"
./timelapse.py
