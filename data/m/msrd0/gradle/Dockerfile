FROM gradle:jdk8

USER root
RUN apt-get -y update \
 && apt-get -y install --no-install-recommends sudo \
 && apt-get -y clean \
 && rm -rf /var/lib/apt/lists/* \
 && echo 'gradle ALL=(ALL) NOPASSWD: ALL' >/etc/sudoers.d/gradle

USER gradle
