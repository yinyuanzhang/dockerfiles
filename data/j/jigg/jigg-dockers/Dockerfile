# If you build a container using this file, please run the following command at a directory 'jigg-dockers/',
# ```
# docker build -t {image name}:{tag} -f docker/knp/Dockerfile .
# ```
FROM openjdk:8

WORKDIR /jigg

ENV LD_LIBRARY_PATH $LD_LIBRARY_PATH:/usr/local/bin:/usr/local/lib
ENV PATH $PATH:$HOME/usr/bin

RUN apt-get update && apt-get install -y less wget tar bzip2 unzip sudo make gcc g++ libz-dev

# install juman
RUN wget http://nlp.ist.i.kyoto-u.ac.jp/nl-resource/juman/juman-7.01.tar.bz2 \
    && tar -jxvf juman-7.01.tar.bz2 \
    && cd juman-7.01 \
    && ./configure && make && sudo make install \
    && cd ../

RUN wget http://nlp.ist.i.kyoto-u.ac.jp/nl-resource/knp/knp-4.19.tar.bz2 \
    && tar -jxvf knp-4.19.tar.bz2 \
    && cd knp-4.19 \
    && ./configure && make && sudo make install \
    && cd ../