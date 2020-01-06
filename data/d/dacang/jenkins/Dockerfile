FROM jenkins/jenkins:lts

# Distributed Builds plugins
RUN /usr/local/bin/install-plugins.sh ssh-slaves && \


# Artifacts
/usr/local/bin/install-plugins.sh htmlpublisher && \

# UI
/usr/local/bin/install-plugins.sh greenballs && \
/usr/local/bin/install-plugins.sh simple-theme-plugin && \

# Scaling
/usr/local/bin/install-plugins.sh kubernetes && \

# Development
/usr/local/bin/install-plugins.sh bitbucket && \
/usr/local/bin/install-plugins.sh bitbucket-approve && \
/usr/local/bin/install-plugins.sh bitbucket-build-status-notifier && \
/usr/local/bin/install-plugins.sh bitbucket-pullrequest-builder && \

/usr/local/bin/install-plugins.sh jira && \
/usr/local/bin/install-plugins.sh jenkins-jira-issue-updater && \

/usr/local/bin/install-plugins.sh php && \
/usr/local/bin/install-plugins.sh slack && \

/usr/local/bin/install-plugins.sh git && \
/usr/local/bin/install-plugins.sh git-changelog && \
/usr/local/bin/install-plugins.sh git-parameter && \

/usr/local/bin/install-plugins.sh build-with-parameters && \
/usr/local/bin/install-plugins.sh envinject && \
/usr/local/bin/install-plugins.sh generic-webhook-trigger && \

# Authentication
/usr/local/bin/install-plugins.sh bitbucket-oauth && \
/usr/local/bin/install-plugins.sh role-strategy