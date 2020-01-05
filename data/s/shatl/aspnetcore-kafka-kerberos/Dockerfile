FROM microsoft/dotnet:2.1-aspnetcore-runtime AS base
LABEL maintainer="vk@alphacloud.net"
WORKDIR /

FROM microsoft/dotnet:2.1-sdk as build

# Download dependency for building  librdkafka
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys 3FA7E0328081BFF6A14DA29AA6A19B38D3D831EF \
    && echo "deb http://download.mono-project.com/repo/debian stretch main" | tee /etc/apt/sources.list.d/mono-official.list \
    && apt-get update && apt-get install -y mono-devel default-jre build-essential libssl-dev libsasl2-2 libsasl2-dev libsasl2-modules-gssapi-mit wget unzip

# Build librdkafka
ENV LIBRDKAFKA_VER=0.11.5
RUN curl -k -L -s https://github.com/edenhill/librdkafka/archive/v${LIBRDKAFKA_VER}.zip  -o ./librdkafka.zip

RUN ls -l && cd / && unzip librdkafka.zip && \
    cd librdkafka-${LIBRDKAFKA_VER} && \
    ./configure && \
    make && \
    make install


FROM base AS final

# Install runtime dependencies - kerberos clients etc
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get -y install krb5-user kstart \
      libsasl2-2 libsasl2-modules-gssapi-mit libsasl2-modules \
     && apt-get clean

COPY --from=build /usr/local/lib/librdkafka*.so* /usr/local/lib/
