FROM housmart/ruby-tesseract

RUN apt-get update -qq && \
    apt-get install -y build-essential libpq-dev && \
    curl -sL https://deb.nodesource.com/setup_9.x | bash - && \
    apt-get install -y nodejs && \
    npm install -g n && \
    n stable && \
    npm install -g yarn && \
    apt-get install -y python-dev && \
    wget https://bootstrap.pypa.io/get-pip.py && \
    python get-pip.py && \
    pip install awscli
