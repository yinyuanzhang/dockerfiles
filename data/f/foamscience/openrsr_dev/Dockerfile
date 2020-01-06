# Start from official Ubuntu 18.04 LTS release
FROM ubuntu:bionic

# Install build dependencies
RUN apt-get update \
  && apt-get install -y \
            git-core \
            build-essential binutils-dev \ 
            cmake \
            flex bison zlib1g-dev \
            libncurses5-dev libxt-dev \
            rpm graphviz python python-dev \
            gcc-5 g++-5 \
            vim; \
   rm -rf /var/lib/apt/lists/*

# Create a new user
RUN useradd --user-group --create-home --shell /bin/bash foam ;\
	echo "foam ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers

# Download required parts of Original foam-extend
RUN git clone https://github.com/FoamScience/OpenRSR.foam.git /opt/foam

WORKDIR /opt/foam/foam-extend-4.0

# Configure build
RUN bash -c "echo export WM_THIRD_PARTY_USE_BISON_27=1  >> etc/prefs.sh" \
  #echo export QT_SELECT=qt4  >> ~/foam/foam-extend-4.0/etc/prefs.sh \
  && echo "export WM_CC='gcc-5'"  >> etc/prefs.sh \
  && echo "export WM_CXX='g++-5'"  >> etc/prefs.sh
  #echo "export QT_BIN_DIR=/usr/bin/" >> ~/foam/foam-extend-4.0/etc/prefs.sh \
  #RUN bash -c "sed  's/# foamInstall=\/opt/foamInstall=\/opt/g' etc/bashrc" \

RUN bash -c "source etc/bashrc"
  # Fix Distro-specific errors with wmake and stuff \ 
RUN sed -i -e 's=rpmbuild --define=rpmbuild --define "_build_id_links none" --define=' ThirdParty/tools/makeThirdPartyFunctionsForRPM \
  && sed -i -e 's/gcc/\$(WM_CC)/' wmake/rules/linux64Gcc/c \
  && sed -i -e 's/g++/\$(WM_CXX)/' wmake/rules/linux64Gcc/c++

#RUN bash -c "yes | ./Allwmake.firstInstall"

USER foam

# Compile OpenRSR
#WORKDIR ~
#RUN git clone https://github.com/FoamScience/OpenRSR.git
#RUN cd OpenRSR
#RUN ./Allwmake
