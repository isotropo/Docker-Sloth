Before running the Docker image, move all videos to a directory called videos. This should be one directory deeper than the directory you're executing the command below from.

To run the image, execute

    docker run -it -v output:/data -v videos:videos py3.6-opencv-json-kitti /bin/bash

from the bash terminal. Next, run the frameGrab.py script.

    python frameGrab.py

You will need to specify the name, file-extension (.mp4, etc), and then the FPS (Frames Per Second) will be displayed. You are then prompted to specify the interval (the number of times a frame is captured per second). The program will then take this number and calculate an approximate frame capture interval by taking the modulus of the current frame and the FPS divided by the user-specified-interval.

*If you're interested in adding new keys to your Sloth config file, edit configWriter.py*

Next, execute

	Sloth --config /home/code/config.py

, and then add all the images you'd like to work with to the workspace. Make whatever bounding boxes you needed, and then if the object is occluded press o (and specify a value 0-3 for occlusion). To specify a truncation, you press t (and then specify a value of 0 or 1 or enter in y or n).

Once you've done this, execute

    python fileConverter.py

and that's it. You can exit and all your work will be saved to a folder called output.
