FROM pytorch/pytorch:1.1.0-cuda10.0-cudnn7.5-runtime

RUN apt-get update && apt-get -y upgrade

RUN conda install -c anaconda libopencv opencv py-opencv

RUN pip install matplotlib pydensecrf Pillow torch torchvision flask 
RUN conda install -c conda-forge libiconv
RUN conda install -c conda-forge uwsgi
#RUN conda install -c cython
RUN pip install Cython --install-option="--no-cython-compile"
RUN conda install tensorflow-gpu

RUN cd /tmp \
    && git clone https://github.com/thtrieu/darkflow.git \
    && cd darkflow \
    && python3 setup.py build_ext --inplace \
    && pip install -e .

CMD /bin/bash
