FROM atlassian/default-image:2
MAINTAINER Amente Bekele

# Install Tools from TrueStudio
RUN mkdir -p /opt/attolic_ts
COPY attolic_ts.tar.gz /opt/attolic_ts/
RUN tar --strip-components=1 -zxf /opt/attolic_ts/attolic_ts.tar.gz -C /opt/attolic_ts
RUN rm /opt/attolic_ts/attolic_ts.tar.gz
ENV PATH=$PATH:/opt/attolic_ts/ARMTools/bin:/opt/attolic_ts/Tools
ENV ATOLLIC_TOOLS_DIR=/opt/attolic_ts/Tools

# Install Generic Tools
RUN apt-get update && apt-get install -y --no-install-recommends wget zip unzip git make \
 srecord bc xz-utils gcc python curl python-pip python-dev build-essential \
 && python -m pip install --upgrade pip setuptools

# Install PlatformIO Core
RUN pip install --ignore-installed -U platformio

RUN pio platform install espressif8266 --with-package framework-arduinoespressif8266 \
 && pio platform install espressif32 \
 && cat /root/.platformio/platforms/espressif32/platform.py \
 && chmod 777 /root/.platformio/platforms/espressif32/platform.py \
 && sed -i 's/~2/>=1/g' /root/.platformio/platforms/espressif32/platform.py \
&& cat /root/.platformio/platforms/espressif32/platform.py

# Upgrade NodeJs
RUN npm install -g n \
 && n 10.15.2 \
 && rm `which node` \
 && rm `which npm` 
ENV PATH=$PATH:/usr/local/n/versions/node/10.15.3/bin/

# Install gulp globally
RUN npm install -g gulp

# Customer binary files merge tool with specified offset
COPY binary_merger.py /opt/binary_merger.py
