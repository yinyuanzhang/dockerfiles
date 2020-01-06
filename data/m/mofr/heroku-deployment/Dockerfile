FROM codeship/heroku-deployment

ENV CACHE_BUST='2019-09-26'

RUN apt-get update && apt-get install -y --no-install-recommends git devscripts
RUN curl -sL https://sentry.io/get-cli/ | bash
