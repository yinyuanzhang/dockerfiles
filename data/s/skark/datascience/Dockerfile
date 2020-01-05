FROM ubuntu:latest as build

ENV CONDA_DIR=/condinst

RUN set -o xtrace \ 
	&& apt-get update \
	&& apt-get -y dist-upgrade \
	&& DEBIAN_FRONTEND=noninteractive apt-get install -y git wget keychain libsm6 libxext6 libxrender1 dvipng texlive-latex-extra texlive-fonts-recommended \
	&& apt-get clean \
	&& rm -rf /var/lib/apt/lists/* \
	&& wget -nv https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh \
	&& /bin/bash Miniconda3-latest-Linux-x86_64.sh -f -b -p $CONDA_DIR \
	&& rm Miniconda3-latest-Linux-x86_64.sh \
	&& $CONDA_DIR/bin/conda install -q -y  \
		notebook \
		numpy \
		pandas \
		scikit-learn \
		seaborn \
		sympy \
		bcolz \
		ipywidgets \
		tensorflow-mkl">=2.0.0" \	
	&& $CONDA_DIR/bin/conda install -q -y pytorch-cpu torchvision-cpu -c pytorch \
	&& $CONDA_DIR/bin/conda install -q -y feather-format opencv scipy matplotlib scikit-image spacy -c conda-forge \
	&& $CONDA_DIR/bin/conda update -y python \
	&& $CONDA_DIR/bin/conda clean -a -y \
	&& $CONDA_DIR/bin/pip install --no-cache-dir sklearn-pandas isoweek pandas_summary torchtext \
	&& find . -type f -name "*.py[co]" -delete \
	&& find . -type f -name "*.js.map" -delete \	
	&& find . -type d -name "__pycache__" -delete \
	&& date >/build-date.txt \
	&& set +o xtrace
	
#		opencv \	
#	&& $CONDA_DIR/bin/conda update --all -y  \	

COPY startup/*.py /root/.ipython/profile_default/startup/

#FROM scratch as final
#COPY --from=build / /

FROM build
COPY unittest.py /work/tx.py
RUN $CONDA_DIR/bin/python /work/tx.py

FROM build
WORKDIR /work
EXPOSE 8888
ENTRYPOINT ["/condinst/bin/jupyter", "notebook", "--ip=0.0.0.0", "--allow-root", "--no-browser", "--NotebookApp.token=''"]
