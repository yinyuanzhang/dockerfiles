FROM vvoronin/ubuntu-tools
MAINTAINER Viktor Voronin <voronin@x12.su>

RUN /tools/apt build-essential wget
 
ENV PERLBREW_ROOT=/perl5

RUN bash -c '\wget -O - http://install.perlbrew.pl | bash' &&\
		/perl5/bin/perlbrew init &&\
		/perl5/bin/perlbrew install -j 4 perl-5.20.1 &&\
		/perl5/bin/perlbrew install-cpanm &&\
		/perl5/bin/perlbrew switch perl-5.20.1
		
ENV PERLBREW_ROOT=/perl5 \
	PATH=/perl5/bin:/perl5/perls/perl-5.20.1/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin \
	PERLBREW_PERL=perl-5.20.1 \
	PERLBREW_VERSION=0.73 \
	PERLBREW_MANPATH=/perl5/perls/perl-5.20.1/man \
	PERLBREW_PATH=/perl5/bin:/perl5/perls/perl-5.20.1/bin \
	PERLBREW_SKIP_INIT=1
