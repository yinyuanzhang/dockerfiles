FROM tensorflow/tensorflow:1.8.0-py3

# Install python-tkinter, -hdf5, and xvfb
RUN apt-get update && \
      apt-get install -y \
      python3-tk \
      python3-h5py \
      xvfb \
      git

# Install Keras
RUN pip --no-cache-dir install \
      keras==2.1.6 \
      tables==3.4.3 \
      google-cloud-storage==1.13.0

COPY matplotlibrc /usr/local/lib/python3.5/dist-packages/matplotlib/mpl-data/matplotlibrc

COPY xvfb-run.sh /usr/bin/
RUN chmod +x /usr/bin/xvfb-run.sh

ENV DISPLAY host.docker.internal:0

