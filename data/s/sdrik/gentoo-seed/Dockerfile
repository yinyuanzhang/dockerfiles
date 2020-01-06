ARG flavor
ARG portage
ARG jobs=2

FROM sdrik/gentoo-portage:${portage} as portage
FROM sdrik/gentoo-system:${flavor}

ARG flavor
ARG jobs

RUN rm -rf /usr/portage /usr/local/portage

COPY --from=portage /usr/portage /usr/portage
COPY . /usr/local/portage

ENV ATHOME_FLAVOR=${flavor}
ENV EMERGE_DEFAULT_OPTS="--binpkg-respect-use=y --binpkg-changed-deps=y --usepkgonly=y --getbinpkgonly=y"

RUN echo "${flavor}" > /.flavor; \
	rm -rf /etc/portage/patches; \
	ln -s /usr/local/portage/profiles/patches /etc/portage/patches; \
	tar c -C /usr/local/portage/seed/common/ . | tar x -C /etc/portage/; \
	rm -rf /usr/local/portage/seed/common; \
	tar c -C /usr/local/portage/seed/${flavor}/ . | tar x -C /etc/portage/; \
	rm -rf /usr/local/portage/seed/${flavor}; \
	mv /usr/local/portage/seed/athome-{entrypoint,flavor,clean-bintree} /usr/bin/; \
	rm -rf /usr/local/portage/seed; \
	profile=$(athome-flavor --profile); \
	if [ -f /usr/local/portage/profiles/${profile}/eapi ]; \
	then ln -sfn /usr/local/portage/profiles/${profile} /etc/portage/make.profile; \
	elif [ -f /usr/portage/profiles/${profile}/eapi ]; \
	then ln -sfn /usr/portage/profiles/${profile} /etc/portage/make.profile; \
	else echo "Missing profile ${profile}"; exit 1; \
	fi

RUN egencache --repo AtHome --update && emerge --metadata --jobs=${jobs}

ENTRYPOINT ["/usr/bin/athome-entrypoint"]
CMD ["/bin/bash", "--login"]

ONBUILD ENTRYPOINT ["/usr/bin/athome-entrypoint"]
ONBUILD CMD ["/bin/bash", "--login"]
