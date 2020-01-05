FROM simexp/octave:01_09_2015
MAINTAINER Pierre-Olivier Quirion <poq@criugm.qc.ca>


ENV NIAK_VERSION v0.13.4
ENV NIAK_RELEASE_NAME niak-with-dependencies

# Install NIAK from the tip of master
RUN apt-get install git -y --fix-missing


RUN cd /home \
   && git clone https://github.com/SIMEXP/niak.git \
   && cd niak \
   && git checkout cbrain_integration 

RUN cd /home/niak/extensions/ \
   && wget https://sites.google.com/site/bctnet/Home/functions/BCT.zip \
   && unzip BCT.zip \
   && rm BCT.zip

RUN cd /home/niak/extensions/ \
   && git clone https://github.com/SIMEXP/psom.git\
   && cd psom \
   && git checkout cbrain_integration 

RUN chmod 755 /home/niak/extensions/psom/psom_worker.py && ln -s /home/niak/extensions/psom/psom_worker.py /usr/bin/psom_worker.py


# Build octave configure file
RUN echo addpath\(genpath\(\"/home/niak/\"\)\)\; >> /etc/octave.conf

# Source minc tools
RUN echo "source /opt/minc-itk4/minc-toolkit-config.sh" >> /etc/profile \
    && echo "source /opt/minc-itk4/minc-toolkit-config.sh" >> /etc/bash.bashrc

# 3D visualisation tools
RUN apt-get install mricron -y \
     libcanberra-gtk-module

# Command to run octave as GUI
# docker run -i -t --privileged --rm -v /etc/group:/etc/group -v /etc/passwd:/etc/passwd   -v /tmp/.X11-unix:/tmp/.X11-unix -e DISPLAY=unix$DISPLAY -v $HOME:$HOME --user $UID poquirion/docker_build /bin/bash --login -c "cd $HOME/travail/simexp/software; octave --force-gui --persist --eval 'addpath(genpath(pwd))'; /bin/bash"
