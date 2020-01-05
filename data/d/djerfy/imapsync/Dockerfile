FROM ubuntu:18.10
LABEL description="Docker ImapSync" \
      maintainer="Djerfy <djerfy@gmail.com>" \
      documentation="https://jesuisadmin.fr/migrer-emails-facilement-imapsync/"

RUN set -xe && \
    apt-get update && \
    apt-get install -y make cpanminus wget \
        libauthen-ntlm-perl libclass-load-perl \
        libcrypt-ssleay-perl libdata-uniqid-perl \
        libdigest-hmac-perl libdist-checkconflicts-perl \
        libfile-copy-recursive-perl libio-compress-perl \
        libio-socket-inet6-perl libio-socket-ssl-perl \
        libio-tee-perl libmail-imapclient-perl \
        libmodule-scandeps-perl libnet-ssleay-perl \
        libpar-packer-perl libreadonly-perl \
        libsys-meminfo-perl libterm-readkey-perl \
        libtest-fatal-perl libtest-mock-guard-perl \
        libtest-pod-perl libtest-requires-perl \
        libtest-simple-perl libunicode-string-perl \
        liburi-perl && \
    cpanm Mail::IMAPClient && \
    cpanm JSON::WebToken && \
    cpanm Regexp::Common

RUN set -xe && \
    wget -q -O /usr/bin/imapsync.pl https://imapsync.lamiral.info/dist/imapsync && \
    chmod +x /usr/bin/imapsync.pl

ENTRYPOINT ["/usr/bin/imapsync.pl"]
