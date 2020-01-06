FROM irvinec/ml-base

LABEL version="0.0.1"
LABEL imagename="gym-base"

WORKDIR /

# Make bash the default shell
SHELL ["/bin/bash", "-c"]

RUN conda update -y conda
RUN conda update -y pip

RUN apt-get -y update
RUN apt-get -y install python-opengl

# Fix mujuco error for gym
RUN mkdir /mujuco
WORKDIR /mujuco
RUN  git clone https://github.com/openai/mujoco-py.git .
RUN apt-get -y install libgl1-mesa-dev libgl1-mesa-glx libosmesa6-dev
RUN pip install -r requirements.txt
RUN python setup.py install
WORKDIR /
RUN rm -rf /mujuco

# Install gym and friends
RUN pip install gym[all]
RUN pip install gym-retro

# Turn on x11 forwarding
RUN echo 'Forward X11 yes' >> /etc/ssh/ssh_config

# Xming (or similar program) recommended on Windows hosts.
# Command to run docker container:
#   docker run -it --privileged -e DISPLAY=<host ip address>:0.0 -v /tmp/.X11-unix:/tmp/.X11-unix irvinec/gym-base
# NOTE: In <host ip address>:0.0  '0.0' is really the display id (given by Xming).
#   Would be more accurate to say '<host ip address>:<display id>'
# NOTE: The above command does not use '--rm' option which is typically included for deleting containers when they are stopped.



