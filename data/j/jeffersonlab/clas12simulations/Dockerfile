#-------------------------------------------------------------------------------
# docker image for CLAS12 Production Simulation - to be run in batch mode on OSG
#-------------------------------------------------------------------------------
#
#  1. Remember to find/replace gemcbatch version with the newest one
#  2. Remember to match clas12tags and JLAB_VERSION in environment.csh
#  3. Remember to match CCDBSQLITE and CCDB_CONNECTION in environment.csh
#  4. Remember to find/replace COATJTAG with the newest one
#  5. If it's a new production version build both the number and the iprod
#
# To build manually. Remember to tag also a version and "latest"
#
#   docker build -f Dockerfile -t clas12simulations:production .
#   docker tag clas12simulations:production jeffersonlab/clas12simulations:production
#   docker push jeffersonlab/clas12simulations:production
#
#
#
#
#
#   No additional tags
#
#  Notice: maybe to do "docker login" before being able to push
#--------------------------------------------------------------------------
#
# To run in batch mode:
#
#   docker run -it --rm jeffersonlab/clas12simulations:production bash
#
# On a mac, if you allow access from localhost with:
#
#  1. Activate the option ‘Allow connections from network clients’ in XQuartz settings
#  2. defaults write org.macosforge.xquartz.X11 enable_iglx -bool true
#     (Restart XQuartz (to activate the setting)
#  3. xhost +127.0.0.1
#
# Then you can run docker and use the local X server with:
#
#  docker run -it --rm -e DISPLAY=docker.for.mac.localhost:0 jeffersonlab/clas12simulations:production bash
#--------------------------------------------------------------------------

FROM jeffersonlab/gemcbatch:2.7
LABEL maintainer "Maurizio Ungaro <ungaro@jlab.org>"

ENV JLAB_ROOT /jlab
ENV JLAB_VERSION 2.3
ENV CLAS12TAG 4.3.1
ENV COATJTAG 6b.3.2
ENV JAVATAG 11.0.5
ENV CCDBSQLITE ccdb_2019-08-04.sqlite
ENV JLAB_SOFTWARE /jlab/2.3/Linux_CentOS7.5.1804-x86_64-gcc4.8.5
ENV JAVADOWNLOAD jdk-$JAVATAG"_linux-x64_bin.tar.gz"

# gfortran for clasdis generator
# root for genKYandOnePion and evio2root


RUN yum install -y gcc-gfortran root

WORKDIR $JLAB_ROOT

# Checking out clas12Tags and compiling CLAS12TAG
# Removing un-used tags and .git stuff
RUN git clone https://github.com/gemc/clas12Tags.git \
	&& cd $JLAB_ROOT/clas12Tags \
	&& source $JLAB_ROOT/$JLAB_VERSION/ce/jlab.sh \
	&& rm -rf $JLAB_ROOT/$JLAB_VERSION/$OSRELEASE/gemc \
	&& ./goInstall $CLAS12TAG \
	# delete .git after goInstall as it does a pull
	&& rm -rf .git* `ls | grep -v goIns | grep -v $CLAS12TAG | grep -v env | grep -v REA | grep -v gcards`

# Getting the field maps
# Replacing the scripts in /etc and with the environment scripts
RUN mkdir -p /jlab/noarch/data \
	&& cd /jlab/noarch/data \
	&& wget -q http://clasweb.jlab.org/12gev/field_maps/TorusSymmetric.dat \
	&& wget -q http://clasweb.jlab.org/12gev/field_maps/clas12NewSolenoidFieldMap.dat \
	&& rm /etc/profile.d/jlab.csh \
	&& rm /etc/profile.d/jlab.sh

# java and coatjava
RUN   mkdir -p $JLAB_SOFTWARE/clas12/lib \
	&& mkdir -p $JLAB_SOFTWARE/clas12/bin \
	&& mkdir -p $JLAB_SOFTWARE/clas12/inc \
	&& cd $JLAB_SOFTWARE \
	# JAVA from Oracle
	# Get JRE tar.gz from https://www.oracle.com/technetwork/java/javase/downloads/index.html
	# The .tar.gz is then put at JLAB on /group/12gev_phys/www/packages/sources/java
	&& wget -q --no-check-certificate https://www.jlab.org/12gev_phys/packages/sources/java/$JAVADOWNLOAD \
	&& tar -zxpvf $JAVADOWNLOAD \
	# reconstruction: coatjava. untar file in coatjava directory
	&& cd $JLAB_SOFTWARE/clas12 \
	&& wget -q --no-check-certificate https://clasweb.jlab.org/clas12offline/distribution/coatjava/coatjava-$COATJTAG.tar.gz \
	&& mkdir -p coatjava ; tar -zxpvf coatjava-$COATJTAG.tar.gz  --strip-components 1 -C coatjava


# CCDBSQLITE
RUN cd /jlab/work \
	&& wget -q --no-check-certificate https://www.jlab.org/12gev_phys/packages/ccdb/$CCDBSQLITE

# Generators
	# clasdis generator
RUN cd /jlab/work \
	&& git clone https://github.com/JeffersonLab/clasdis-nocernlib \
	&& cd clasdis-nocernlib \
	&& make \
	&& cp clasdis $JLAB_SOFTWARE/clas12/bin \
	# inclusive dis with radiative correction
	&& cd /jlab/work \
	&& git clone https://github.com/JeffersonLab/inclusive-dis-rad.git \
	&& cd inclusive-dis-rad \
	&& make \
	&& cp generate-dis $JLAB_SOFTWARE/clas12/bin \
	# clasdvcs
	&& cd /jlab/work \
	&& git clone https://github.com/JeffersonLab/dvcsgen.git \
	&& cd dvcsgen \
	&& make \
	&& cp dvcsgen $JLAB_SOFTWARE/clas12/bin \
	# genKYandOnePion
	&& cd /jlab/work \
	&& git clone https://github.com/ValeriiKlimenko/genKYandOnePion \
	&& cd genKYandOnePion \
	&& chmod +x COMPILE_eg_ky \
	&& ./COMPILE_eg_ky \
	&& cp eg_ky $JLAB_SOFTWARE/clas12/bin 

# Temp /condor for el6 binding
RUN mkdir /condor \
	&& mkdir /etc/condor



ADD environment.csh     /etc/profile.d
ADD environment.sh      /etc/profile.d
WORKDIR $JLAB_ROOT/work
