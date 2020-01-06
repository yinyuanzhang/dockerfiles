FROM sumglobal/rpi-openjdk:8-jdk-azul

#enable building ARM container on x86 machinery on the web (comment out next line if built on Raspberry)
RUN [ "cross-build-start" ]

#------------------
# for rpi/ARM
#------------------
ENV KAFKA_HEAP_OPTS -Xmx256M\ -Xms256M
#-----------------------------------------------------------------------------------------------------------------
# Zulu embedded doesn't support the G1 compiler and other options set by default - These are a bit more reasonable
#-----------------------------------------------------------------------------------------------------------------
ENV KAFKA_JVM_PERFORMANCE_OPTS -server\ -XX:+DisableExplicitGC\ -Djava.awt.headless=true

#copy files
COPY "./init.d/*" /etc/init.d/

#do installation
RUN apt-get update \
    && apt-get install -y vim bash openssh-server \
#do users
    && echo 'root:root' | chpasswd \
    && sed -i 's/PermitRootLogin without-password/PermitRootLogin yes/' /etc/ssh/sshd_config \
    && sed 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' -i /etc/pam.d/sshd \
    && mkdir /var/run/sshd \
#clean up
    && apt-get -yqq autoremove \
    && apt-get -y clean \
    && rm -rf /var/lib/apt/lists/*

#set the entrypoint
ENTRYPOINT ["/etc/init.d/entrypoint.sh"]

#SSH Port
EXPOSE 22

#set stop signal
STOPSIGNAL SIGTERM

#stop processing ARM emulation (comment out next line if built on Raspberry)
RUN [ "cross-build-end" ]
