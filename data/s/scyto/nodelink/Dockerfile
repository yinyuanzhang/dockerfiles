# nodelink v9 linux amd64 only - docker hub autobuild
FROM mono:slim

EXPOSE 8090
VOLUME NodeLink
COPY startnodelinkold.sh /startnodelinkold.sh

RUN apt-get update && apt-get install -y \
	wget \
    libmono-System.Net.Http \
    libmono-Microsoft.VisualBasic \
    && apt-get clean \
    && chmod +x startnodelinkold.sh 

# Define environment variable
ENV PATH /usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
ENV LANG C.UTF-8

# Run  when the container launches 
# ENTRYPOINT ["./startnodelink.sh"]
CMD ["/bin/bash", "/startnodelinkold.sh"]