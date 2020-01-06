FROM debian:wheezy

RUN apt-get update -y && apt-get install --no-install-recommends -y -q curl nginx git
RUN mkdir /nodejs && curl http://nodejs.org/dist/latest-v5.x/node-v5.10.0-linux-x64.tar.gz  | tar xvzf - -C /nodejs --strip-components=1

ENV PATH $PATH:/nodejs/bin

CMD ["/usr/sbin/nginx", "-g", "daemon off; "]