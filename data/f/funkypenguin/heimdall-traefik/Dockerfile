FROM linuxserver/heimdall:latest

# Now we DO need these, for the auto-labeling of the image
ARG BUILD_DATE
ARG VCS_REF

# Good docker practice, plus we get microbadger badges
LABEL org.label-schema.build-date=$BUILD_DATE \
      org.label-schema.vcs-url="https://github.com/funkypenguin/oauth2_proxy.git" \
      org.label-schema.vcs-ref=$VCS_REF \
      org.label-schema.schema-version="2.2-r1"

RUN echo -e "\nFORCE_HTTPS=true" >> /var/www/localhost/heimdall/.env
