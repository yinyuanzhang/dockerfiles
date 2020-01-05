FROM haskell
RUN apt-get update -qy
RUN apt-get install -qy vim
RUN stack upgrade
RUN stack setup
RUN stack update
COPY config.yaml /root/.stack/config.yaml
RUN stack new work
WORKDIR /work
RUN stack test
