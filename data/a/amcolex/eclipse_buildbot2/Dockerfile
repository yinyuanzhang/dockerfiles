#------------------------------------------------#
# * Copyright 2017 Flyability SA
# * Alex Pabouctsidis
# 
# * This docker file is used to create our eclipse buildbot image
#   which is used by bitbucket pipelines. The image is based on ubuntu, 
#   to which we add the GCC ARM toolchain & Eclipse + Plugins.
#
#   The eclipse download link is specific to the eclipse version and 
#   must be changed manually after each no release. The link may 
#   also break at any time.
#------------------------------------------------#

# Pull base image.
FROM ubuntu

# add GCC PAA
RUN apt-get update && apt-get install -y software-properties-common
RUN add-apt-repository -y ppa:team-gcc-arm-embedded/ppa 

# install required toolchains
RUN apt-get update && apt-get install -y \
  gcc-arm-embedded \
  build-essential \
  gcc-multilib \
  git \
  unzip \
  default-jre \ 
  sshpass && \
  mkdir /home/build/

  
# download eclipse
ADD http://ftp.snt.utwente.nl/pub/software/eclipse//technology/epp/downloads/release/photon/R/eclipse-cpp-photon-R-linux-gtk-x86_64.tar.gz /home

# extract and delete zip
RUN tar xvf /home/eclipse-cpp-photon-R-linux-gtk-x86_64.tar.gz -C /home
RUN rm /home/eclipse-cpp-photon-R-linux-gtk-x86_64.tar.gz

# download SonarQube scanner
ADD https://binaries.sonarsource.com/Distribution/sonar-scanner-cli/sonar-scanner-cli-3.2.0.1227-linux.zip /home
RUN unzip /home/sonar-scanner-cli-3.2.0.1227-linux.zip -d /home
RUN mv /home/sonar-scanner-3.2.0.1227-linux /home/sonar-scanner-cli
RUN rm /home/sonar-scanner-cli-3.2.0.1227-linux.zip

# download build wrapper
ADD https://sonarcloud.io/static/cpp/build-wrapper-linux-x86.zip /home
RUN unzip /home/build-wrapper-linux-x86.zip -d /home
RUN rm /home/build-wrapper-linux-x86.zip

# add to path variable
ENV PATH="/home/sonar-scanner-cli/bin:${PATH}"
ENV PATH="/home/build-wrapper-linux-x86:${PATH}"

# install eclipse GNU ARM Eclipse plugin
RUN /home/eclipse/eclipse -application org.eclipse.equinox.p2.director -noSplash \
-repository http://gnu-mcu-eclipse.netlify.com/v4-neon-updates \
-installIU  ilg.gnumcueclipse.managedbuild.cross.arm.feature.feature.group

# Define working directory.
WORKDIR /home

# Define default command.
CMD ["bash"]