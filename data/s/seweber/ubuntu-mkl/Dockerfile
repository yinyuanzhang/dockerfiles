FROM ubuntu:bionic
ENV DEBIAN_FRONTEND noninteractive
RUN apt-get update \
  && apt-get install --no-install-recommends -y curl ca-certificates gnupg2 \
  && curl -LO https://apt.repos.intel.com/intel-gpg-keys/GPG-PUB-KEY-INTEL-SW-PRODUCTS-2019.PUB \
  && apt-key add GPG-PUB-KEY-INTEL-SW-PRODUCTS-2019.PUB \
  && echo 'deb http://apt.repos.intel.com/mkl all main' > /etc/apt/sources.list.d/intel-mkl.list \
  && apt-get update \
  && apt-get install --no-install-recommends -y \
    build-essential cmake libboost-all-dev redis-server jq \
    python3 python3-dev python3-pip python3-pytest python3-numpy python3-setuptools python3-redis python3-tqdm cython3 \
    libopenmpi-dev libpetsc-complex-3.7-dev libslepc-complex-3.7-dev libparmetis-dev \
    intel-mkl-64bit-2019.1-053 libtbb-dev \
  && curl -s https://api.github.com/repos/pairinteraction/pairinteraction/releases \
   | jq ".[0].assets | map(select(.name | contains(\"ubuntu-bionic.deb\"))) | .[0].browser_download_url" \
   | xargs curl -LO \
  && apt install --no-install-recommends -y ./*.deb \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/* \
  && sed -i 's/bind .*/bind 127.0.0.1/g' /etc/redis/redis.conf
RUN echo 'plm_rsh_agent = false' >> /etc/openmpi/openmpi-mca-params.conf
ENV MKLROOT="/opt/intel/compilers_and_libraries_2019/linux/mkl/"
