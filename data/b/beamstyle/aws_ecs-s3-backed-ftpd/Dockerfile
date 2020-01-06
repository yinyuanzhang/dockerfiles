FROM debian:buster

MAINTAINER Thomas Cheng <thomas@beamstyle.com.hk>

RUN set -eux;                               \
    apt-get update && apt-get install -y                  \
        curl                                \
        fuse                                \
        gcc                                 \
        git                                 \
        openssh-server                      \
        openssl                             \
        syslog-ng                           \
        musl-dev                            \
        ca-certificates


##### SSH #####

RUN mkdir -p /var/run/sshd

# Enabling password-based login for SSH server
RUN sed -ri 's/#PermitRootLogin.*$/PermitRootLogin yes/g' /etc/ssh/sshd_config
RUN sed -ri 's/UsePAM yes/#UsePAM yes/g' /etc/ssh/sshd_config

# Login fix (otherwise user is kicked off after login) for SSH server
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' -i /etc/pam.d/sshd

# Set user visibility
ENV NOTVISIBLE "in users profile"
RUN echo "export VISIBLE=now" >> /etc/profile

# Exposing the SSH port
EXPOSE 22

# Fixes SSH terminal display error (esp. when using VI) for users "root"
RUN echo "shopt -s checkwinsize"                >> ~/.bashrc 
RUN echo "set nocompatible"                     >> ~/.vimrc
RUN echo "set backspace=2"                      >> ~/.vimrc

##### Goofys #####


# Get goofys installed to /usr/local/bin/goofys, and set executable permissions
RUN set -eux;                                                                                                               \
    curl --fail -sSL -o /usr/local/bin/goofys https://github.com/kahing/goofys/releases/download/v0.21.0/goofys  \
    && chmod +x /usr/local/bin/goofys

# Create volume for goofys to use
RUN mkdir -p /mnt/s3
VOLUME /mnt/s3

# Fixes swap file issues with using VI on the mount directory
RUN echo "set directory=~/tmp,/var/tmp,/tmp"    >> ~/.vimrc



# add syslog-ng (syslog required by Goofys)
ADD rootfs/ /


ENV AWS_REGION ap-southeast-1
ENV AWS_BUCKET_AND_PREFIX my-bucket:optional-prefix
ENV AWS_ACCESS_KEY xxxxxxxxxx
ENV AWS_SECRET_KEY xxxxxxxxxx

ENV SSH_ROOT_PASSWORD=password
ENV SSH_STARTUP_DIRECTORY=/mnt/s3

ENV GOOFYS_MOUNT_DIR /mnt/s3
ENV GOOFYS_STAT_CACHE_TTL 1m0s
ENV GOOFYS_TYPE_CACHE_TTL 1m0s
ENV GOOFYS_DIR_MODE 0770
ENV GOOFYS_FILE_MODE 0770



# Execute script run.sh
ADD run.sh /usr/local/bin/
RUN ["chmod", "+x", "/usr/local/bin/run.sh"]
CMD ["/usr/local/bin/run.sh"]
