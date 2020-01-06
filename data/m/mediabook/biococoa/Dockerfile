# Base Image, GNUstep dev environment
FROM mediabook/gnustep:latest

MAINTAINER Scott Christley <schristley@mac.com>

# PROXY: uncomment these if building behind UTSW proxy
#ENV http_proxy 'http://proxy.swmed.edu:3128/'
#ENV https_proxy 'https://proxy.swmed.edu:3128/'
#ENV HTTP_PROXY 'http://proxy.swmed.edu:3128/'
#ENV HTTPS_PROXY 'https://proxy.swmed.edu:3128/'

# Copy project source
COPY . /biococoa

RUN ["bash", "-c", "source /usr/local/share/GNUstep/Makefiles/GNUstep.sh && cd /biococoa && make install"]
