mkdir renamed

counter=1

ls -1tr *.JPG | while read filename; do cp $filename renamed/$(printf %05d $counter)_$filename; ((counter++)) && echo $filename; done

cd renamed

mkdir resized

parallel --progress gm mogrify -path resized -resize 3840x2160! *.JPG # If you want to keep the aspect ratio, remove the exclamation mark (!)

cd resized

ffmpeg -r 25 -pattern_type glob -i '*.JPG' -c:v copy output.avi # Change -r 25 to define the frame rate. 25 here means 25 fps.
