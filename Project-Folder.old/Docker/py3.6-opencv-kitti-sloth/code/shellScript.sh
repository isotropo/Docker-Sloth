#!/bin/bash
# Change to root user
sudo su

# Install python3.6 on Ubuntu 16.04
add-apt-repository ppa:deadsnakes/ppa
apt-get update
apt-get install python3.6 -y

# Installation of openCV-python3.6
pip3.6 install numpy
cd ~/Software
OPENCV_VERSION="3.4.1"
wget https://github.com/opencv/opencv/archive/${OPENCV_VERSION}.zip 
unzip ${OPENCV_VERSION}.zip 
mkdir /opencv-${OPENCV_VERSION}/cmake_binary 
cd /opencv-${OPENCV_VERSION}/cmake_binary 

cmake -DBUILD_TIFF=ON \
-DBUILD_opencv_java=OFF \
  -DWITH_CUDA=OFF \
  -DENABLE_AVX=ON \
  -DWITH_OPENGL=ON \
  -DWITH_OPENCL=ON \
  -DWITH_IPP=ON \
  -DWITH_TBB=ON \
  -DWITH_EIGEN=ON \
  -DWITH_V4L=ON \
  -DBUILD_TESTS=OFF \
  -DBUILD_PERF_TESTS=OFF \
  -DCMAKE_BUILD_TYPE=RELEASE \
  -DCMAKE_INSTALL_PREFIX=$(python3.6 -c "import sys; print(sys.prefix)") \
  -DPYTHON_EXECUTABLE=$(which python3.6) \
  -DPYTHON_INCLUDE_DIR=$(python3.6 -c "from distutils.sysconfig import get_python_inc; print(get_python_inc())") \
  -DPYTHON_PACKAGES_PATH=$(python3.6 -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())") .. \

make install
rm /${OPENCV_VERSION}.zip
rm -r /opencv-${OPENCV_VERSION}


# Installation process for sip
apt-get update && apt-get install -y \
    apt-utils \
    mercurial \
    bison \
    flex \
    build-essential \
    cmake \
    git \
    wget \
    unzip \
    yasm \
    pkg-config \
    libswscale-dev \
    libtbb2 \
    libtbb-dev \
    libjpeg-dev \
    libpng-dev \
    libtiff-dev \
    libjasper-dev \
    libavformat-dev \
    libpq-dev
apt-get autoremove
cd ~/Software
chmod 777 ~/Software 
hg clone https://www.riverbankcomputing.com/hg/sip 
cd sip 
python3.6 build.py prepare 
python3.6 configure.py 
make && make install

# PyQt4 Installation
mkdir ~/Software
cd ~/Software
wget ttps://sourceforge.net/projects/pyqt/files/PyQt4/PyQt-4.12.1/PyQt4_gpl_x11-4.12.1.tar.gz/download
tar -xzf *.tar.gz
cd PyQt*
python3.6 configure-ng.py -yes
make
make install

# Sloth Installation
pip3.6 install okapi
export PYTHONPATH=$(which okapi)/python3.6/:$PYTHONPATH
cd /home/
pip3.6 install git+git://github.com/cvhciKIT/sloth