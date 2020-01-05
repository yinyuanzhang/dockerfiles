FROM jupyter/datascience-notebook

LABEL maintainer="till@meyerzuwestram.net"

USER root
RUN apt-get update && \
	DEBIAN_FRONTEND=noninteractive apt-get install -yq --no-install-recommends \
		netbase \
		haskell-stack \
		build-essential \
		libzmq3-dev \
		libncurses5-dev \
		pkg-config \
		zlib1g-dev

USER jovyan
RUN stack upgrade --binary-only # this upgrades the user's local stack
ENV PATH=$HOME/.local/bin:$PATH
RUN stack --install-ghc --resolver lts-12.7 install ihaskell
RUN ihaskell install --stack

CMD stack exec /usr/local/bin/start-notebook.sh

