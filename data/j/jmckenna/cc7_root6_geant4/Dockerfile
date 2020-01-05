FROM rootproject/root-cc7
WORKDIR /

#Install dependencies
RUN yum install -y cmake g++ gcc libexpat1-dev \
libxerces-c-dev libx11-dev libgl1-mesa-dev xerces-c xerces-c-devel libXmu libXmu-devel lesstif-devel

#Build geant4
#RUN mkdir geant4
RUN git clone --depth 1 https://github.com/Geant4/geant4.git
#WORKDIR geant4

RUN mkdir build
WORKDIR build
RUN cmake3 -DCMAKE_C_COMPILER=gcc -DCMAKE_CXX_COMPILER=g++ -DCMAKE_BUILD_TYPE=RelWithDebInfo -DGEANT4_INSTALL_DATA=ON -DCLHEP_ROOT_DIR=$CLHEP_BASE_DIR -DCMAKE_COMPILER_IS_GNUCXX=ON -DGEANT4_USE_OPENGL_X11=ON -DGEANT4_USE_RAYTRACER_X11=ON -DGEANT4_USE_GDML=ON ../geant4 2>&1 | tee cmake.log
RUN make -j4
RUN make install

WORKDIR /
CMD /bin/bash
