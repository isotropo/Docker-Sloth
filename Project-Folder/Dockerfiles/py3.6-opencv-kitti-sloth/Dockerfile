FROM ubuntu:latest
FROM jjanzic/docker-python3-opencv

# Installation process for sip
RUN apt-get update && apt-get install -y \
    apt-utils \
    mercurial \
    bison \
    flex \
    vim
RUN cd /home && \
    chmod 700 /home && \
    hg clone https://www.riverbankcomputing.com/hg/sip && \
    cd sip && \
    python build.py prepare && \
    python configure.py && \
    make && make install

# Setup for use of gui from a docker container.
# For whatever reason this option doesn't work...
# RUN apt-get install -qqy x11-apps

# Installation process for PyQt4
COPY ./Software/Sloth/PyQt4/PyQt4_gpl_x11-4.12.1 /home/Software/
# RUN chmod -R 777 /home/Software
WORKDIR "/home/Software/PyQt4_gpl_x11-4.12.1"
# RUN python /home/Software/PyQt4_gpl_x11-4.12.1/configure-ng.py -yes && \
    # make && make install

# # Adds a dependency needed before sloth can be properly installed
RUN pip install okapi
RUN export PYTHONPATH=$(which okapi)/python/:$PYTHONPATH
RUN cd /home/

# # Installs sloth using Anaconda.
RUN pip install git+git://github.com/cvhciKIT/sloth

# # Get everything up to date
RUN apt-get update && apt-get install -y \
    vim

COPY code/python/frameGrab.py /home/code/python/frameGrab.py
COPY videos/ /home/videos/

RUN chmod -R 755 /home
RUN cd /home/code/python
