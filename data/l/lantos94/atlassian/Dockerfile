FROM adoptopenjdk/openjdk8:alpine
LABEL Author="Lyndon Leong"

RUN apk add --no-cache sudo

RUN export uid=1000 gid=1000 && \
    mkdir -p /home/confluence && \
    echo "confluence:x:${uid}:${gid}:confluence,,,:/home/confluence:/bin/bash" >> /etc/passwd && \
    echo "confluence:x:${uid}:" >> /etc/group && \
    echo "confluence ALL=(ALL) NOPASSWD: ALL" > /etc/sudoers.d/confluence && \
    chmod 0440 /etc/sudoers.d/confluence && \
    chown ${uid}:${gid} -R /home/confluence


RUN apk add --no-cache ca-certificates wget curl openssh bash procps openssl perl

# font fix
RUN apk add msttcorefonts-installer ttf-dejavu tini fontconfig && \ 
    update-ms-fonts && \
    fc-cache -f
RUN ln -s /usr/lib/libfontconfig.so.1 /usr/lib/libfontconfig.so \
    && ln -s /lib/libuuid.so.1 /usr/lib/libuuid.so.1 
# && ln -s /lib/libc.musl-x86_64.so.1 /usr/lib/libc.musl-x86_64.so.1

ENV LANG=en_AU.UTF-8
ENV LANGUAGE=en_AU.UTF-8
ENV LD_LIBRARY_PATH /usr/lib


RUN mkdir -p /opt/atlassian
RUN mkdir -p /var/atlassian/application-data/confluence

# props not 777 maybe 766
RUN chmod 777 /opt/atlassian/
RUN chmod 777 /var/atlassian/application-data/confluence

USER confluence
WORKDIR /opt/atlassian

# swapped from ADD to RUN wget because of caching
RUN wget https://product-downloads.atlassian.com/software/confluence/downloads/atlassian-confluence-6.6.14.tar.gz
RUN mkdir confluence && tar -xf atlassian-confluence-6.6.14.tar.gz -C confluence --strip-components 1

ENV confluence_HOME=/var/atlassian/application-data/confluence
RUN echo "confluence.home=/var/atlassian/application-data/confluence" >> /opt/atlassian/confluence/confluence/WEB-INF/classes/confluence-init.properties


CMD /opt/atlassian/confluence/bin/start-confluence.sh -fg