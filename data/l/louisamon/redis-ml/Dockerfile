# Compile redis-ml from sources
FROM ubuntu AS redis-ml-compiler
RUN apt-get update -y \
&& apt-get install -y \
  build-essential \
  libatlas-base-dev \
  wget
RUN wget -qO- https://github.com/RedisLabsModules/redis-ml/archive/master.tar.gz | tar xvz
WORKDIR redis-ml-master/src
RUN make

# Create a Redis 4 image pre-loaded with the compiled redis-ml module
FROM redis:4
COPY --from=redis-ml-compiler /redis-ml-master/src/redis-ml.so .
CMD [ "redis-server", "--loadmodule", "./redis-ml.so" ]
