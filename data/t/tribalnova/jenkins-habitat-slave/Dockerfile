FROM jenkins/jnlp-slave
LABEL maintainer="dominique.rochefort@hmhco.com"

USER root

# Silence some warnings while building the docker image
ENV DEBIAN_FRONTEND noninteractive

# Remove Warning: apt-key output should not be parsed (stdout is not a terminal)
# Ref: https://stackoverflow.com/questions/48162574/how-to-circumvent-apt-key-output-should-not-be-parsed
ENV APT_KEY_DONT_WARN_ON_DANGEROUS_USAGE=1

RUN echo "deb http://archive.debian.org/debian jessie non-free" >> /etc/apt/sources.list && \
        echo "deb [check-valid-until=no] http://archive.debian.org/debian jessie-backports main" >> /etc/apt/sources.list && \
        apt-get update && \
        apt-get install -y \
        apt-utils jq ffmpeg zip dnsutils \
        python-setuptools \
        python-dev build-essential \
        software-properties-common groff

# install sox with mp3 support
RUN apt-get install libsox-fmt-mp3 sox -y

# Install text-to-speech software
RUN apt-get install libttspico0 libttspico-utils libttspico-data -y

# Install Ruby and Sass
RUN apt-get install -y ruby ruby-dev && \
        gem install sass 

# Install Python PIP
RUN easy_install pip && pip install awscli


# Install Node 8
ENV NPM_CONFIG_PREFIX="/home/jenkins/.npm"

RUN mkdir -p /home/jenkins/.npm && \
        curl -sL https://deb.nodesource.com/setup_10.x | bash - && \
        apt-get install -y nodejs && \
        chown jenkins -R /home/jenkins

# Install yarn: https://yarnpkg.com/lang/en/docs/install/#linux-tab
RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add - && \
        echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee /etc/apt/sources.list.d/yarn.list && \ 
        apt-get update && \
        apt-get install -y yarn

ADD init-credentials.sh /usr/bin/init-credentials.sh
RUN chmod a+x /usr/bin/init-credentials.sh

# Install chrome browser
RUN curl -sL https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - && \
    echo 'deb http://dl.google.com/linux/chrome/deb/ stable main' >> /etc/apt/sources.list.d/google.list && \
    apt-get update && \
    apt-get install -y google-chrome-stable

# Add flag to the chrome executable so it runs with headless mode by default
RUN CHROME_FILE=`whereis -b google-chrome | awk '{print $2}'` && \
    cp $CHROME_FILE "$CHROME_FILE".old && \
    cat "$CHROME_FILE".old | sed 's/exec -a "$0" "$HERE\/chrome" "$@"/exec -a "$0" "$HERE\/chrome" "$@" --no-default-browser-check --headless --no-sandbox --user-data-dir/' > $CHROME_FILE && \
    rm "$CHROME_FILE".old

# Install Bedrock Root Certificate
ADD bedrock-ca.pem bedrock-ca.pem
RUN install bedrock-ca.pem /usr/local/share/ca-certificates/bedrock-ca.crt && \
        update-ca-certificates

USER jenkins

# Install Node packages
RUN npm i -g npm@latest
RUN npm i bower grunt-cli gulp-cli -g

# EXPLIB-1268 - bower-artifactory integration
# RUN npm i -g bower-art-resolver

# Install chrome-driver
RUN npm install -g chromedriver

ENV PATH="/home/jenkins/.npm/bin:$PATH"  

# Add bitbucket and Github to the known hosts
RUN mkdir -p /home/jenkins/.ssh && \
        ssh-keyscan -H bitbucket.org >> /home/jenkins/.ssh/known_hosts && \
        ssh-keyscan -H github.com >> /home/jenkins/.ssh/known_hosts

# Add access to @hmh private npm registry
RUN npm config set @hmh:registry http://npm.tribalnova.com

# Create the SVN directory to hold SVN credentials
RUN mkdir -p /home/jenkins/.subversion/auth/svn.simple     

# Create an error notification token to handle fatal errors
# Ref: https://jira.hmhco.com/browse/HACO-352
RUN touch error-notification.token

# Launch as Jenkins slave with proper arguments
ENTRYPOINT ["jenkins-slave"]
