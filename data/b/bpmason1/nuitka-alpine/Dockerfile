FROM alpine:3.10.3

RUN apk --no-cache add \
      build-base \
      libuuid \
      g++ \
      chrpath \
      musl-dev \
      python3-dev \
      bash \
      vim 

RUN pip3 install --upgrade pip
RUN pip3 install nuitka==0.6.5

RUN cd $( dirname $(which nuitka3) ) && ln -s $PWD/nuitka3 nuitka

CMD bash
