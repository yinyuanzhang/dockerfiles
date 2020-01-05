#-------------------------------------------------------------------------------
# docker image for CLAS12 Production Simulation - to be run in batch mode on OSG
#
# It is based on gemcbatch:2.7 image and includes:
#
# - JLAB_VERSION 2.3
# - clas12 tag 4.3.0
#
# - coatjava 5.7.41
# - clasdis, dvcd, disrad generator
# - ced version 1.006
#
#--------------------------------------------------------------------------
#
#  1. Remember to find/replace gemcinteractive version with the newest one
#  2. Remember to match clas12tags and JLAB_VERSION in environment.csh
#  3. Remember to find/replace COATJTAG with the newest one
#  4. If it's a new production version build both the number and the iprod
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
ENV CLAS12TAG 4.3.0
ENV COATJTAG 5.9.0
ENV CCDBSQLITE ccdb_2019-04-11.sqlite


# gfortran for clasdis generator



RUN yum install -y gcc-gfortran

WORKDIR $JLAB_ROOT

# Removing un-used tags and .git stuff
# Removing default version of gemc
# Replacing the scripts in /etc and with the environment scripts
# Checking out clas12Tags and compiling CLAS12TAG
# Putting clas12 gcard in $JLAB_ROOT/work
# Getting the field maps
# $JLAB_ROOT/work is an existing directory
RUN git clone https://github.com/gemc/clas12Tags.git \
	&& cd $JLAB_ROOT/clas12Tags \
	&& source $JLAB_ROOT/$JLAB_VERSION/ce/jlab.sh \
	&& rm -rf $JLAB_ROOT/$JLAB_VERSION/$OSRELEASE/gemc \
	&& ./goInstall $CLAS12TAG \
	# delete .git after goInstall as it does a pull
	&& rm -rf .git* `ls | grep -v goIns | grep -v $CLAS12TAG | grep -v env | grep -v REA` \
	&& cp $JLAB_ROOT/clas12Tags/$CLAS12TAG/clas12.gcard $JLAB_ROOT/work \
	&& mkdir -p /jlab/noarch/data \
	&& cd /jlab/noarch/data \
	&& wget -q http://clasweb.jlab.org/12gev/field_maps/TorusSymmetric.dat \
	&& wget -q http://clasweb.jlab.org/12gev/field_maps/clas12NewSolenoidFieldMap.dat \
	&& rm /etc/profile.d/jlab.csh \
	&& rm /etc/profile.d/jlab.sh \
	# reconstruction, clara and coatjava
	&& mkdir -p $JLAB_SOFTWARE/clas12/lib \
	&& mkdir -p $JLAB_SOFTWARE/clas12/bin \
	&& mkdir -p $JLAB_SOFTWARE/clas12/inc \
	&& cd $JLAB_SOFTWARE \
	# JAVA from Oracle
	# Get JRE tar.gz from https://www.oracle.com/technetwork/java/javase/downloads/index.html
	# The .tar.gz is then put at JLAB on /site
	&& wget --no-check-certificate https://www.jlab.org/12gev_phys/packages/sources/java/jre-8u191-linux-x64.tar.gz \
	&& tar -zxpvf jre-8u191-linux-x64.tar.gz \
	# reconstruction: coatjava
	&& cd $JLAB_SOFTWARE/clas12 \
	&& wget --no-check-certificate https://github.com/JeffersonLab/clas12-offline-software/releases/download/$COATJTAG/coatjava-$COATJTAG.tar.gz \
	&& tar -zxpvf coatjava-$COATJTAG.tar.gz \
	&& cd /jlab/work \
	# CCDBSQLITE
	&& wget --no-check-certificate https://www.jlab.org/12gev_phys/packages/ccdb/$CCDBSQLITE \
	# clasdis generator
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
	&& cd /jlab/work \
	# clasdvcs
	&& git clone https://github.com/JeffersonLab/dvcsgen.git \
	&& cd dvcsgen \
	&& make \
	&& cp dvcsgen $JLAB_SOFTWARE/clas12/bin \
	# Temp /condor for el6 binding
	&& mkdir /condor \
	&& mkdir /etc/condor

ADD environmentB.csh     /etc/profile.d
ADD environmentB.sh      /etc/profile.d

WORKDIR $JLAB_ROOT/work
