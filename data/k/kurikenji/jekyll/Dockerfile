FROM alpine:3.8

RUN apk upgrade --update && \
    apk add libatomic readline readline-dev libxml2 libxml2-dev \
        ncurses-terminfo-base ncurses-terminfo \
        libxslt libxslt-dev zlib-dev zlib \
        ruby ruby-dev yaml yaml-dev \
        libffi-dev build-base git nodejs \
        ruby-io-console ruby-irb ruby-json ruby-rake && \
    gem install --no-document redcarpet kramdown maruku rdiscount RedCloth liquid pygments.rb && \
    gem install --no-document sass safe_yaml && \ 
    gem install --no-document jekyll -v 4.0 && \
    gem install --no-document jekyll-paginate jekyll-sass-converter webrick && \
    gem install --no-document jekyll-sitemap jekyll-feed jekyll-redirect-from && \
    gem install --no-document jekyll-theme-cayman bigdecimal bundler && \
#    apk del build-base zlib-dev ruby-dev readline-dev libxml2-dev && \
    rm -rf /root/src /tmp/* /usr/share/man /var/cache/apk/* && \
    apk search --update && \
    apk --no-cache add bash && \
    mkdir /workdir

WORKDIR /workdir
VOLUME ["/workdir"]
CMD ["bash"]


