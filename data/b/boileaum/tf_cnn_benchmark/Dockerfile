FROM tensorflow/tensorflow:latest-gpu

LABEL maintainer="Matthieu Boileau <matthieu.boileau@math.unistra.fr>"

RUN apt-get update && apt-get -yq dist-upgrade \
 && apt-get install -yq --no-install-recommends \
    git \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*

RUN git clone https://github.com/tensorflow/benchmarks.git

WORKDIR benchmarks/scripts/tf_cnn_benchmarks
