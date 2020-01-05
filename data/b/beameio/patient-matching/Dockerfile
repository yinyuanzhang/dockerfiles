# HELib base image
FROM debian:10

RUN apt-get update && \
    apt-get install -y build-essential wget cmake m4 libgmp-dev file unzip

RUN wget https://www.shoup.net/ntl/ntl-11.3.2.tar.gz && \
    tar xf ntl-11.3.2.tar.gz && \
    (cd ntl-11.3.2/src && \
    ./configure SHARED=on NTL_GMP_LIP=on NTL_THREADS=on NTL_THREAD_BOOST=on && \
    make -j4 && \
    make install)

RUN wget https://github.com/homenc/HElib/archive/7427ed3709bb9872835324dd0007a97b3ca3baca.zip && \
    unzip 7427ed3709bb9872835324dd0007a97b3ca3baca.zip && \
    (cd HElib-7427ed3709bb9872835324dd0007a97b3ca3baca && \
    mkdir build && \
    cd build && \
    cmake -DCMAKE_BUILD_TYPE=RelWithDebInfo -DBUILD_SHARED=ON -DENABLE_THREADS=ON .. && \
    make -j4 && \
    make install && \
    ldconfig)

COPY . /tmp/patient-matching/
WORKDIR /tmp/patient-matching

RUN make
RUN apt-get clean

# Patient-matching base image
FROM debian:10

COPY requirements.txt /opt

RUN apt-get update && \
    apt-get install -qy python3 && \
    apt-get install -qy python3-pip && \
    pip3 install -r /opt/requirements.txt

RUN rm -rf /opt/requirements.txt

COPY --from=0 /usr/local/lib/libhelib.so /usr/local/lib/libhelib.so
COPY --from=0 /usr/local/lib/libhelib.so.1.0.0 /usr/local/lib/libhelib.so.1.0.0
COPY --from=0 /usr/local/lib/libntl.a /usr/local/lib/libntl.a
COPY --from=0 /usr/local/lib/libntl.la /usr/local/lib/libntl.la
COPY --from=0 /usr/local/lib/libntl.so /usr/local/lib/libntl.so
COPY --from=0 /usr/local/lib/libntl.so.39 /usr/local/lib/libntl.so.39
COPY --from=0 /usr/local/lib/libntl.so.39.0.2 /usr/local/lib/libntl.so.39.0.2

RUN mkdir /var/lib/patient-matching
COPY --from=0 /tmp/patient-matching/GenerateKeys /var/lib/patient-matching
COPY --from=0 /tmp/patient-matching/Multiply /var/lib/patient-matching
COPY --from=0 /tmp/patient-matching/Encrypt /var/lib/patient-matching
COPY --from=0 /tmp/patient-matching/Decrypt /var/lib/patient-matching

COPY . /opt/patient-matching/
WORKDIR /opt/patient-matching/src

ENV LD_LIBRARY_PATH /usr/local/lib
ENV PYTHONPATH "${PYTHONPATH}:/opt/patient-matching"

RUN apt-get clean