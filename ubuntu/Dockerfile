FROM ubuntu:16.04

#MAINTAINER Gary Bradski


# 기본 디렉토리
WORKDIR /app
ADD . /app

# First: get all the dependencies:
#
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential
RUN apt-get install -y cmake git libgtk2.0-dev pkg-config libavcodec-dev \
libavformat-dev libswscale-dev python-dev python-numpy libtbb2 libtbb-dev \
libjpeg-dev libpng-dev libtiff-dev libjasper-dev libdc1394-22-dev unzip

RUN apt-get install -y wget

# Just get a simple editor for convienience (you could just cancel this line)
RUN apt-get install -y vim


# Second: get and build OpenCV 3.2
#
RUN cd \
    && wget https://github.com/opencv/opencv/archive/3.2.0.zip \
    && unzip 3.2.0.zip \
    && cd opencv-3.2.0 \
    && mkdir build \
    && cd build \
    && cmake .. \
    && make -j8 \
    && make install \
    && cd \
    && rm 3.2.0.zip


# Third: install and build opencv_contrib
#
RUN cd \
    && wget https://github.com/opencv/opencv_contrib/archive/3.2.0.zip \
    && unzip 3.2.0.zip \
    && cd opencv-3.2.0/build \
    && cmake -DOPENCV_EXTRA_MODULES_PATH=../../opencv_contrib-3.2.0/modules/ .. \
    && make -j8 \
    && make install \
    && cd ../.. \
    && rm 3.2.0.zip


# Forth: get and build the Learning OpenCV 3 examples:
#    I copy the needed data to where the executables will be: opencv-3.2.0/build/bin
#
RUN cd \
    && git clone https://github.com/oreillymedia/Learning-OpenCV-3_examples.git \
    && cd Learning-OpenCV-3_examples \
    && mkdir build \
    && cd build \
    && cmake .. \
    && make -j8


# 호스트와 연결할 포트 ( 이렇게 빌드하는 이유는 추후 jwilder/nginx-proxy 를 위해서 입니다 )
EXPOSE 8080


# flask 설치
RUN pip install flask

ENTRYPOINT ["python"]

# 실행 명령어
CMD ["app.py"]