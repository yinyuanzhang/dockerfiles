FROM ubuntu-debootstrap:14.04
ADD . /app
ADD ./entrypoint.sh /
WORKDIR /app
RUN LC_ALL=C DEBIAN_FRONTEND=noninteractive /app/docker-install-dependencies.sh \
  &&  groupadd -r mevoj \
  &&  useradd -r -g mevoj mevoj \
  &&  mkdir /home/mevoj \
  &&  chown -R mevoj:mevoj /home/mevoj \
  &&  cat .gitignore | egrep -v "(^#.*|^$)" | xargs rm -rf \
  &&  rm -rf .git/ .editorconfig docker-compose.yml README.md Dockerfile LICENSE start-docker.sh \
  &&  touch .create-admin \
  &&  npm install \
  &&  chown -R mevoj:mevoj /app
EXPOSE 1337
EXPOSE 2222
CMD /entrypoint.sh
