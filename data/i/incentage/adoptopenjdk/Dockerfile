#
# Prepare AdoptOpenJDK
#

FROM ubuntu:16.04

ARG JDKVER

ENV OPTDIR=/opt/app \
    ETCDIR=/etc/app \
    LOGDIR=/var/log/app \
    RUNDIR=/var/run/app \
    LC_ALL=C.UTF-8

# https://github.com/moby/moby/issues/38710
# Permissions on /etc/passwd for OpenShift dynamic runtime user ID
# Install AdoptOpenJDK and dependencies
RUN chmod g=u /etc/passwd \
 && mkdir -p ${OPTDIR} \
 && chmod g=u ${OPTDIR} \
 && mkdir -p ${ETCDIR} \
 && chmod g=u ${ETCDIR} \
 && mkdir -p ${LOGDIR} \
 && chmod g=u ${LOGDIR} \
 && mkdir -p ${RUNDIR} \
 && chmod g=u ${RUNDIR} \
 && apt update \
 && apt install -y \
        apt-transport-https \
        ca-certificates \
        fonts-dejavu-core \
        openssl \
        fontconfig \
        gzip \
        nmap \
        software-properties-common \
        tar \
        unzip \
        wget \
 && ln -s ncat /usr/bin/nc \
 && wget -qO - https://adoptopenjdk.jfrog.io/adoptopenjdk/api/gpg/key/public | apt-key add - \
 && add-apt-repository -y https://adoptopenjdk.jfrog.io/adoptopenjdk/deb/ \
 && apt update \
 && apt install -y \
        adoptopenjdk-11-hotspot=${JDKVER}* \
 && apt remove -y \
        apt-transport-https \
        software-properties-common \
 && apt autoremove -y \
 && apt clean \
 && rm -rf /var/lib/apt/lists/

# Set the JAVA_HOME to the now installed JDK
ENV JAVA_HOME /usr/lib/jvm/adoptopenjdk-11-hotspot-amd64

# entrypoint.sh allows OpenShift compatibility
COPY entrypoint.sh /

# Containers do not run as root
USER 1001:0

# CMD is not used. This allows us to pass args directly to entrypoint.sh
ENTRYPOINT [ "/entrypoint.sh" ]
