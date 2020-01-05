FROM tensorflow/tensorflow:1.5.0-devel-gpu-py3
MAINTAINER haebinshin <sunsal0704@gmail.com>

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        ca-certificates locales tzdata curl python3-dev vim g++ openjdk-8-jdk && \
    apt-get clean

RUN pip3 --no-cache-dir install \
        tornado \
        numpy \
        pymysql \
        pandas \
        configargparse \
        gensim \
        JPype1-py3 \
        konlpy \
        jamotools

RUN wget https://raw.githubusercontent.com/HaebinShin/konlpy/master/scripts/mecab.sh && \
    /bin/bash mecab.sh && \
    rm mecab.sh

WORKDIR "/data"

RUN locale-gen en_US.UTF-8
ENV LC_ALL=en_US.UTF-8
ENV LANG=en_US.UTF-8
ENV LANGUAGE=en_US.UTF-8

RUN ln -sf /usr/share/zoneinfo/Asia/Seoul /etc/localtime

CMD ["/bin/bash", "-c", "jupyter notebook --notebook-dir=/data --no-browser --allow-root"]


