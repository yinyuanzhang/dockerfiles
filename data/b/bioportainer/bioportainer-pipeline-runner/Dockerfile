FROM python:alpine

############### Environment config
ENV SHELL=/bin/bash \
    HOME=/root \
    WORKDIR=$HOME/workdir/data \
    JAVA_VERSION_MAJOR=8 \
    JAVA_VERSION_MINOR=192 \
    JAVA_VERSION_BUILD=12 \
    JAVA_PACKAGE=jdk \
    HOTSWAP_AGENT_VERSION=1.2.0 \
    JAVA_JCE=unlimited \
    JAVA_HOME=/opt/jdk \
    PATH=${PATH}:/opt/jdk/bin \
    GLIBC_REPO=https://github.com/sgerrand/alpine-pkg-glibc \
    GLIBC_VERSION=2.28-r0 \
    LANG=C.UTF-8 \
    JUPYTER_TYPE=notebook \
    JUPYTER_PORT=8888 \
    NXF_DEBUG=0

ADD .config/start.sh /start.sh
ADD .config/start-notebook.sh /usr/local/bin/
ADD .config/wrapdocker /wrapdocker
ADD .tools/GUI /GUI
ADD .tools/Docker/docker-compose /usr/local/bin/
ADD .config/supervisord.conf /.config/
ADD .config/docker.conf /etc/supervisor/conf.d/docker.conf
ADD .config/gui.conf /etc/supervisor/conf.d/gui.conf
ADD .config/jupyter.conf /etc/supervisor/conf.d/jupyter.conf

RUN apk --update add --no-cache \
    build-base bash iptables ca-certificates e2fsprogs docker git libstdc++ curl \
    util-linux screen coreutils shadow \
    && rm -rf /var/cache/apk/* \
    && mkdir -p /.config/supervisord \
    && mkdir -p $HOME/workdir \
    && ln -s /root/.nextflow/assets $HOME/workdir/data \
    && chmod -R +x /GUI/conf/scripts/ \
    && chmod +x /wrapdocker && chmod +x /start.sh \
    && chmod +x /usr/local/bin/start-notebook.sh \
    && echo "$HOME/workdir/data" > /.work \
    && echo "$HOME/workdir/data" > /.workdir \
    && pip3 install -U pip \
    && apk update && apk add --no-cache -u supervisor \
    && pip3 install tornado typing jupyter bash_kernel nf-core \
    && python3 -m ipykernel install --user \
    && python3 -m bash_kernel.install --user \
    && apk del build-base && rm -rf /var/cache/apk/*
    

######################################################
# Install Java 8
######################################################

RUN set -ex \
    && [[ ${JAVA_VERSION_MAJOR} != 7 ]] || \
       ( echo >&2 'Oracle no longer publishes JAVA7 packages' && exit 1 ) \
    && for pkg in glibc-${GLIBC_VERSION} glibc-bin-${GLIBC_VERSION} glibc-i18n-${GLIBC_VERSION}; \
        do curl -sSL ${GLIBC_REPO}/releases/download/${GLIBC_VERSION}/${pkg}.apk \
        -o /tmp/${pkg}.apk; done \
    && apk add --no-cache --allow-untrusted /tmp/*.apk && rm -v /tmp/*.apk \
    && ( /usr/glibc-compat/bin/localedef --force --inputfile POSIX --charmap UTF-8 C.UTF-8 || true ) \
    && echo "export LANG=C.UTF-8" > /etc/profile.d/locale.sh \
    && /usr/glibc-compat/sbin/ldconfig /lib /usr/glibc-compat/lib \
    && mkdir /tmp/dcevm \
    && curl -L -o /tmp/dcevm/DCEVM-light-8u112-installer.jar \
        "https://github.com/dcevm/dcevm/releases/download/light-jdk8u112%2B8/DCEVM-light-8u112-installer.jar" \
    && mkdir /opt \
    && curl -jksSLH "Cookie: oraclelicense=accept-securebackup-cookie" \
        -o /tmp/java.tar.gz \
        http://download.oracle.com/otn-pub/java/jdk/${JAVA_VERSION_MAJOR}u${JAVA_VERSION_MINOR}-b${JAVA_VERSION_BUILD}/750e1c8617c5452694857ad95c3ee230/${JAVA_PACKAGE}-${JAVA_VERSION_MAJOR}u${JAVA_VERSION_MINOR}-linux-x64.tar.gz \
    && JAVA_PACKAGE_SHA256=$(curl -sSL https://www.oracle.com/webfolder/s/digest/${JAVA_VERSION_MAJOR}u${JAVA_VERSION_MINOR}checksum.html \
        | grep -E "${JAVA_PACKAGE}-${JAVA_VERSION_MAJOR}u${JAVA_VERSION_MINOR}-linux-x64\.tar\.gz" | \
        grep -Eo '(sha256: )[^<]+' | cut -d: -f2 | xargs) \
    && echo "${JAVA_PACKAGE_SHA256}  /tmp/java.tar.gz" > /tmp/java.tar.gz.sha256 \
    && sha256sum -c /tmp/java.tar.gz.sha256 && gunzip /tmp/java.tar.gz \
    && tar -C /opt -xf /tmp/java.tar \
    && ln -s /opt/jdk1.${JAVA_VERSION_MAJOR}.0_${JAVA_VERSION_MINOR} /opt/jdk \
    && cd /tmp/dcevm && unzip DCEVM-light-8u112-installer.jar \
    && mkdir -p /opt/jdk/jre/lib/amd64/dcevm \
    && cp linux_amd64_compiler2/product/libjvm.so /opt/jdk/jre/lib/amd64/dcevm/libjvm.so \
    && mkdir -p /opt/hotswap-agent/ \
    && curl -L -o /opt/hotswap-agent/hotswap-agent-${HOTSWAP_AGENT_VERSION}.jar \
        "https://github.com/HotswapProjects/HotswapAgent/releases/download/RELEASE-${HOTSWAP_AGENT_VERSION}/hotswap-agent-${HOTSWAP_AGENT_VERSION}.jar" \
    && ln -s /opt/hotswap-agent/hotswap-agent-${HOTSWAP_AGENT_VERSION}.jar \
        /opt/hotswap-agent/hotswap-agent.jar \
    && if [ "${JAVA_JCE}" == "unlimited" ]; then echo "Installing Unlimited JCE policy" \
    &&  curl -jksSLH "Cookie: oraclelicense=accept-securebackup-cookie" -o /tmp/jce_policy-${JAVA_VERSION_MAJOR}.zip \
        http://download.oracle.com/otn-pub/java/jce/${JAVA_VERSION_MAJOR}/jce_policy-${JAVA_VERSION_MAJOR}.zip \
    && cd /tmp && unzip /tmp/jce_policy-${JAVA_VERSION_MAJOR}.zip \
    && cp -v /tmp/UnlimitedJCEPolicyJDK8/*.jar /opt/jdk/jre/lib/security/; \
    fi \
    && sed -i s/#networkaddress.cache.ttl=-1/networkaddress.cache.ttl=10/ \
        $JAVA_HOME/jre/lib/security/java.security \
    && apk del glibc-i18n \
    && rm -rf /opt/jdk/*src.zip \
           /opt/jdk/lib/missioncontrol \
           /opt/jdk/lib/visualvm \
           /opt/jdk/lib/*javafx* \
           /opt/jdk/jre/plugin \
           /opt/jdk/jre/bin/javaws \
           /opt/jdk/jre/bin/jjs \
           /opt/jdk/jre/bin/orbd \
           /opt/jdk/jre/bin/pack200 \
           /opt/jdk/jre/bin/policytool \
           /opt/jdk/jre/bin/rmid \
           /opt/jdk/jre/bin/rmiregistry \
           /opt/jdk/jre/bin/servertool \
           /opt/jdk/jre/bin/tnameserv \
           /opt/jdk/jre/bin/unpack200 \
           /opt/jdk/jre/lib/javaws.jar \
           /opt/jdk/jre/lib/deploy* \
           /opt/jdk/jre/lib/desktop \
           /opt/jdk/jre/lib/*javafx* \
           /opt/jdk/jre/lib/*jfx* \
           /opt/jdk/jre/lib/amd64/libdecora_sse.so \
           /opt/jdk/jre/lib/amd64/libprism_*.so \
           /opt/jdk/jre/lib/amd64/libfxplugins.so \
           /opt/jdk/jre/lib/amd64/libglass.so \
           /opt/jdk/jre/lib/amd64/libgstreamer-lite.so \
           /opt/jdk/jre/lib/amd64/libjavafx*.so \
           /opt/jdk/jre/lib/amd64/libjfx*.so \
           /opt/jdk/jre/lib/ext/jfxrt.jar \
           /opt/jdk/jre/lib/ext/nashorn.jar \
           /opt/jdk/jre/lib/oblique-fonts \
           /opt/jdk/jre/lib/plugin.jar \
           /tmp/* /var/cache/apk/* \
  && echo 'hosts: files mdns4_minimal [NOTFOUND=return] dns mdns4' >> /etc/nsswitch.conf \
  && rm -rf /var/cache/apk/* \
  && curl -fsSL get.nextflow.io | bash && mv nextflow /usr/bin
    
WORKDIR $HOME/workdir/data

EXPOSE 7000
EXPOSE 8888
EXPOSE 5000
VOLUME ["$HOME/workdir/data", "/var/lib/docker"]
CMD ["/start.sh"]
