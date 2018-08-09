FROM ubuntu:latest
FROM jjanzic/docker-python3-opencv

ENTRYPOINT ["cd" "../../../.."]

COPY code/python/ /home/code/python/
COPY videos/ /home/videos/

RUN chmod -R 755 /home
RUN cd /home/code/python
