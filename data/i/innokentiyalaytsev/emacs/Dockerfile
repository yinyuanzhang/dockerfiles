FROM ubuntu:18.04 AS ccls-build

ENV DEBIAN_FRONTEND noninteractive

RUN echo 'APT::Get::Assume-Yes "true";' >> /etc/apt/apt.conf

# Separate step for better caching
RUN apt-get update

# Eliminate warnings about package configuration being deferred
RUN apt-get install --no-install-recommends apt-utils

# ccls
RUN apt-get install --no-install-recommends \
        build-essential \
        cmake \
# Required for git to work with https
        ca-certificates \
        clang-7 \
        cmake \
        git \
        libclang-7-dev \
        llvm-7-dev \
        rapidjson-dev

RUN ln --symbolic `(which clang-7)` /usr/local/sbin/clang

RUN git clone \
        --branch 0.20190314 \
        --depth 1 \
        --shallow-submodules  \
        -- https://github.com/MaskRay/ccls.git /tmp/ccls && \
    mkdir /tmp/ccls-build && cd /tmp/ccls-build && \
    cmake /tmp/ccls \
        -DCMAKE_BUILD_TYPE=Release &&\
    make && \
    make install

# Cleanup
RUN apt-get remove \
        apt-utils \
        build-essential \
        libclang-7-dev \
        pinentry-curses \
        rapidjson-dev \
    && apt-get autoremove && apt-get autoclean \
    && rm -rf /tmp/* /var/lib/apt/lists/* /root/.cache/*

RUN ls `(clang -print-resource-dir)` -la

# ------------------------------------------------------------

FROM silex/emacs:26.2 AS emacs

LABEL maintainer="Innokentiy Alaytsev <alaitsev@gmail.com>"

# Set these arguments to actual identifiers when building image
# to run commands as host user.
# Instpiration: https://jtreminio.com/blog/running-docker-containers-as-current-host-user/
ARG USER_ID=1000
ARG GROUP_ID=1000

ENV DEBIAN_FRONTEND noninteractive

RUN echo 'APT::Get::Assume-Yes "true";' >> /etc/apt/apt.conf

# Separate step for better caching
RUN apt-get update

# Eliminate warnings about package configuration being deferred
RUN apt-get install --no-install-recommends apt-utils

RUN apt-get install --no-install-recommends \
        clang-format-7 \
        git \
        gnupg \
# pinentry-gtk2 is required for using gpg from emacs.
# pinentry-curses will not work properly.
        pinentry-gtk2 \
        ssh \
        sudo

# Support scripts for system setup and application running
COPY support_scripts/* /tmp/support_scripts/
RUN chown root /tmp/support_scripts/* && \
    chmod 700 /tmp/support_scripts/* && \
    mv /tmp/support_scripts/* /usr/local/sbin/ && \
# cleanup
    rm -rf /tmp/support_scripts

ENV UNAME="emacs" \
    GNAME="emacs" \
    UHOME="/home/emacs" \
    WORKSPACE="/home/emacs/.workspace" \
    SHELL="/bin/bash"

# Create user with known group and home folder
RUN groupadd --gid ${GROUP_ID} ${GNAME} && \
    useradd  \
        --uid ${USER_ID} \
        --gid ${GROUP_ID} ${UNAME} \
        --shell /bin/bash \
        --create-home && \
    usermod --append --groups sudo ${UNAME}

COPY home ${UHOME}

# Permissions
RUN chown --recursive ${USER_ID}:${GROUP_ID} ${UHOME}/

# Workspace directory will be used to store persistent state:
# .bash_history, Emacs desktop and workgroups. If this directory
# is not bound to some host directory, then the state will be lost.
RUN run_as_user mkdir ${WORKSPACE}
VOLUME ["${WORKSPACE}"]

# Update font cache for the user
RUN run_as_user fc-cache --force --verbose

# For GPG 2.x
RUN mkdir --parents /run/user/${USER_ID} && \
    chown --recursive ${USER_ID}:${GROUP_ID} /run/user/${USER_ID}/

# Cleanup
RUN apt-get remove \
        apt-utils \
    && apt-get autoremove && apt-get autoclean \
    && rm -rf /tmp/* /var/lib/apt/lists/* /root/.cache/*

# ccls and Clang resources. Should not be required, but I am not sure.
COPY --from=ccls-build /usr/local/bin/ccls /usr/local/bin/ccls
COPY --from=ccls-build /usr/lib/llvm-7/lib/clang/7.0.0 /usr/lib/llvm-7/lib/clang/7.0.0

ENTRYPOINT [ "entrypoint" ]
CMD ["emacs"]
