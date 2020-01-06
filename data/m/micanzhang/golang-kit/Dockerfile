FROM micanzhang/golang-testing:latest

# build protoc
ADD build-protoc.sh build-protoc.sh
RUN /bin/sh build-protoc.sh && rm build-protoc.sh

# golang protobuf plugin
RUN go get -u github.com/golang/protobuf/protoc-gen-go

# install python3
RUN apt-get install -y python3 python3-pip && \
    pip3 install --upgrade pip setuptools && \
    if [[ ! -e /usr/bin/pip ]]; then ln -s pip3 /usr/bin/pip ; fi && \
    if [[ ! -e /usr/bin/python ]]; then ln -sf /usr/bin/python3 /usr/bin/python; fi && \
    rm -r /root/.cache
