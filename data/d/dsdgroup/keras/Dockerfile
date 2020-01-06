FROM dsdgroup/theano:cpu

MAINTAINER Guo Quan <guoquanscu@gmail.com>

ENV REFRESHED_AT 2016-09-29

# Install keras
RUN pip install keras

# Set up .keras for theano backend
RUN mkdir -p /root/.keras/ && touch /root/.keras/keras.json && \
    echo "{"                                    > /root/.keras/keras.json && \
    echo "    \"image_dim_ordering\": \"tf\","  >> /root/.keras/keras.json && \
    echo "    \"epsilon\": 1e-07,"              >> /root/.keras/keras.json && \
    echo "    \"floatx\": \"float64\","         >> /root/.keras/keras.json && \
    echo "    \"backend\": \"theano\""          >> /root/.keras/keras.json && \
    echo "}"                                    >> /root/.keras/keras.json
