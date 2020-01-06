ARG CLI_IMAGE
FROM ivrh/library-cli as cli

FROM govcms8lagoon/nginx-drupal

COPY --from=cli /app /app
