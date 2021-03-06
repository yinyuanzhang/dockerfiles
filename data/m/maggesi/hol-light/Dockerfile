### ===========================================================================
### Container for running HOL Light.
###
### Nix on Alpine image with OCaml, elpi, dmtcp and other tools installed.
### ===========================================================================

FROM nixos/nix

USER root

# Add normal user "worker" and prepare a directory /home/worker/work
# Then install HOL Light and dependencies using Nix
# NB: Library num is a separate package for recent versions of OCaml
      # nixpkgs.ocaml-ng.ocamlPackages_4_07.num \

RUN addgroup -S workgroup \
 && adduser -S worker -G workgroup \
 && mkdir /home/worker/work \
 && nix-channel --add https://nixos.org/channels/nixpkgs-unstable nixpkgs \
 && nix-channel --update \
 && nix-env -iA \
      nixpkgs.ocaml-ng.ocamlPackages_4_05.ocaml \
      nixpkgs.ocaml-ng.ocamlPackages_4_05.camlp5 \
      nixpkgs.ocaml-ng.ocamlPackages_4_05.findlib \
      nixpkgs.ocaml-ng.ocamlPackages_4_05.elpi \
      nixpkgs.bash \
      nixpkgs.rlwrap \
      nixpkgs.dmtcp \
      nixpkgs.screen \
 && nix-channel --remove nixpkgs \
 && nix-collect-garbage -d

# Change user and working directory.
USER worker
WORKDIR /home/worker
CMD ["ocaml"]
