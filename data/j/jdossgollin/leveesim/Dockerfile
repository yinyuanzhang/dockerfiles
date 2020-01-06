FROM  tensorflow/tensorflow:1.15.0-py3

COPY leveesim/requirements.txt /tmp/requirements.txt
RUN apt-get --yes install git libsm6 libxrender1 libfontconfig1
RUN pip install -r /tmp/requirements.txt &&\
    pip install https://github.com/hill-a/stable-baselines/archive/e315ebecbfd26225522a2e63a6bbd440c1df7f01.zip
RUN pip install https://github.com/jdossgollin/leveesim/archive/19b0dad1a9bd391b1f8a9b79cc2dad7cce3a573b.zip