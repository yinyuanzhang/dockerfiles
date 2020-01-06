FROM alpine:3.10.2

RUN apk add --no-cache git

# TODO: Can it be shallow clone?
RUN mkdir /pytorch
RUN git clone --recurse-submodules -j 10 https://github.com/pytorch/pytorch.git /pytorch

# Print out current revision
RUN git -C /pytorch rev-parse HEAD
