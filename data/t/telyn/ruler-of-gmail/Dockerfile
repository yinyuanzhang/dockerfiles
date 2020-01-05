FROM perl as compiler
RUN cpan install File::ShareDir::Install && cpan install XML::Output
COPY compile.pl /usr/bin/rog
