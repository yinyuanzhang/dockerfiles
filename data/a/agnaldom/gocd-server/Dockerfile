FROM gocd/gocd-server:v19.1.0

RUN mkdir -p  /godata/plugins/external/

RUN  curl --location --fail  https://github.com/Vincit/gocd-slack-task/releases/download/v1.3.1/gocd-slack-task-1.3.1.jar > /godata/plugins/external/gocd-slack-task-1.3.1.jar

RUN curl --location --fail  https://github.com/tomzo/gocd-rocketchat-plugin/releases/download/0.1.1/gocd-rocketchat-plugin-0.1.1.jar > /godata/plugins/external/gocd-rocketchat-plugin-0.1.1.jar
RUN curl --location --fail  https://github.com/gocd-contrib/email-notifier/releases/download/0.2-exp/email-notifier-0.2.jar > /godata/plugins/external/email-notifier-0.2.jar

#RUN curl --location --fail https://dl.bintray.com/suhanlee/maven/com/devsh/suhanlee/slack-message/0.1.3/:slack-message-0.1.3-sources.jar > /godata/plugins/external/slack-message-0.1.3-sources.jar

RUN curl --location --fail  https://github.com/paullalonde/gocd-sns-notification-plugin/releases/download/v0.7/sns-notification-plugin-0.7.jar > /godata/plugins/external/sns-notification-plugin-0.7.jar

RUN curl --location --fail  https://github.com/gocd-contrib/google-oauth-authorization-plugin/releases/download/2.0.0/google-oauth-authorization-plugin-2.0.0-7.jar > /godata/plugins/external/google-oauth-authorization-plugin-2.0.0-7.jar 
RUN curl --location --fail https://github.com/cnorthwood/gocd-tls-auth/releases/download/2.0.0/gocd-tls-auth-2.0.0.jar > /godata/plugins/external/gocd-tls-auth-2.0.0.jar
RUN curl --location --fail https://github.com/gocd-contrib/guest-login-plugin/releases/download/1.0.2/gocd-guest-login-plugin-1.0.2-27.jar > /godata/plugins/external/gocd-guest-login-plugin-1.0.2-27.jar
RUN curl --location --fail https://github.com/4finance/go-plugin-groovy/releases/download/1.0.1/go-plugin-groovy-1.0.1.jar > /godata/plugins/external/go-plugin-groovy-1.0.1.jar 
RUN curl --location --fail https://github.com/tomzo/gocd-json-config-plugin/releases/download/0.2.1/json-config-plugin-0.2.1.jar > /godata/plugins/external/json-config-plugin-0.2.1.jar 
RUN curl --location --fail https://github.com/tomzo/gocd-yaml-config-plugin/releases/download/0.6.2/yaml-config-plugin-0.6.2.jar > /godata/plugins/external/yaml-config-plugin-0.6.2.jar 
#RUN curl --location --fail https://github.com/gocd/kubernetes-elastic-agents/releases/download/2.1.0-123/kubernetes-elastic-agent-2.1.0-123.jar > /godata/plugins/external/kubernetes-elastic-agent-2.1.0-123.jar
#RUN curl --location --fail https://github.com/gocd-contrib/docker-elastic-agents/releases/download/v2.2.0/docker-elastic-agents-2.2.0-187.jar > /godata/plugins/external/docker-elastic-agents-2.2.0-187.jar 
RUN curl --location --fail https://github.com/varchev/go-npm-poller/releases/download/0.3.1/go-npm-poller.jar > /godata/plugins/external/go-npm-poller.jar
RUN curl --location --fail https://github.com/eaiesb/Gocd-Artifactory-Plugin/releases/download/1.0/Artifactory-Plugin.jar > /godata/plugins/external/Artifactory-Plugin.jar 
RUN curl --location --fail  https://github.com/gocd-contrib/gem-repo-poller/releases/download/0.1/gem-repo-poller-0.1.jar > /godata/plugins/external/gem-repo-poller-0.1.jar 
RUN curl --location --fail https://github.com/indix/gocd-s3-artifacts/releases/download/v5.1.0/s3fetch-assembly-v5.1.0.jar > /godata/plugins/external/s3fetch-assembly-v5.1.0.jar 
RUN curl --location --fail https://github.com/indix/gocd-s3-artifacts/releases/download/v5.1.0/s3material-assembly-v5.1.0.jar > /godata/plugins/external/s3material-assembly-v5.1.0.jar 
RUN curl --location --fail https://github.com/indix/gocd-s3-artifacts/releases/download/v5.1.0/s3publish-assembly-v5.1.0.jar > /godata/plugins/external/s3publish-assembly-v5.1.0.jar 
RUN curl --location --fail https://github.com/cnenning/go-artifactory-scm-plugin/releases/download/0.9/go-artifactory-pkg-plugin-0.9.jar > /godata/plugins/external/go-artifactory-pkg-plugin-0.9.jar
RUN curl --location --fail https://github.com/TWChennai/gocd-git-path-material-plugin/releases/download/1.2.3/gocd-git-path-material-plugin-1.2.3.jar > /godata/plugins/external/gocd-git-path-material-plugin-1.2.3.jar 
RUN curl --location --fail https://github.com/ashwanthkumar/gocd-build-github-pull-requests/releases/download/v1.3.5/github-pr-poller-1.3.5.jar > /godata/plugins/external/github-pr-poller-1.3.5.jar 
RUN curl --location --fail https://github.com/TWChennai/gocd-git-path-material-plugin/releases/download/1.2.3/gocd-git-path-material-plugin-1.2.3.jar > /godata/plugins/external/gocd-git-path-material-plugin-1.2.3.jar 
RUN curl --location --fail https://github.com/manojlds/gocd-docker/releases/download/0.1.27/docker-task-assembly-0.1.27.jar > /godata/plugins/external/docker-task-assembly-0.1.27.jar 
RUN curl --location --fail https://github.com/Haufe-Lexware/gocd-plugins/releases/download/v1.0.0-beta/gocd-docker-pipeline-plugin-1.0.0.jar > /godata/plugins/external/gocd-docker-pipeline-plugin-1.0.0.jar \
RUN curl --location --fail https://github.com/cma-arnold/gocd-docker-exec-plugin/releases/download/1.0.0/gocddockerexecplugin-1.0.0.jar > /godata/plugins/external/gocddockerexecplugin-1.0.0.jar 
RUN curl --location --fail https://github.com/jmnarloch/gocd-health-check-plugin/releases/download/1.0.2/gocd-health-check-plugin-1.0.2.jar > /godata/plugins/external/gocd-health-check-plugin-1.0.2.jar 
RUN curl --location --fail https://github.com/tispr/gocd-opsworks-plugin/archive/gocd-opsworks-plugin-0.0.2.tar.gz > /godata/plugins/external/gocd-opsworks-plugin-0.0.2.tar.gz 
RUN curl --location --fail https://github.com/gocd-contrib/script-executor-task/releases/download/0.3/script-executor-0.3.0.jar > /godata/plugins/external/script-executor-0.3.0.jar
RUN curl --location --fail https://github.com/manojlds/gocd-docker/releases/download/0.1.27/docker-task-assembly-0.1.27.jar > /godata/plugins/external/docker-task-assembly-0.1.27.jar
RUN curl --location --fail https://github.com/ruckc/gocd-maven-plugin/releases/download/0.1.1/gocd-maven-plugin-0.1.1.jar > /godata/plugins/external/gocd-maven-plugin-0.1.1.jar
