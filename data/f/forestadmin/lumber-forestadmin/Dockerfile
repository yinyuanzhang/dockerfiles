FROM node:lts-jessie

WORKDIR /usr/src/app

VOLUME /usr/src/app

EXPOSE $APPLICATION_PORT
CMD npm install -g lumber-cli@2 -s && \
  lumber generate "${APPLICATION_NAME:-$APP_NAME}" \
    -c "$DATABASE_URL" \
    -S "${DATABASE_SSL:-false}" \
    -s "$DATABASE_SCHEMA" \
    -H "$APPLICATION_HOST" \
    -p "$APPLICATION_PORT" && \
  cd "${APPLICATION_NAME:-$APP_NAME}" && \
  npm install lumber-forestadmin -s --save && \
  lumber install lumber-forestadmin \
    --email "$FOREST_EMAIL" \
    --projectName "${APPLICATION_NAME:-$APP_NAME}" \
    --token "$FOREST_TOKEN" && \
  npm install -s
