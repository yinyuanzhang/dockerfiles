FROM k0kubun/ruby:2.6.1
ENV RUBYOPT="--jit"

RUN apt-get update && apt-get install -y curl
RUN gem install acmesmith -v 2.1.0

RUN useradd k0kubun
USER k0kubun
