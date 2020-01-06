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
RUN conda install -y python=3.6.9 pandas scikit-learn matplotlib tqdm numpy scipy xlsxwriter keras=2.2.0 && \
pip install pillow flask-restful && \
conda clean -y --all && mkdir -m 777 /vifi_lsu

# Add VIFI astronomy python modules
COPY vifi_lsu_mod.py vificlientlib.py test_flask_rest_api.py start_flask_restapi.sh /vifi_lsu/
RUN chmod +x /vifi_lsu/start_flask_restapi.sh

# Run the vificlientlib to activate the vifi client REST APIs
ENTRYPOINT ["/vifi_lsu/start_flask_restapi.sh"]
CMD ["/bin/bash"]