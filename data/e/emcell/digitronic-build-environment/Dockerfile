FROM debian:stretch

RUN dpkg --add-architecture i386 && \
    apt-get update && \
    apt-get install -y make vim-common wget git bzip2 build-essential libstdc++5:i386 wine wine32 procps openjdk-8-jre zip && \
    mkdir -p /root/tmp && cd /root/tmp && \
    wget https://developer.arm.com/-/media/Files/downloads/gnu-rm/5_3-2016q1/gccarmnoneeabi532016q120160330linuxtar.bz2 && \
    tar -xjf gccarmnoneeabi532016q120160330linuxtar.bz2 && \
    mkdir -p /usr/local && \
    cp -R gcc-arm-none-eabi-5_3-2016q1/* /usr/local && \
    rm -rf gcc-arm-none-eabi-5_3-2016q1 && \
    rm -rf gccarmnoneeabi532016q120160330linuxtar.bz2 && \
    wine hh && \
    for timeCount in 0 1 2 3 4 5 6 7 8 9 10 ; do \
        if [ -r "$HOME/.wine/system.reg" ]; then break; \
        elif [ $timeCount -eq 10 ]; then fail; fi; \
        sleep 1; \
    done  && \
    sed -i -r 's/"PATH"=str\(2\):"(.*)"/"PATH"=str\(2\):"\1;C:\\\\MinGW\\\\bin"/' ~/.wine/system.reg && \
    wget http://download.emcellsoft.de/digitronic/mingw.tar.gz && \
    tar -xf mingw.tar.gz -C /opt/ && \
    ln -s /opt/mingw ~/.wine/drive_c/MinGW

WORKDIR /home/user
