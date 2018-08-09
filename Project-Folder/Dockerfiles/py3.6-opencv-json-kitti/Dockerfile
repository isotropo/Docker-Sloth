# When building from this Dockerfile, move it to Project-Folder/
# These are the dependencies needed in this docker image.
FROM ubuntu:latest
FROM jjanzic/docker-python3-opencv


COPY code/python/ /home/code/python/
RUN chmod -R 755 /home

# This makes is so that the user will start in the directory where all the python code is located.
WORKDIR /home/code/python