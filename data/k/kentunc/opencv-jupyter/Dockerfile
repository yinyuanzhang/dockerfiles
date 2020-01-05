FROM python:3.6.5-stretch

RUN apt-get update && apt-get install -y --no-install-recommends \
    cmake \
    libgtk2.0-dev \
    pkg-config \
    libavcodec-dev \
    libavformat-dev \
    libswscale-dev \
  && pip install \
    numpy \
    jupyter

WORKDIR /usr/local/src

RUN git clone https://github.com/opencv/opencv.git

WORKDIR opencv/build

RUN cmake \
    -D CMAKE_BUILD_TYPE=RELEASE \
    -D CMAKE_INSTALL_PREFIX="$(python -c "import sys; print(sys.prefix)")" \
    -D PYTHON_EXECUTABLE="$(which python)" \
    -D PYTHON_INCLUDE_DIR="$(python -c "from distutils.sysconfig import get_python_inc; print(get_python_inc())")" \
    -D PYTHON_PACKAGES_PATH="$(python -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")" \
    .. \
  && make -j "$(nproc --all)" \
  && make install

WORKDIR /data

RUN apt-get purge -y cmake \
  && rm -rf /var/lib/apt/lists/* \
  && rm -rf /usr/local/src/*

CMD ["jupyter", "notebook", "--ip", "0.0.0.0", "--no-browser", "--allow-root", "--NotebookApp.token=''"]
