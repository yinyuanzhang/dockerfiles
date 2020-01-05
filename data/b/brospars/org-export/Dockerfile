FROM debian:testing
ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update && apt-get -y install emacs24

ADD install.el /emacs/install.el
WORKDIR /emacs
ENV HOME /emacs
RUN emacs --batch --load install.el
ADD export.el /emacs/export.el
ADD org-export.sh /emacs/org-export.sh

ENV LANG en_US.UTF-8
