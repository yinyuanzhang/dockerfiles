FROM tclavier/nginx

RUN apt-get update \
 && apt-get install -y \
    imagemagick \
    make \
    git \
    wget \
 && apt-get clean

RUN wget https://github.com/spf13/hugo/releases/download/v0.40/hugo_0.40_Linux-64bit.deb -O /tmp/hugo.deb \
 && dpkg -i /tmp/hugo.deb \
 && rm -f /tmp/hugo.deb

# Analyse script
RUN apt-get update \
&& apt-get install -y \
   python-bs4 \
   python-docopt \
   python-urllib3 \
   python-yaml \
&& apt-get clean

COPY . /site
WORKDIR /site

RUN make download_images && make assets
RUN hugo_env=production hugo --buildFuture --destination=/var/www/prod
RUN hugo --buildDrafts --buildFuture --destination=/var/www/draft \
 && echo "User-agent: *" > /var/www/draft/robots.txt \
 && echo "Disallow:/ "  >> /var/www/draft/robots.txt

COPY nginx_vhost.conf /etc/nginx/conf.d/ajiro.conf
