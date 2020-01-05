FROM nixos/nix

RUN nix-channel --add https://nixos.org/channels/nixpkgs-unstable nixpkgs
RUN nix-channel --update

RUN nix-env -iA nixpkgs.bashInteractive
RUN nix-env -iA nixpkgs.git
RUN rm -rf /root/.cache/nix/*

