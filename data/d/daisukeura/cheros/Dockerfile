FROM eclipse/stack-base:ubuntu

RUN sudo apt update
RUN sudo apt install python-pip -y
RUN apt install ros-robot ros-robot-dev -y
ENV LANG C.UTF-8

RUN sudo pip2 install --no-cache-dir numpy

RUN sudo apt remove python3* -y
RUN rm -rf /var/lib/apt/lists/*

USER user
WORKDIR /projects
CMD tail -f /dev/null
