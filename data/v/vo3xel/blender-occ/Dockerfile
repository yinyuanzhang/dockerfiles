FROM debian:10.0

################MINICONDA####################################
ENV LANG=C.UTF-8 LC_ALL=C.UTF-8
ENV PATH /opt/conda/bin:$PATH

RUN apt-get update --fix-missing && \
    apt-get install -y wget bzip2 ca-certificates curl git && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* &&\

    wget --quiet https://repo.anaconda.com/miniconda/Miniconda2-4.7.10-Linux-x86_64.sh -O ~/miniconda.sh && \
    /bin/bash ~/miniconda.sh -b -p /opt/conda && \
    rm ~/miniconda.sh && \
    /opt/conda/bin/conda clean -tipsy && \
    ln -s /opt/conda/etc/profile.d/conda.sh /etc/profile.d/conda.sh && \
    echo ". /opt/conda/etc/profile.d/conda.sh" >> ~/.bashrc && \
    echo "conda activate base" >> ~/.bashrc

ENV TINI_VERSION v0.16.1
ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini /usr/bin/tini
RUN chmod +x /usr/bin/tini

################OCC####################################
RUN conda install python=3.6 &&\
    conda config --add channels conda-forge &&\
	conda config --add channels dlr-sc &&\
	conda config --add channels pythonocc &&\
	conda config --add channels oce &&\
	conda config --add channels tpaviot &&\
	conda config --add channels anaconda &&\
	conda config --add channels 3dhubs &&\
	conda config --add channels cadquery &&\
	conda info pythonocc-core==0.18 &&\
	conda list &&\
	conda update --all &&\
	conda install pythonocc-core==0.17.3 


################BPY####################################
RUN cat /etc/apt/sources.list &&\
	sed -i '/deb http:\/\/deb.debian.org\/debian buster main/ a\
		deb-src http:\/\/deb.debian.org\/debian buster main' /etc/apt/sources.list &&\
	sed -i '/deb http:\/\/security.debian.org\/debian-security buster\/updates main/ a\
		deb-src http:\/\/security.debian.org\/debian-security buster\/updates main' /etc/apt/sources.list &&\
	sed -i '/deb http:\/\/deb.debian.org\/debian buster-updates main buster\/updates main/ a\
		deb-src http:\/\/deb.debian.org\/debian buster-updates main' /etc/apt/sources.list &&\
	echo sed-ed-result: &&\
	cat /etc/apt/sources.list &&\

	apt-get update -y && apt-get upgrade -y &&\
    apt-get install cmake -y &&\
    apt-get install libboost1.67-dev -y &&\
    apt-get install libopencolorio-dev -y &&\
    apt-get install libopenimageio-dev -y &&\
    apt-get install llvm -y &&\
    apt-get install subversion build-essential gettext \
		libxi-dev libsndfile1-dev \
		libpng-dev libjpeg-dev libfftw3-dev \
		libopenexr-dev libopenjp2-7-dev \
		libopenal-dev libalut-dev libvorbis-dev \
		libglu1-mesa-dev libsdl1.2-dev libfreetype6-dev \
		libtiff-dev libavdevice-dev \
		libavformat-dev libavutil-dev libavcodec-dev libjack-dev \
		libswscale-dev libx264-dev libmp3lame-dev python3-dev \
		libspnav-dev libtheora-dev libjack-dev libglew1.6-dev -y &&\
	apt install git &&\
	apt-get build-dep blender -y
	
RUN mkdir /blend &&\
	cd blend && git clone http://git.blender.org/blender.git &&\
	apt-get install sudo -y &&\
	cd blender &&\
	git branch -a &&\
	git checkout blender2.7 &&\
	git submodule update --init --recursive &&\
	git submodule foreach git checkout master &&\
	git submodule foreach git pull --rebase origin master &&\
	make update &&\

	apt-get update -y && apt-get install git build-essential -y &&\
	./build_files/build_environment/install_deps.sh &&\
	
# This time works without linking
#	echo linking /usr/lib/python3.6/site-packages/requests to /opt/conda/lib/python3.6/site-packages/requests &&\
#		mkdir -p /usr/lib/python3.6/site-packages/requests &&\
#		ln -sf /opt/conda/lib/python3.6/site-packages/requests /usr/lib/python3.6/site-packages/requests &&\
  
	cd /blend &&\
		mkdir cmake-make &&\
		cd cmake-make &&\
		cmake ../blender \
			-DPYTHON_LIBRARY=/opt/conda/lib/python3.6 \
			-DPYTHON_INCLUDE_DIR=/opt/conda/include/python3.6m \
			-WITH_PYTHON_INSTALL=OFF \
			-WITH_PLAYER=OFF \
			-WITH_PYTHON_MODULE=ON \
			-DWITH_MEM_JEMALLOC=OFF \
			-DWITH_CODEC_SNDFILE=ON \
			-DPYTHON_VERSION=3.6 \
			-DWITH_OPENCOLORIO=ON \
			-DOPENCOLORIO_ROOT_DIR=/opt/lib/ocio \
			-DWITH_OPENIMAGEIO=ON \
			-DOPENIMAGEIO_ROOT_DIR=/opt/lib/oiio \
			-DWITH_CYCLES_OSL=ON \
			-DWITH_LLVM=ON \
			-DLLVM_VERSION=6.0 \
			-DOSL_ROOT_DIR=/opt/lib/osl \
			-DWITH_OPENSUBDIV=ON \
			-DOPENSUBDIV_ROOT_DIR=/opt/lib/osd \
			-DWITH_OPENVDB=ON \
			-DWITH_OPENVDB_BLOSC=ON \
			-DWITH_ALEMBIC=ON \
			-DALEMBIC_ROOT_DIR=/opt/lib/alembic \
			-DWITH_CODEC_FFMPEG=OFF \
			-DFFMPEG_LIBRARIES='avformat;avcodec;avutil;avdevice;swscale;swresample;lzma;rt;theora;theoradec;theoraenc;vorbis;vorbisenc;vorbisfile;ogg;x264;openjp2' &&\
			
			
		cat CMakeCache.txt &&\
		sed -i 's/WITH_PYTHON_MODULE:BOOL=OFF/WITH_PYTHON_MODULE:BOOL=ON/' CMakeCache.txt &&\
		sed -i 's/WITH_PYTHON_INSTALL:BOOL=ON/WITH_PYTHON_INSTALL:BOOL=OFF/' CMakeCache.txt &&\
		sed -i 's/WITH_PYTHON_INSTALL_NUMPY:BOOL=ON/WITH_PYTHON_INSTALL_NUMPY:BOOL=OFF/' CMakeCache.txt &&\
		sed -i 's/WITH_PYTHON_INSTALL_REQUESTS:BOOL=ON/WITH_PYTHON_INSTALL_REQUESTS:BOOL=OFF/' CMakeCache.txt &&\
		cat CMakeCache.txt &&\
		make install

ENV PYTHONPATH "${PYTHONPATH}:/blend/cmake-make/bin"

###############Installing last dependencies#############################
RUN pip install Flask &&\
	pip install Flask-RESTful &&\
	pip install pyopenssl &&\
	pip install flask-cors &&\
	pip install pillow &&\
	pip install sphinx &&\
	pip install sphinxcontrib-httpdomain