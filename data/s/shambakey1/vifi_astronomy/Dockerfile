FROM continuumio/miniconda3

# Install libgl for matlibplot module
#RUN apt-get update --fix-missing && \
#    apt-get install -y wget bzip2 ca-certificates \
#    libglib2.0-0 libxext6 libsm6 libxrender1 libxft-dev libfreetype6 libfreetype6-dev \
#    git vim
RUN apt-get update --fix-missing && \
    apt-get install -y libgl1-mesa-glx
	#mesa-libGL libXcomposite libXcursor libXi libXtst libXScrnSaver libXrandr alsa-lib mesa-libEGL

# Install required python modules
RUN conda install -y python scikit-learn keras matplotlib astropy && \
conda clean -y --all && mkdir -m 777 /vifi_ast

# Add VIFI astronomy python modules
COPY vifi_astr_mod.py vifi_ast/