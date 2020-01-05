FROM composer:1.6.5

# node-sass gets built from source (??) so we need the build-base package
RUN composer global require tightenco/jigsaw:v1.2.8 && \
	composer clear-cache && \
	apk update && \
	apk --no-cache add nodejs build-base && \
	npm install -g npm && \
	npm cache clean --force

ENV PATH="/tmp/vendor/bin:${PATH}"

CMD ["jigsaw"]
