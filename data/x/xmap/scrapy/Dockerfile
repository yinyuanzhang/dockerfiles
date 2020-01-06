FROM revolutionsystems/python:3.8.0-wee-optimized-lto

RUN apt-get update \
  && apt-get install -y --no-install-recommends gcc python3-dev libmagic-dev libxml2-dev libxslt1-dev zlib1g-dev libffi-dev libssl-dev \
  && pip install scrapy scrapy-fake-useragent beautifulsoup4 python-magic lxml pillow \
  && rm -rf /var/lib/apt/lists/*

CMD ["scrapy", "shell", "--nolog"]
