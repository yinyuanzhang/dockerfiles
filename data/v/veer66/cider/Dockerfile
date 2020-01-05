FROM debian:sid
RUN apt-get update -y && apt-get upgrade -y && apt-get install --no-install-recommends -y emacs clojure leiningen
COPY .emacs /root
COPY install.el .
RUN emacs --batch --load install.el
RUN mkdir -p /work
WORKDIR "/work"
