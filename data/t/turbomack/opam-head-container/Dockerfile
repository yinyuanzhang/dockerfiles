FROM ocaml/opam
MAINTAINER Marek Fajkus <marek.faj@gmail.com>

# update opam
RUN cd /home/opam/opam-repository && git pull origin master
RUN opam update

# rebuild opam
RUN opam init
RUN eval `opam config env`
