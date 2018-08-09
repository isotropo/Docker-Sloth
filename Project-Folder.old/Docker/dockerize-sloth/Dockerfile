FROM ubuntu:latest
FROM python:3.6

# Installation process for sip
RUN sudo apt-get update && sudo apt-get install mercurial \
    bison \
    flex \
    vim \
    libqt-dev
RUN -qqy x11-apps
RUN cd /home && \
    chmod 700 /home && \
    hg clone https://www.riverbankcomputing.com/hg/sip && \
    cd sip && \
    python build.py prepare && \
    python configure.py && \
    make && make install

# Installation process for PyQt4
RUN cd /home && \
    wget https://sourceforge.net/projects/pyqt/files/PyQt4/PyQt-4.12.1/PyQt4_gpl_x11-4.12.1.tar.gz/download && \
    tar -xzf *.tar.gz && \
    cd PyQt* && \
    python configure-ng.py -yes && \
    make && make install

# Installation process for okapi and sloth
RUN pip install okapi
RUN export PYTHONPATH=$(which okapi)/python/:$PYTHONPATH
RUN cd /home/
RUN git clone github.com/cvhciKIT/sloth
RUN cd sloth
RUN python setup.py install -yes

# Replace 1000 with your user / group id
RUN export uid=0 gid=1000 && \
    mkdir -p /home/developer && \
    echo "developer:x:${uid}:${gid}:Developer,,,:/home/developer:/bin/bash" >> /etc/passwd && \
    echo "developer:x:${uid}:" >> /etc/group && \
    echo "developer ALL=(ALL) NOPASSWD: ALL" > /etc/sudoers.d/developer && \
    chmod 0440 /etc/sudoers.d/developer && \
    chown ${uid}:${gid} -R /home/developer