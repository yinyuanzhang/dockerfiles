FROM busybox

MAINTAINER dbye68@gmail.com

ENV LANG=C.UTF-8 LC_ALL=C.UTF-8

# RUN apk --no-cache add git tar bzip2 ca-certificates && update-ca-certificates

# RUN mkdir /spatial_data
# WORKDIR /spatial_data

# get sample Armidale spatial data

RUN wget --no-check-certificate -O armidale.tar.gz https://github.com/NSW-OEH-EMS-KST/grid-garage-sample-data/archive/GridGarage_SampleData_v1.0.2.tar.gz && \
    tar -xzf armidale.tar.gz && rm armidale.tar.gz

# get sample MCASS spatial data

RUN wget --no-check-certificate -O mcass.tar.gz https://github.com/byezy/mcassexample/archive/v1.0.tar.gz && \
    tar -xzf mcass.tar.gz && rm mcass.tar.gz
    
# get github code source

# BeakerX
RUN wget --no-check-certificate -O beakerx.tar.gz https://github.com/twosigma/beakerx/archive/1.4.1.tar.gz && \
    tar -xzf beakerx.tar.gz && rm beakerx.tar.gz

# gg

RUN wget --no-check-certificate -O ggub.tar.gz https://github.com/byezy/ggub/archive/v16-dev.tar.gz && \
    tar -xzf ggub.tar.gz && rm ggub.tar.gz

