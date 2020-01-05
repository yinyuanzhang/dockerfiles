FROM ubuntu:latest
RUN apt-get -qq update; apt-get -qqy install mercurial
RUN hg clone https://hg.prosody.im/prosody-modules/ /usr/lib/prosody/extra-modules/

FROM prosody/prosody:0.11
USER root
COPY --from=0 /usr/lib/prosody/extra-modules/ /usr/lib/prosody/extra-modules/
RUN apt-get -qq update; apt-get -qqy install lua-ldap lua-socket lua-sec lua-event lua-dbi-mysql

ENV EXTRA_MODULES "blocking smacks presence_cache smacks_offline cloud_notify auth_ldap http_upload omemo_all_access pep_vcard_avatar migrate vcard_muc"
RUN for MOD in ${EXTRA_MODULES}; do ln -s /usr/lib/prosody/extra-modules/mod_${MOD} /usr/lib/prosody/modules/; done

ADD https://launchpad.net/ubuntu/+source/lua-ldap/1.2.3-1/+build/15747230/+files/lua-ldap_1.2.3-1_amd64.deb /tmp/lua-ldap_1.2.3-1_amd64.deb
RUN dpkg -i /tmp/lua-ldap_1.2.3-1_amd64.deb

# add to external group: ssl-cert (115)
RUN groupadd -g 115 ssl-cert-ex; usermod -a -G ssl-cert-ex prosody

USER prosody