FROM ocaml/opam:ubuntu-16.04_ocaml-4.04.0
RUN sudo apt-get update && sudo apt-get install -yq wget git emacs24-nox proofgeneral 
RUN opam install -y camlp5 ocamlfind
RUN opam repo add coq-released https://coq.inria.fr/opam/released
RUN opam install -y coq.8.6 coq-mathcomp-ssreflect.1.6.1 coq-mathcomp-algebra
RUN mkdir /home/opam/.emacs.d
COPY init.el /home/opam/.emacs.d/
RUN sudo chown opam:opam /home/opam/.emacs.d/init.el











