FROM alpine:edge

COPY /sbin/cleanup /usr/local/sbin/cleanup
COPY /bin/* /usr/local/bin/

# User
ENV UNAME="pekar"              \
    GNAME="peka"               \
    UHOME="/home/pekar"        \
    UID="1000"                 \
    GID="1000"                 \
    SHELL="/bin/bash"          \
    WORKSPACE="/mnt/workspace"

ENV DISPLAY=:0

ENV PORT=4200
EXPOSE $PORT

ENV GIT_UPSTREAM_URL="https://github.com/pekach/pekach.git"
ENV GIT_UPSTREAM_BRANCH="master"

# Update
RUN echo "http://nl.alpinelinux.org/alpine/edge/testing" \
    >> /etc/apk/repositories \
    && echo "http://nl.alpinelinux.org/alpine/edge/community" \
    >> /etc/apk/repositories \
    && apk --no-cache upgrade \
    && cleanup

# Install stuff
RUN apk --no-cache add \
    bash \
    coreutils \
    curl \
    dbus \
    firefox \
    git \
    hub \
    libsass \
    nodejs-current-npm \
    openssh \
    rsync \
    wget \
    xhost \
    xvfb \
    && npm -g config set user root \
    && apk --no-cache add --virtual build-deps \
    build-base \
    libsass-dev \
    python2-dev \
    && npm install -g @angular/cli \
    && apk del build-deps \
    && cleanup

# Add user
RUN echo "${UNAME}:x:${UID}:${GID}:${UNAME},,,:${UHOME}:${SHELL}" \
    >> /etc/passwd \
    && echo "${UNAME}::17032:0:99999:7:::" \
    >> /etc/shadow \
    && echo "${GNAME}:x:${GID}:${UNAME}" \
    >> /etc/group \
    && mkdir -p "${UHOME}" "${WORKSPACE}" /tmp/.X11-unix \
    && chmod 1777 /tmp/.X11-unix \
    && chown "${UID}":"${GID}" "${UHOME}" "${WORKSPACE}"

USER $UNAME

ENV HOME="${UHOME}"
WORKDIR "${WORKSPACE}"

ENTRYPOINT ["bash", "/usr/local/bin/run"]
