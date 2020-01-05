# Jonas Becker's very own Docker container for testing purposes made for the
# project course "Geometriebasierte Entscheidungsunterstützung in der
# forensischen Chemometrie", winter semester 2019/20.

FROM phist91/texlive-full-minted:latest
LABEL maintainer="p.st@wwu.de"

# Installing JDK 11 and Maven
RUN apt-get update -y \
    && apt-get install -y curl openjdk-11-jdk maven git

# Installing Gitlab Runner
RUN curl -L https://packages.gitlab.com/install/repositories/runner/gitlab-runner/script.deb.sh | bash \
    && apt-get install -y gitlab-runner

# Installing SSH server
# ENV NOTVISIBLE "in users profile"
# RUN apt-get install -y openssh-server \
#    && mkdir /var/run/sshd \
#    && echo 'root:PASSWORD' | chpasswd \
#    && sed -i 's/PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config \
#    && sed 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' -i /etc/pam.d/sshd \
#    && echo "export VISIBLE=now" >> /etc/profile
# EXPOSE 22
# CMD ["/usr/sbin/sshd", "-D"]
