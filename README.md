## Working With Docker-Sloth

Before running the Docker image, move all videos to `Project-Folder/videos`. This should be one directory deeper than the directory you're executing the command below from.

To run the image, execute

    docker run -it -v output:/data -v videos:videos mobutubuntu/py3.6-opencv-json-kitti:latest /bin/bash

in the directory `Project-Folder`. Within the docker container, run `frameGrab.py`.

    python frameGrab.py

You will need to specify the name, file-extension (.mp4, etc), and then the FPS (Frames Per Second) will be displayed. 

You are then prompted to specify the interval (the number of times a frame is captured per second). 

The program will then take this number and calculate an approximate frame capture interval by taking the modulus of the current frame and the FPS divided by the user-specified-interval.

*If you're interested in adding new keys to your Sloth config file, edit `configWriter.py`.*

Next, execute

	Sloth --config /home/code/config.py

, and then add all the images you'd like to work with to the workspace. Select the keys corresponding to the annotations you want to make and click and drag to make bounding boxes around your target object(s).

Once you've done this, execute

    python fileConverter.py

. And that's it. You can exit and all your work will be saved to a folder called output.

## Rebuilding Docker Containers

Copy the dockerfile you're interested in editing and rebuilding to `Project-Folder`.
