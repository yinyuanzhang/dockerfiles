FROM debian
RUN echo "deb http://http.us.debian.org/debian/ testing non-free contrib main" >> /etc/apt/sources.list
RUN apt-get update && apt-get install -y \
    git \
    mercurial \
    gcc-8 \
    g++-8 \
    cmake \
    libgmp-dev
ENV CC="gcc-8" CXX="g++-8"
RUN ln -s /usr/bin/g++-8 /usr/bin/g++
RUN git config --global user.email "felix@fefrei.de" \
&&  git config --global user.name "Felix Freiberger"
RUN cd ~ \
&& git clone https://github.com/smtrat/carl \
&& cd ~/carl \
&& git checkout master
RUN cd ~/carl \
&& mkdir build && cd build && cmake ../ \
&& make
