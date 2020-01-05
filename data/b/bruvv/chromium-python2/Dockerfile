FROM debian:stable-slim

ARG DEBIAN_FRONTEND=noninteractive
ENV TZ=Europe/Amsterdam

#update all
RUN apt-get update && apt-get -y upgrade \
  && apt-get install -y --no-install-recommends apt-utils \
  && apt-get install -y wget gnupg unzip xvfb libxi6 libgconf-2-4

#install chrome
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - \
    && sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list' \
    && apt-get update \
    && apt-get install -y google-chrome-stable python python-pip curl libappindicator1 locales
    
RUN wget -N http://chromedriver.storage.googleapis.com/75.0.3770.90/chromedriver_linux64.zip -P ~/ \
    && unzip ~/chromedriver_linux64.zip -d ~/ \
    && rm ~/chromedriver_linux64.zip \
    && mv ~/chromedriver /usr/local/bin/chromedriver \
    && chmod 0755 /usr/local/bin/chromedriver

RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone


RUN chmod 0755 /etc/default/locale

RUN localedef -i nl_NL -c -f UTF-8 -A /usr/share/locale/locale.alias nl_NL.UTF-8
ENV LC_ALL=nl_NL.UTF-8
ENV LANG=nl_NL.UTF-8
ENV LANGUAGE=nl_NL.UTF-8


RUN sed -i -e 's/# nl_NL.UTF-8 UTF-8/nl_NL.UTF-8 UTF-8/' /etc/locale.gen && \
    dpkg-reconfigure --frontend=noninteractive locales && \
    update-locale LANG=nl_NL.UTF-8
    
RUN pip install selenium

RUN rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /usr/share/man/?? /usr/share/man/??_*
RUN apt-get autoremove && apt-get autoclean

RUN rm -f /etc/localtime

RUN ln -s /usr/share/zoneinfo/Europe/Amsterdam /etc/localtime

WORKDIR /script

#ONBUILD COPY requirements.txt /script/requirements.txt
ONBUILD RUN pip install -r /script/requirements.txt
#ONBUILD COPY . /usr/src/app

CMD /script/run.sh
