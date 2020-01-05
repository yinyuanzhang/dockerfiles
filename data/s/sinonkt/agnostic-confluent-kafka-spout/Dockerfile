FROM jfloff/alpine-python:3.8

RUN apk add --update py-pip

ADD requirements.txt /root/requirements.txt
ADD acks.py /root/acks.py

# Install librdkafka
RUN git clone https://github.com/edenhill/librdkafka.git && \
  cd librdkafka && \
  git fetch origin aa63660a090ccf002b591d9a91d9a0f47449d043 && \
  ./configure --prefix=/usr && \
  make && make install && \
  cd ..

WORKDIR /root

RUN pip install -r requirements.txt && \
  chmod u+x /root/acks.py