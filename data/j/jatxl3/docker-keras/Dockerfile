# docker-keras - Keras in Docker for reproducible deep learning

FROM jatxl3/docker-keras:latest
COPY mnist_cnn.py /srv
RUN cd /srv && python mnist_cnn.py

WORKDIR /srv/
