FROM archlinux/base

RUN pacman -Syy --noconfirm pacman-contrib curl sed --needed && \
	curl -s "https://www.archlinux.org/mirrorlist/?country=FR&country=GB&use_mirror_status=on" | sed -e 's/^#Server/Server/' -e '/^#/d' | rankmirrors -n 6 - > /etc/pacman.d/mirrorlist && \
	pacman -Syyu --noconfirm --needed \
		pandoc \
		texlive-core \
		texlive-pictures \
		texlive-bibtexextra \
		texlive-pstricks \
		texlive-latexextra \
		ca-certificates \
		biber \
		make \
		git \
		git-lfs \
		inkscape \
		librsvg && \
	pacman -Scc --noconfirm && \
	rm -rf /var/lib/pacman/sync /tmp/* /var/tmp/*

ENV PATH="/usr/bin/vendor_perl/:${PATH}"

CMD /bin/sh
