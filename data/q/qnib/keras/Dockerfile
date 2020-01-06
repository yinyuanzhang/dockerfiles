FROM tensorflow/tensorflow:latest-gpu


RUN apt-get update \
 && apt-get install -y git libyaml-dev \
 && git clone https://github.com/keras-team/keras.git /usr/local/keras \
 && cd /usr/local/keras \
 && python setup.py install
VOLUME ["/share"]
WORKDIR /usr/local/keras/examples
COPY examples/imdb_cnn.py \
     examples/mnist_cnn.py \
     /usr/local/keras/examples/
# $HOME will hold .cache and .keras
ENV HOME=/tmp/
