FROM jenkins/jenkins:lts
MAINTAINER mariusz@kabala.waw.pl
USER root

RUN apt-get update && \
    apt-get -y install apt-transport-https \
      ca-certificates \
      curl \
      gnupg2 \
      software-properties-common && \
    curl -fsSL https://download.docker.com/linux/$(. /etc/os-release; echo "$ID")/gpg > /tmp/dkey; apt-key add /tmp/dkey && \
    add-apt-repository \
      "deb [arch=amd64] https://download.docker.com/linux/$(. /etc/os-release; echo "$ID") \
      $(lsb_release -cs) \
      stable" && \
   apt-get update && \
   apt-get -y install docker-ce && \
   # See https://crbug.com/795759
   apt-get install -yq libgconf-2-4 && \
   # Install latest chrome dev package, which installs the necessary libs to
   # make the bundled version of Chromium that Puppeteer installs work.
   apt-get install -y wget --no-install-recommends && \
   wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - && \
   sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list' && \
   apt-get update && \
   apt-get install -y google-chrome-unstable --no-install-recommends && \
   rm -rf /var/lib/apt/lists/* && \
   wget --quiet https://raw.githubusercontent.com/vishnubob/wait-for-it/master/wait-for-it.sh -O /usr/sbin/wait-for-it.sh && \
   chmod +x /usr/sbin/wait-for-it.sh && \
   curl -L "https://github.com/docker/compose/releases/download/1.24.0/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose && \
   sudo chmod +x /usr/local/bin/docker-compose

RUN /usr/local/bin/install-plugins.sh \
    role-strategy \
    matrix-auth \
    github-oauth \
    github \
    ghprb \
    git \
    git-client \
    s3 \
    amazon-ecs \
    amazon-ecr \
    docker-workflow \
    workflow-aggregator \
    workflow-multibranch \
    job-dsl \
    ssh-slaves \
    envinject \
    docker-build-publish \
    antisamy-markup-formatter \
    multiple-scms \
    build-timeout \
    queue-cleanup \
    nodejs \
    ansicolor \
    checkstyle \
    build-name-setter \
    timestamper \
    modernstatus \
    simple-theme-plugin \
    mail-watcher-plugin \
    allure-jenkins-plugin \
    build-blocker-plugin \
    parameterized-trigger \
    conditional-buildstep \
    throttle-concurrents \
    testng-plugin \
    rebuild \
    groovy-postbuild \
    sonar \
    ws-cleanup \
    build-user-vars-plugin \
    cobertura \
    progress-bar-column-plugin \
    extra-columns \
    cucumber-reports \
    dashboard-view \
    gatling \
    github-branch-source \
    htmlpublisher \
    git-parameter \
    jackson2-api \
    metrics-graphite \
    metrics \
    ci-skip \
    mask-passwords \
    pipeline-utility-steps \
    configurationslicing \
    flow \
    jobConfigHistory \
    job-import-plugin \
    managed-scripts \
    jenkins-multijob-plugin \
    ssh \
    ssh-agent \
    claim \
    flaky-test-handler \
    junit-attachments \
    test-stability \
    pipeline-maven \
    tasks \
    postbuild-task \
    permissive-script-security \
    blueocean \
    influxdb \
    extensible-choice-parameter \
    pipeline-githubnotify-step \
    command-launcher \
    robot \
    uno-choice \
    audit-trail \
    build-with-parameters \
    workflow-remote-loader \
    clover \
    cloverphp \
    lockable-resources \
    http_request \
    pipeline-github-lib \
    hidden-parameter \
    configuration-as-code \
    configuration-as-code-support \
    ;
