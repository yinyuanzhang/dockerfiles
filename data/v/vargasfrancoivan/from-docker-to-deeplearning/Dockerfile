FROM python:3.7.3-slim-stretch

LABEL maintainer="Franco I. Vargas <vargasfrancoivan@gmail.com>" \
      name="from Docker to Deep Learning" \
      description="Container with almost everything that you may need." \
      version="Alpha 1.0"

ENV BUILD_PACKAGES="\
        build-essential \
        linux-headers-4.9 \
        python3-dev \
        cmake \
        tcl-dev \
        xz-utils \
        zlib1g-dev \
        git \
        curl" \
    APT_PACKAGES="\
        ca-certificates \
        openssl \
        graphviz \
        fonts-noto \
        libpng16-16 \
        libfreetype6 \
        libjpeg62-turbo \
        libgomp1" \
    PIP_PACKAGES="\
        pyyaml \
        mkl \
        cffi \
        h5py \
        requests \
        pillow \
        graphviz \
        numpy \
        pandas \
        scipy \
        scikit-learn \
        seaborn \
        matplotlib \
        jupyter \
        xgboost \
        tensorflow \
        keras \
        torch \
        torchvision \
        mxnet-mkl" \
    JUPYTER_CONFIG_DIR=/home/.ipython/profile_default/startup \
    LANG=C.UTF-8

RUN set -ex; \
    apt-get update -y; \
    apt-get upgrade -y; \
    apt-get install -y ${APT_PACKAGES}; \
    apt-get install -y ${BUILD_PACKAGES}; \
    pip install -U -v setuptools wheel; \
    pip install -U -v ${PIP_PACKAGES}; \
    apt-get remove --purge --auto-remove -y ${BUILD_PACKAGES}; \
    apt-get clean; \
    apt-get autoclean; \
    apt-get autoremove; \
    rm -rf /tmp/* /var/tmp/*; \
    rm -rf /var/lib/apt/lists/*; \
    rm -rf /var/cache/apt/archives/*.deb \
        /var/cache/apt/archives/partial/*.deb \
        /var/cache/apt/*.bin; \
    find /usr/lib/python3 -name __pycache__ | xargs rm -rf; \
    rm -rf /root/.[acpw]*; \
    pip install jupyter && jupyter nbextension enable --py widgetsnbextension; \
    mkdir -p ${JUPYTER_CONFIG_DIR}; \
    echo "import warnings" | tee ${JUPYTER_CONFIG_DIR}/config.py; \
    echo "warnings.filterwarnings('ignore')" | tee -a ${JUPYTER_CONFIG_DIR}/config.py; \
    echo "c.NotebookApp.token = u''" | tee -a ${JUPYTER_CONFIG_DIR}/config.py

WORKDIR /home/notebooks

EXPOSE 8888

CMD [ "jupyter", "notebook", "--port=8888", "--no-browser", \
"--allow-root", "--ip=0.0.0.0", "--NotebookApp.token=" ]
