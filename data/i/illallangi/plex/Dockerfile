FROM illallangi/ansible:latest
ENV PLEX_VERSION=1.11.3.4793-482972920
ENV PLEX_SHA256=9f9e6d7a34dfedc7d5c953f6de25eba362c9fa434213a2690caaebe04c9fd288
COPY image/* /etc/ansible.d/image/
RUN /usr/local/bin/ansible-runner.sh image

ENV UID=1024
ENV USER=plex
COPY container/* /etc/ansible.d/container/
CMD ["/usr/local/bin/plex-entrypoint.sh"]
