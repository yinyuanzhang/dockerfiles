FROM node:10

RUN npm -g config set user root \
  && npm install -g elm@^0.19 --no-progress
RUN git clone https://github.com/obmarg/libsysconfcpus.git;
RUN cd libsysconfcpus && ./configure && make && make install && cd ../
