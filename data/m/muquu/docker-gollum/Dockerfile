FROM ruby

RUN apt-get -y update && apt-get -y install libicu-dev cmake && rm -rf /var/lib/apt/lists/*
RUN ln -fs /usr/share/zoneinfo/Asia/Tokyo /etc/localtime
RUN gem install github-linguist
RUN gem install gollum
RUN gem install org-ruby  # optional
WORKDIR /wiki
ENTRYPOINT ["gollum", "--port", "80", "--bare", "--emoji", "--allow-uploads", "--css", "--js"]
EXPOSE 80
