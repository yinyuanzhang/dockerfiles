FROM rundeck/rundeck:3.1.3

LABEL maintainer="zoredache@gmail.com"

USER 0
RUN  apt-get update \
  && apt-get install --yes curl apt-transport-https lsb-release gnupg \
  && curl -fsSL "https://download.docker.com/linux/debian/gpg" | apt-key add -qq - \
  && echo "deb [arch=amd64] https://download.docker.com/linux/debian stretch stable" \
     > /etc/apt/sources.list.d/download_docker_com_linux_debian.list  \
  && apt-get update \
  && apt-get install --yes docker-ce-cli \
  && addgroup --gid 999 docker \
  && adduser rundeck docker \
  && apt-get install --yes sshpass \
  && rm -rf /var/lib/apt/lists/*

# because this commit is stupid!
# https://github.com/rundeck/rundeck/commit/451f08de20de5c1389a4d3fdf9af2837b74b2798#diff-e6f6497ed67b3308e01a6cab264aa44a
RUN addgroup --gid 1000 rundeck && adduser rundeck rundeck

RUN  wget -nv -O /home/rundeck/rundeck-cli-all.jar \
     https://github.com/rundeck/rundeck-cli/releases/download/v1.1.7/rundeck-cli-1.1.7-all.jar \
  && echo "81749942ab0031e4e970a63df6e010fca3e891e842d7494cb423e5c8d7058e69  /home/rundeck/rundeck-cli-all.jar" | \
     sha256sum --check \
  && chown 1000:1000 /home/rundeck/rundeck-cli-all.jar
USER 1000

