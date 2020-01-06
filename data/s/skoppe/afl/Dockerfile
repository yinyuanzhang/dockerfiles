FROM base/devel

RUN pacman -Sy --noconfirm git gcc make && \
	git clone https://github.com/skoppe/afl && \
	cd afl && \
	make && \
	pacman -Rns git make && \
    find /. -name "*~" -type f -delete && \
    bash -c "echo 'y' | pacman -Scc >/dev/null 2>&1" && \
    paccache -rk0 >/dev/null 2>&1 &&  \
    pacman-optimize && \
    rm -r /var/lib/pacman/sync/*