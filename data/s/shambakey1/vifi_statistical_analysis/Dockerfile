FROM continuumio/miniconda3

# Install libgl for matlibplot module
#RUN apt-get update --fix-missing && \
#    apt-get install -y wget bzip2 ca-certificates \
#    libglib2.0-0 libxext6 libsm6 libxrender1 libxft-dev libfreetype6 libfreetype6-dev \
#    git vim
RUN apt-get update --fix-missing && \
    apt-get install -y libgl1-mesa-glx build-essential
	#mesa-libGL libXcomposite libXcursor libXi libXtst libXScrnSaver libXrandr alsa-lib mesa-libEGL

# Install required python modules
RUN conda install -y python pandas matplotlib numpy scipy scikit-learn && \
conda install -c conda-forge pyyaml scikit-sparse && \
conda clean -y --all

# Add VIFI astronomy python modules
COPY gl_stat.py ssdf_functions.py ./