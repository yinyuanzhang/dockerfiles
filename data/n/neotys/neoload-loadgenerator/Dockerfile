#Be carefull openshift change the ID of the user on the fly. But this user is always in root group.

FROM neotys/alpine-glibc:3.10 as builder


ENV NL_VERSION=7.1
ADD https://www.neotys.com/redirect/redirect.php?product=neoload&target=direct-download&os=linux&version=${NL_VERSION} ./neoload_linux_x64.sh

ADD response.varfile ./

#The group has same right that the owner for openshift. This is by chmod because installer force the mod (umask is useless).
RUN sh /neoload_linux_x64.sh -q -c -dir /neoload -varfile response.varfile && \
    rm -rf /neoload/jre/*src.zip \
           /neoload/jre/lib/missioncontrol \
           /neoload/jre/lib/visualvm \
           /neoload/jre/lib/*javafx* \
           /neoload/jre/plugin \
           /neoload/jre/bin/javaws \
           /neoload/jre/bin/jjs \
           /neoload/jre/bin/orbd \
           /neoload/jre/bin/pack200 \
           /neoload/jre/bin/policytool \
           /neoload/jre/bin/rmid \
           /neoload/jre/bin/rmiregistry \
           /neoload/jre/bin/servertool \
           /neoload/jre/bin/tnameserv \
           /neoload/jre/bin/unpack200 \
           /neoload/jre/lib/javaws.jar \
           /neoload/jre/lib/deploy* \
           /neoload/jre/lib/desktop \
           /neoload/jre/lib/*javafx* \
           /neoload/jre/lib/*jfx* \
           /neoload/jre/lib/amd64/libdecora_sse.so \
           /neoload/jre/lib/amd64/libprism_*.so \
           /neoload/jre/lib/amd64/libfxplugins.so \
           /neoload/jre/lib/amd64/libglass.so \
           /neoload/jre/lib/amd64/libgstreamer-lite.so \
           /neoload/jre/lib/amd64/libjavafx*.so \
           /neoload/jre/lib/amd64/libjfx*.so \
           /neoload/jre/lib/ext/jfxrt.jar \
           /neoload/jre/lib/oblique-fonts \
           /neoload/jre/lib/plugin.jar \
           /tmp/* /var/cache/apk/* && \
    chmod -R g=u /neoload


ADD ./lglogs.xconfig ./logs.xconfig /neoload/conf/

RUN echo "-Dneotys.logs.noredirection=false" >> /neoload/bin/LoadGeneratorAgent.vmoptions && \
    sed -i "s|collected.lg.logs.size.max=.*|collected.lg.logs.size.max=-1|g" /neoload/conf/agent.properties

FROM neotys/alpine-glibc:3.10

LABEL neoload.product.kind=LoadGenerator \
      neoload.product.version=7.1.0 \
      neoload.product.build=20191120-35 \
      neoload.project.version=7.0

ENV LOG_ALSO_TO_CONSOLE=true

RUN set -ex && \
    addgroup -S neoload &&\
    adduser -S -G neoload neoload &&\
    chmod g+w /etc/passwd && \
    chgrp 0 /home/neoload && \
    chmod g=rwx /home/neoload

#Alpine put suid bit on home directory. So the right inherit from parent directory. We prefer to use the GID of process for new files.
#We need to accept that entrypoin.sh changes the /etc/passwd.

EXPOSE 7100

#The group is root for openshift.
COPY --chown=neoload:0 --from=builder /neoload /home/neoload/neoload

ADD ./entrypoint.sh /home/neoload/

USER neoload

ENTRYPOINT ["/bin/sh", "/home/neoload/entrypoint.sh"]
