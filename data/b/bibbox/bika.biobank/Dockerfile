FROM python:2.7
# FROM bika_plone

MAINTAINER Thoba Lose 'thoba@sanbi.ac.za' and Hocine Bendou 'hocine@sanbi.ac.za'

RUN useradd --system -U -u 500 plone \
 && mkdir -p /plone /data/filestorage /data/blobstorage \
 && chown -R plone:plone /plone /data

ENV PLONE_MAJOR=4.3
ENV PLONE_VERSION=4.3.7
ENV PLONE_MD5=b4ece39a6dda7a72c9084057d8faae4f
RUN buildDeps="curl sudo git python-setuptools python-dev build-essential libssl-dev libxml2-dev libxslt1-dev libbz2-dev libjpeg62-turbo-dev" \
 && runDeps="libxml2 libxslt1.1 libjpeg62" \
 && apt-get update \
 && apt-get install -y --no-install-recommends $buildDeps \
 && curl -o Plone.tgz -SL https://launchpad.net/plone/$PLONE_MAJOR/$PLONE_VERSION/+download/Plone-$PLONE_VERSION-UnifiedInstaller.tgz \
 && echo "$PLONE_MD5 Plone.tgz" | md5sum -c - \
 && tar -xzf Plone.tgz \
 && ./Plone-$PLONE_VERSION-UnifiedInstaller/install.sh \
      --password=admin \
      --daemon-user=plone \
      --owner=plone \
      --group=plone \
      --target=/plone \
      --instance=instance \
      --var=/data \
      zeo \
 && rm -rf Plone*

RUN git clone -b inventory https://github.com/bikalabs/bika.lims.git /bika.lims \

     && git clone https://github.com/rockfruit/bika.sanbi.git /bika.sanbi

COPY buildout.cfg /plone/instance/buildout.cfg

RUN chown -R plone:plone /plone /data /bika.lims /bika.sanbi \
 && cd /plone/instance \
 && sudo -u plone bin/buildout \
 && SUDO_FORCE_REMOVE=yes apt-get purge -y --auto-remove $buildDeps \
 && apt-get install -y --no-install-recommends $runDeps \
 && rm -rf /var/lib/apt/lists/* \
 && rm -rf /plone/buildout-cache/downloads/* \
 && find /plone \( -type f -a -name '*.pyc' -o -name '*.pyo' \) -exec rm -rf '{}' +

VOLUME /data/filestorage /data/blobstorage

COPY docker-entrypoint.sh /docker-entrypoint.sh

RUN chmod +x /docker-entrypoint.sh

EXPOSE 8080

USER plone

WORKDIR /plone/instance

ENTRYPOINT ["/docker-entrypoint.sh"]

CMD ["start"]
