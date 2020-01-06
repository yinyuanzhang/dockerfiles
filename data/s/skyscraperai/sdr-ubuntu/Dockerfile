FROM ubuntu:cosmic


ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update && \
  apt-get install -y software-properties-common && \
  add-apt-repository -y ppa:bladerf/bladerf && \
  add-apt-repository -y ppa:ettusresearch/uhd && \
  add-apt-repository -y ppa:pothosware/support && \
  add-apt-repository -y ppa:myriadrf/drivers && \
  add-apt-repository -y ppa:ettusresearch/uhd && \
  add-apt-repository -y ppa:pothosware/framework

RUN apt-get install -y \
  automake \
  bladerf \
  bladerf-fpga-hostedx40 \
  cmake \
  git \
  gnuradio \
  gr-iqbal \
  gr-osmosdr \
  libbladerf-dev \
  libbladerf-udev \
  libboost-all-dev \
  libssl-dev \
  osmo-sdr \
  pothos-all \
  python-numpy \
  python-soapysdr \
  python3-numpy \
  python3-soapysdr \
  rtl-sdr \
  soapysdr-module-bladerf \
  soapysdr-module-osmosdr \
  soapysdr-module-rtlsdr \
  soapysdr-tools \
  swig \
  uhd-host \
  uhd-soapysdr \
  soapysdr-module-uhd \
  && apt-get clean && rm -rf /var/lib/apt/lists/*

RUN rm -rf /tmp/* /var/tmp/*


WORKDIR /home
CMD ["bash"]
