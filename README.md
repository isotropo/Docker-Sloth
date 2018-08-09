## Working With Docker-Sloth

Before running the Docker image, move all videos to `Project-Folder/videos`. This should be one directory deeper than the directory you're executing the command below from. To run the image, execute

    docker run -it -v output:/home/data -v videos:/home/videos mobutubuntu/py3.6-opencv-json-kitti:latest /bin/bash

in the directory `Project-Folder`. Within the docker container, run `frameGrab.py`.

    python frameGrab.py

You will need to specify the name, file-extension (.mp4, etc), and then the FPS (Frames Per Second) will be displayed. 

You are then prompted to specify the interval (the number of times a frame is captured per second). 

The program will then take this number and calculate an approximate frame capture interval by taking the modulus of the current frame and the FPS divided by the user-specified-interval.

*If you're interested in adding new keys to your Sloth config file, edit `configWriter.py`.*

** NOTE: py3.6-opencv-kitti-sloth is not currently dockerized. The user must either build Sloth from source or install via anaconda on their native filesystem **

Next, execute 

	Sloth --config python/config-files/config.py

, and then add all the images you'd like to work with to the workspace. Select the keys corresponding to the annotations you want to make and click and drag to make bounding boxes around your target object(s). Then save your annotations.

Once you've done this, execute

    python fileConverter.py

, specify your filename, and then your annotation file is generated as `output.json` in `Project-Folder/output/annotations`.

## Rebuilding Docker Containers

Copy the dockerfile you're interested in editing and rebuilding to `Project-Folder`.
