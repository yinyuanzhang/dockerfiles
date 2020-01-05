FROM qnib/plain-audioguide:2019-05-20.2 AS build

WORKDIR /home/jekyll/project
COPY ./assets ./assets
COPY ./_config.yml ./_config.yml
COPY ./_includes ./_includes
COPY ./audio ./audio
COPY ./stops ./stops
USER root
RUN chown -R jekyll .
RUN bundle exec jekyll build

FROM qnib/plain-caddy
COPY --from=build /home/jekyll/project/_site /srv
