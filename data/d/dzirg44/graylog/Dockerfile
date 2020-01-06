FROM graylog/graylog:3.1
ARG SSO_PLUGIN_VERSION=3.1.0
ARG SSO_PLUGIN_URL=https://github.com/Graylog2/graylog-plugin-auth-sso/releases/download/${SSO_PLUGIN_VERSION}/graylog-plugin-auth-sso-${SSO_PLUGIN_VERSION}.jar
ARG SSO_PLUGIN_PATH=/usr/share/graylog/plugin/graylog-plugin-auth-sso-${SSO_PLUGIN_VERSION}.jar
RUN curl --create-dirs -SLo ${SSO_PLUGIN_PATH} ${SSO_PLUGIN_URL}
