FROM postgres:latest as base
RUN apt-get update \
&& apt-get install -y --no-install-recommends \
    make \
    postgresql-server-dev-10


FROM base as build
RUN apt-get install -y --no-install-recommends \
    build-essential \
    wget \
    git-core \
    ca-certificates \
    python
RUN mkdir -p /tmp/build \
&& cd /tmp/build \
&& wget https://github.com/plv8/plv8/archive/v2.1.0.tar.gz
RUN cd /tmp/build \
&& tar -xvzf v2.1.0.tar.gz
RUN cd /tmp/build/plv8-2.1.0 \
&& make static


FROM base as final
COPY --from=build /tmp/build/plv8-2.1.0/plv8.so /tmp/install/
COPY --from=build /tmp/build/plv8-2.1.0/plv8.control /tmp/install/
COPY --from=build /tmp/build/plv8-2.1.0/plv8--2.1.0.sql /tmp/install/
COPY Makefile /tmp/install/
RUN ls -la /tmp/install \
&& cd /tmp/install/ \
&& make install
RUN rm -rf /var/lib/apt/lists/*
