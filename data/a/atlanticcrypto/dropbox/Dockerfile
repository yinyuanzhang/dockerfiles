FROM shellbro/centos:8.0-0

ARG UID=1001
ARG GID=1001

RUN yum makecache && yum -y install python2 python3 && yum clean all

RUN groupadd -g $GID dropbox-user && useradd -u $UID -g $GID dropbox-user
USER dropbox-user
WORKDIR /home/dropbox-user

RUN mkdir bin Dropbox
RUN curl -L "https://www.dropbox.com/download?plat=lnx.x86_64" | tar xzf - \
    && >&2 echo "Dropbox ver.:" $(cat /home/dropbox-user/.dropbox-dist/VERSION)
RUN curl -L -o bin/dropbox \
    "https://www.dropbox.com/download?dl=packages/dropbox.py" \
    && chmod u+x bin/dropbox

EXPOSE 17500

ENTRYPOINT ["/home/dropbox-user/.dropbox-dist/dropboxd"]
