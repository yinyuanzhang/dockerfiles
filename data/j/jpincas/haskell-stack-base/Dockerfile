FROM haskell

RUN apt-get update
RUN apt-get install -y entr

WORKDIR /home/docker/workspace

RUN stack update
RUN stack new hs-server

WORKDIR /home/docker/workspace/hs-server
RUN stack install scotty
RUN stack install aeson
RUN stack install hedis
RUN stack install uuid
RUN stack install http-conduit
RUN stack install warp
RUN stack install bytestring
RUN stack install either-unwrap
RUN stack install text
RUN stack install time
RUN stack install split
RUN stack install pwstore-fast
RUN stack install MissingH
RUN stack install http-types
RUN stack install containers
RUN stack install amqp
RUN stack install directory
RUN stack install process
RUN stack install mongoDB
RUN stack install bson
RUN stack install tasty
RUN stack install tasty-hunit

CMD ghc -v
