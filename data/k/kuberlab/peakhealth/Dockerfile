FROM golang:1.11

ENV SRCPATH "$GOPATH/src/github.com/kuberlab/peakhealth"

RUN mkdir -p $SRCPATH
COPY ./pkg "$SRCPATH/pkg"
COPY ./peakhealth.go "$SRCPATH/peakhealth.go"
COPY ./Gopkg* "$SRCPATH/"
COPY ./build.sh "$SRCPATH/"

RUN curl https://raw.githubusercontent.com/golang/dep/master/install.sh | sh

RUN $SRCPATH/build.sh

COPY ./swagger-ui "$GOPATH/swagger-ui"
COPY ./firebase-login "$GOPATH/firebase-login"

CMD [ "peakhealth" ]

EXPOSE 8082
