FROM abernix/meteord:node-4-base
RUN apt-get update
RUN apt-get install wget -y
RUN apt-get install apt-utils -y
RUN apt-get install graphicsmagick -y
RUN apt-get install libdigest-hmac-perl -y
RUN apt-get install libfile-copy-recursive-perl -y
RUN apt-get install libio-tee-perl -y
RUN apt-get install libunicode-string-perl -y
RUN apt-get install libmail-imapclient-perl -y
RUN apt-get install libterm-readkey-perl -y
RUN apt-get install makepasswd rcs perl-doc libio-tee-perl git libmail-imapclient-perl libdigest-md5-file-perl libterm-readkey-perl libfile-copy-recursive-perl make automake build-essential libunicode-string-perl -y
RUN apt-get install libauthen-ntlm-perl libcrypt-ssleay-perl libdigest-hmac-perl libfile-copy-recursive-perl libio-compress-perl libio-socket-inet6-perl libio-socket-ssl-perl libio-tee-perl libmodule-scandeps-perl libnet-ssleay-perl libpar-packer-perl libreadonly-perl libterm-readkey-perl libtest-pod-perl libtest-simple-perl libunicode-string-perl liburi-perl cpanminus -y
RUN apt-get install -y --fix-missing g++ curl libssl-dev apache2-utils git libxml2-dev sshfs cpanminus makepasswd rcs perl-doc libio-tee-perl git libmail-imapclient-perl libdigest-md5-file-perl libterm-readkey-perl libfile-copy-recursive-perl libauthen-ntlm-perl libcrypt-ssleay-perl libdigest-hmac-perl libfile-copy-recursive-perl libio-compress-perl libio-socket-inet6-perl libio-socket-ssl-perl libio-tee-perl libmodule-scandeps-perl libnet-ssleay-perl libpar-packer-perl libterm-readkey-perl libtest-pod-perl libtest-simple-perl libunicode-string-perl cpanminus

RUN sed -i -e 's/# en_US.UTF-8 UTF-8/en_US.UTF-8 UTF-8/' /etc/locale.gen && locale-gen
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US:en  
ENV LC_ALL en_US.UTF-8

RUN cpanm "Class::Load"
RUN cpanm "Crypt::OpenSSL::RSA"
RUN cpanm "Data::Uniqid"
RUN cpanm "Dist::CheckConflicts"
RUN cpanm "JSON"
RUN cpanm "JSON::WebToken"
RUN cpanm "JSON::WebToken::Crypt::RSA"
RUN cpanm "Module::Implementation"
RUN cpanm "Module::Runtime"
RUN cpanm "Package::Stash"
RUN cpanm "Package::Stash::XS"
RUN cpanm "Readonly"
RUN cpanm "Sys::MemInfo"
RUN cpanm "Test::Fatal"
RUN cpanm "Test::Mock::Guard"
RUN cpanm "Test::MockObject"
RUN cpanm "Test::Requires"
RUN cpanm "Try::Tiny"
RUN cpanm "Regexp::Common"

WORKDIR /usr/src
RUN export PERL_MM_USE_DEFAULT=1
RUN perl -MCPAN -e 'install Unicode::String'
WORKDIR "/usr/src"
RUN git clone git://github.com/imapsync/imapsync.git /usr/src/imapsync
WORKDIR "/usr/src/imapsync"
RUN make install
RUN mkdir dist

RUN wget https://gist.githubusercontent.com/lanmower/38e6175febd8b9a567cc9755ce7221db/raw/ad869f2abf0e56e0c83a3b7595e583de3d04f131/ffdshow.sh -O /tmp/ffmpeg.sh
RUN chmod +x /tmp/ffmpeg.sh
RUN /tmp/ffmpeg.sh
VOLUME ["/store/cfs"]
