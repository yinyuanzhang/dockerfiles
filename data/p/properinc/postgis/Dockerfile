FROM mdillon/postgis:9.6

RUN localedef -i ja_JP -c -f UTF-8 -A /usr/share/locale/locale.alias ja_JP.UTF-8

# netcat: script/create_masked_database-gae.sh uses nc(1)
RUN apt-get update -qq && \
    apt-get install -y apt-transport-https && \
    apt-get -y install netcat
