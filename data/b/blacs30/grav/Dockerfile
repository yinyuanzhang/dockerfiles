FROM blacs30/grav:1.6.16

ADD data /provided/

ENV GRAV_ADDITIONS haywire,cacti,archives,tagcloud,highlight,bibleref,relatedpages,feed,taxonomylist

RUN cd /var/www/html; for i in $(echo $GRAV_ADDITIONS | sed "s/,/ /g"); \
  do \
  echo "[ INFO ] Installing grav plugin/theme: $i" \
  bin/gpm --quiet install "$i"; \
  done
