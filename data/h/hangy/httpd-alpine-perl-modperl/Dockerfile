FROM hangy/httpd-alpine-perl-extended:0.1

#  Fetch mod_perl source, build and install it
#  Note: The fetch URL should be adjusted to point to a local mirror
ADD http://www.eu.apache.org/dist/perl/mod_perl-2.0.10.tar.gz mod_perl-2.0.10.tar.gz
RUN set -x \
    && ln -s /usr/lib/x86_64-linux-gnu/libgdbm.so.3.0.0 /usr/lib/libgdbm.so \
    && tar -zxvf mod_perl-2.0.10.tar.gz \
    && rm mod_perl-2.0.10.tar.gz \
    && cd mod_perl-2.0.10 \
    && perl Makefile.PL MP_AP_PREFIX=/usr/local/apache2 \
    && make \ 
    && make install \
    && cd .. \
    && rm -r mod_perl-2.0.10