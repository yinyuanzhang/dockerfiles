# seqtk container
FROM ubuntu:14.04
MAINTAINER osvaldo.zagordi@gmail.com

RUN apt-get update -y && apt-get install -y \
  seqtk \
  && rm -rf /var/lib/apt/lists/*

#ENTRYPOINT ["/usr/bin/seqtk"]
#CMD ["seq"]
