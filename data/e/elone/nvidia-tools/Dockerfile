FROM nvidia/opencl:devel-ubuntu18.04

ENV DEBIAN_FRONTEND noninteractive

# install system tools
RUN apt-get update && apt-get install -y python python-pip aircrack-ng p7zip unzip

# install JohnTheRipper bleeding-jumbo dependencies
RUN apt-get install -y build-essential libssl-dev libgmp-dev libbz2-dev libpcap-dev zlib1g-dev libcompress-raw-lzma-perl

# install john
RUN wget -t0 https://www.catpasswd.cn/static/file/edcbeda1fe465395fdf3d2ea63ca61422637144f \
    && mv edcbeda1fe465395fdf3d2ea63ca61422637144f JohnTheRipper-edcbeda1fe465395fdf3d2ea63ca61422637144f.zip \
    && unzip -x JohnTheRipper-edcbeda1fe465395fdf3d2ea63ca61422637144f.zip \
    && mv JohnTheRipper-edcbeda1fe465395fdf3d2ea63ca61422637144f JohnTheRipper-bleeding-jumbo \
    && cd JohnTheRipper-bleeding-jumbo/src/ \
    && ./configure && make -s clean && make -sj4 \
    && cd ../../ \
    && mv JohnTheRipper-bleeding-jumbo/ /usr/local/ \
    && ln -s /usr/local/JohnTheRipper-bleeding-jumbo/run/john /usr/local/bin/john \
    && ln -s /usr/local/JohnTheRipper-bleeding-jumbo/run/rar2john /usr/local/bin/rar2john \
    && ln -s /usr/local/JohnTheRipper-bleeding-jumbo/run/zip2john /usr/local/bin/zip2john \
    && rm JohnTheRipper-edcbeda1fe465395fdf3d2ea63ca61422637144f.zip

# install hashcat 4.0.0
RUN wget -t0 https://hashcat.net/files/hashcat-4.0.1.7z \
    && 7zr x hashcat-4.0.1.7z \
    && mv hashcat-4.0.1/ /usr/local/ \
    && ln -s /usr/local/hashcat-4.0.1/hashcat64.bin /usr/local/bin/hashcat \
    && ln -s /usr/local/hashcat-4.0.1/hashcat64.bin /usr/local/bin/hashcat64 \
    && ln -s /usr/local/hashcat-4.0.1/hashcat64.bin /usr/local/bin/hashcat64.bin \
    && rm hashcat-4.0.1.7z

# install hashcat-utils v1.8
RUN wget -t0 https://github.com/hashcat/hashcat-utils/releases/download/v1.8/hashcat-utils-1.8.7z \
    && 7zr x hashcat-utils-1.8.7z \
    && mv hashcat-utils-1.8 /usr/local/ \
    && ln -s /usr/local/hashcat-utils-1.8/bin/cap2hccapx.bin /usr/local/bin/cap2hccapx \
    && rm hashcat-utils-1.8.7z

# install python libs
COPY ./requirements.txt /requirements.txt
RUN pip install --upgrade setuptools \
    && pip install -r requirements.txt \
    && rm requirements.txt \
    && pip install --upgrade pip
