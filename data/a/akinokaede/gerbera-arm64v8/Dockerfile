FROM multiarch/ubuntu-core:arm64-bionic

RUN apt-get update && apt-get install software-properties-common -y
RUN add-apt-repository ppa:stephenczetty/gerbera-updates -y
RUN apt-get update && apt-get upgrade -y && apt-get install -y gerbera

ENTRYPOINT [ "/usr/bin/gerbera" ]
