FROM vguardiola/gentoo
RUN emerge -D dev-db/redis && eclean-dist -dqf && rm /usr/portage/distfiles -rf
COPY ./etc/security/limits.d/redis /etc/security/limits.d/redis
COPY ./etc/redis.conf /etc/redis.conf
RUN echo "vm.overcommit_memory = 1" >> /etc/sysctl.conf
EXPOSE 6379
CMD [ "redis-server", "/etc/redis.conf"]