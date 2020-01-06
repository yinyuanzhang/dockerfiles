FROM kennethreitz/pipenv

COPY . /app

CMD while true; do (scrapy crawl pinurl); echo 'delay 600'; sleep 600; done