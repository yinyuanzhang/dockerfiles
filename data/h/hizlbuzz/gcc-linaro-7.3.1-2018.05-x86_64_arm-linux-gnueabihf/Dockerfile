FROM ubuntu:18.04

RUN apt update
RUN apt install -y xz-utils wget  build-essential

# get and extract linaro
RUN wget https://releases.linaro.org/components/toolchain/binaries/7.3-2018.05/arm-linux-gnueabihf/gcc-linaro-7.3.1-2018.05-x86_64_arm-linux-gnueabihf.tar.xz
RUN tar -xf gcc-linaro-7.3.1-2018.05-x86_64_arm-linux-gnueabihf.tar.xz 
RUN rm gcc-linaro-7.3.1-2018.05-x86_64_arm-linux-gnueabihf.tar.xz

# set path
ENV PATH="/gcc-linaro-7.3.1-2018.05-x86_64_arm-linux-gnueabihf/bin/:${PATH}"

# some project specific stuff
# eclipse used absolute paths (makfiles) --> setup link
RUN mkdir -p /root/capps
RUN mkdir -p /home/shell/ObcSoftware
RUN ln -s /root/capps/ /home/shell/ObcSoftware
