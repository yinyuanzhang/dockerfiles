FROM mserajnik/hyve:latest
WORKDIR /usr/src/app/services/web
ENV VUE_APP_HYVE_API_URL="REEEEEEEEEEEEEEEEEEE" \
    VUE_APP_HYVE_ROBOTS="noindex, nofollow" \
    VUE_APP_HYVE_TITLE="hyve"
RUN envsubst < .env.docker > .env
RUN yarn build

FROM alpine
ENTRYPOINT ["/entrypoint.sh"]
HEALTHCHECK --interval=10s --timeout=5s --retries=3 \
  CMD wget --quiet --tries=1 --no-check-certificate --spider \
  http://localhost:80 || exit 1
COPY --from=legsplits/hydrus-web:latest /sbin/nweb /sbin/nweb
COPY entrypoint.sh /entrypoint.sh
COPY --from=0 /usr/src/app/services/web/dist /hyve-web