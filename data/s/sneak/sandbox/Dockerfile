FROM phusion/baseimage:0.11
CMD ["/sbin/my_init"]

ADD ./sources.list /etc/apt/sources.list

# setup
ADD ./run.sh /tmp/run.sh
RUN bash /tmp/run.sh && rm /tmp/run.sh

# enable ssh
RUN rm -f /etc/service/sshd/down

#cleanup
RUN apt-get clean && \
    rm -rf \
        /var/lib/apt/lists/* \
        /tmp/* \
        /var/tmp/* \
        /etc/ssh/ssh_host_*_key
