# fluentd/Dockerfile
FROM fluent/fluentd:v1.2-debian
ADD conf/* /fluentd/etc/
RUN ["gem", "install", "fluent-plugin-elasticsearch", "--no-rdoc", "--no-ri", "--version", "2.6.1"]
RUN ["gem", "install", "fluent-plugin-concat", "--no-rdoc", "--no-ri", "--version", "2.2.0"] 
