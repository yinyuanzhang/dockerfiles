FROM ruby:2.2

RUN printf "deb http://archive.debian.org/debian/ jessie main\ndeb-src http://archive.debian.org/debian/ jessie main\ndeb http://security.debian.org jessie/updates main\ndeb-src http://security.debian.org jessie/updates main" > /etc/apt/sources.list
RUN apt-get update \
 && apt-get install gettext-base --yes \
 && apt-get clean all \
 && rm -rf /var/lib/apt/lists/*

RUN gem install i18n -v 1.5.1
RUN gem install fluentd

# Mix-in modules
RUN fluent-gem install fluent-mixin-config-placeholders
RUN fluent-gem install fluent-mixin-plaintextformatter

# Splunk output plugin for Fluent event collector.
RUN fluent-gem install fluent-plugin-splunk-http-eventcollector

# Enrich your fluentd events with Kubernetes metadata
RUN fluent-gem install fluent-plugin-kubernetes_metadata_filter

# Fluentd Output filter plugin to rewrite tags that matches specified attribute.
RUN fluent-gem install fluent-plugin-rewrite-tag-filter

COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
# Run the Fluentd service.
ENTRYPOINT ["/entrypoint.sh"]
