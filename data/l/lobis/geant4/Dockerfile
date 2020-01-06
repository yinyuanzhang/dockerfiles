FROM ubuntu:18.04
LABEL maintainer=luis.antonio.obis@gmail.com

ENV GEANT4_VERSION=v10.5.1

# INSTALL DEPENDANCES
RUN apt-get update -y && \
    apt-get install -y ca-certificates build-essential cmake git libexpat1-dev libx11-dev libxmu-dev libxerces-c-dev libqt4-dev && \
    apt-get autoremove -y && \
    apt-get clean -y && \
    rm -rf /var/cache/apt/archives/* && \
    rm -rf /var/lib/apt/lists/*

# CLONE SOURCE AND BUILD
ARG GEANT4_DIR=/home/geant4
ARG GEANT4_INSTALL_DIR=/opt/geant4/install/
RUN mkdir -p $GEANT4_DIR && \
    git clone https://github.com/Geant4/geant4.git --branch=${GEANT4_VERSION} $GEANT4_DIR/source && \    
    mkdir -p $GEANT4_DIR/build && \
    cd $GEANT4_DIR/build && \
    cmake ../source/ -DGEANT4_BUILD_MULTITHREADED=ON -DGEANT4_USE_QT=ON -DGEANT4_USE_OPENGL_X11=ON -DGEANT4_USE_RAYTRACER_X11=ON -DGEANT4_INSTALL_DATA=ON -DGEANT4_USE_GDML=ON -DCMAKE_INSTALL_PREFIX=$GEANT4_INSTALL_DIR && \
    make -j$((`nproc` + 1)) install && \
    rm -rf $GEANT4_DIR

# .bashrc
RUN echo "source $GEANT4_INSTALL_DIR/bin/geant4.sh" >> ~/.bashrc

CMD ["/bin/bash"]