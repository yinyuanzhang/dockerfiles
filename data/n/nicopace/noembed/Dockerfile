FROM perl:5.20
MAINTAINER nico@libre.ws
RUN apt-get update && apt-get -y install libgif-dev cpanminus wget git python-setuptools python-dev build-essential && easy_install pygments && rm -rf /var/lib/apt/lists/*
WORKDIR /usr/src/myapp
RUN git clone --depth=1 https://github.com/leedo/noembed.git .
RUN cpan Module::Install Module::Find Class::Load Text::MicroTemplate::File AnyEvent::Fork AnyEvent::HTTP Plack::Builder Plack::Handler::Twiggy
RUN PERL_CPANM_OPT="--skip-installed --notest --auto-cleanup=0" cpanm . 
RUN perl Makefile.PL
RUN make
WORKDIR /usr/src/myapp/eg/
COPY files/lib/Noembed/Util.pm ../lib/Noembed/Util.pm
EXPOSE 5000
CMD [ "plackup", "-I../lib", "app.psgi" ]
