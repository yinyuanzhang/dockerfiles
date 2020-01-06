FROM postgres:11.1

RUN apt-get update -y && apt-get install -y curl git && apt-get install -y --reinstall make

# Add go to postgres
COPY go /usr/local
ENV PATH=$PATH:$HOME/go/bin:/usr/local/go/bin
ENV GOPATH=$HOME/go
RUN mkdir -p $GOPATH/bin
ENV GO15VENDOREXPERIMENT=1

EXPOSE 5432

CMD ["postgres"]