FROM ubuntu:18.04

WORKDIR /app/

#RUN git clone --depth=1 https://github.com/chrzyki/candc.git

######################## build gsoap ####################################

ADD candc-1.00.tbz2 /app/
ADD Makefile.unix /app/candc-1.00/Makefile.unix
ADD models.tar.bz2 /app/
ADD run_server.sh /app/candc-1.00/bin/run_server.sh
ADD candc.patch /app/candc-1.00/candc.patch

RUN apt update \
 && apt install -y build-essential git bison flex gsoap libgsoap-dev gcc-5 g++-5 g++-5-multilib gcc-5-multilib \
 && update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-5 50 \
 && update-alternatives --install /usr/bin/g++ g++ /usr/bin/g++-5 50 \
 && cd /app/candc-1.00 \
 && patch -p1 -i candc.patch \
 && make -f Makefile.unix -j `nproc` && make -f Makefile.unix soap \
 && apt purge -y build-essential git bison flex gcc-5 g++-5 g++-5-multilib gcc-5-multilib\
 && apt autoremove -y

EXPOSE 9004

ENTRYPOINT cd /app/candc-1.00/bin && ./run_server.sh