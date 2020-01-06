# we want to build the jekyll site
FROM jekyll/minimal as builder

# Put everything into /news/
RUN mkdir /news/
WORKDIR /news/

# Add our sources into /srv/jekyll
ADD _includes /news/_includes
ADD _posts /news/_posts
ADD _config.yml /news/_config.yml
ADD news.json /news/news.json

# Run the build
RUN chown -R jekyll:jekyll /news/
RUN jekyll build

# Copy over the files
FROM pierrezemb/gostatic:latest
COPY --from=builder /news/_site /srv/http
EXPOSE 8043