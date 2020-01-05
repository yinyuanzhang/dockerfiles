FROM joblocal/core:latest

LABEL maintainer="joblocal GmbH <produktentwicklung@joblocal.de>"

RUN apt-get update \
	&& apt-get -y --no-install-recommends install \
		texlive-latex-extra \
		texlive-lang-german \
		texlive-fonts-recommended \
		texlive-fonts-extra \
		lmodern \
		latex-xcolor \
		pgf \
	&& apt-get -y autoremove \
	&& apt-get clean \
	&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

COPY ./rootfs /
