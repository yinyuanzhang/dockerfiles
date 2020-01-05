FROM funkypenguin/grinpool-mwnginx-dockerbase

ARG BUILD_DATE
ARG VCS_REF

# Good docker practice, plus we get microbadger badges
LABEL org.label-schema.build-date=$BUILD_DATE \
      org.label-schema.vcs-url="https://github.com/funkypenguin/grin-pool.git" \
      org.label-schema.vcs-ref=$VCS_REF \
      org.label-schema.schema-version="2.2-r1"

EXPOSE 80
EXPOSE 443
EXPOSE 3332
EXPOSE 3333
EXPOSE 3334
EXPOSE 13416
EXPOSE 23416

# General
COPY src/nginx.conf /etc/nginx/nginx.conf

# Proxy Config
COPY src/stratum_proxy_params  /etc/nginx/stratum_proxy_params

# mwgrinpool.com
RUN mkdir -p /mwgrinpool.com/
COPY src/mwgrinpool.stream.conf /mwgrinpool.com/mwgrinpool.stream.conf
COPY src/mwgrinpool.http.conf /mwgrinpool.com/mwgrinpool.http.conf

RUN touch XY
# mwgrinpool.com
RUN mkdir -p /mwfloopool.com/
COPY src/mwfloopool.stream.conf /mwfloopool.com/mwfloopool.stream.conf
COPY src/mwfloopool.http.conf /mwfloopool.com/mwfloopool.http.conf
