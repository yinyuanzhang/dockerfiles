FROM adoptopenjdk/openjdk8:alpine
LABEL Author="Lyndon Leong"

RUN apk add --no-cache sudo

RUN export uid=1000 gid=1000 && \
    mkdir -p /home/jira && \
    echo "jira:x:${uid}:${gid}:jira,,,:/home/jira:/bin/bash" >> /etc/passwd && \
    echo "jira:x:${uid}:" >> /etc/group && \
    echo "jira ALL=(ALL) NOPASSWD: ALL" > /etc/sudoers.d/jira && \
    chmod 0440 /etc/sudoers.d/jira && \
    chown ${uid}:${gid} -R /home/jira


RUN apk add --no-cache ca-certificates wget curl openssh bash procps openssl perl

# font fix
RUN apk add msttcorefonts-installer ttf-dejavu tini fontconfig && \ 
    update-ms-fonts && \
    fc-cache -f
RUN ln -s /usr/lib/libfontconfig.so.1 /usr/lib/libfontconfig.so \
    && ln -s /lib/libuuid.so.1 /usr/lib/libuuid.so.1 \
    && ln -s /lib/libc.musl-x86_64.so.1 /usr/lib/libc.musl-x86_64.so.1
ENV LANG=en_AU.UTF-8
ENV LANGUAGE=en_AU.UTF-8
ENV LD_LIBRARY_PATH /usr/lib


RUN mkdir -p /opt/atlassian
RUN mkdir -p /var/atlassian/application-data/jira

# props not 777 maybe 766
RUN chmod 777 /opt/atlassian/
RUN chmod 777 /var/atlassian/application-data/jira

USER jira
WORKDIR /opt/atlassian

# swapped from ADD to RUN wget because of caching
RUN wget https://product-downloads.atlassian.com/software/jira/downloads/atlassian-jira-software-8.2.0.tar.gz
RUN mkdir jira && tar -xf atlassian-jira-software-8.2.0.tar.gz -C jira --strip-components 1

ENV JIRA_HOME=/var/atlassian/application-data/jira

CMD /opt/atlassian/jira/bin/start-jira.sh -fg
