FROM rails:4.2

EXPOSE 3000

## TODO: use git clone of the rails apps instead of COPY 
COPY /rails/blog /data/blog
RUN cd /data/blog && \
  bundle install

WORKDIR /data/blog
CMD rails server
