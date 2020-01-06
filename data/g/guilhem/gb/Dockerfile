FROM guilhem/gb:1.4

RUN mkdir -p /go/src/app
WORKDIR /go/src/app

ENV PATH /go/src/app/bin:$PATH

ONBUILD COPY . /go/src/app
ONBUILD RUN gb vendor restore
ONBUILD RUN gb build
