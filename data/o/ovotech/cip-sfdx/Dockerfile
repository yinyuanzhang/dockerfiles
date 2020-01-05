FROM circleci/openjdk:latest-node-browsers

ENV SFDX_AUTOUPDATE_DISABLE=true

RUN sudo npm install --global \
    @salesforce/eslint-config-lwc@0.4.0 \
    @salesforce/eslint-plugin-aura@1.2.0 \
    eslint@5.16.0 \
    lint-staged@9.3.0 \
    prettier@1.18 \
    sfdx-cli@7.15.3 \
    selenium-standalone@6.16.0

RUN PMD_URL="https://github.com/pmd/pmd/releases/download/pmd_releases/6.11.0/pmd-bin-6.11.0.zip" \
    && curl --silent --show-error --location --fail --output /tmp/pmd-bin-6.11.0.zip $PMD_URL \
    && sudo unzip /tmp/pmd-bin-6.11.0.zip -d /tmp \
    && sudo mv /tmp/pmd-bin-6.11.0 /usr/local/lib \
    && rm -rf /tmp/pmd-bin-6.11.0.zip /tmp/pmd-bin-6.11.0 \
    && sudo sh -c 'printf "#!/bin/sh\n/usr/local/lib/pmd-bin-6.11.0/bin/run.sh pmd \"\$@\"\n" > /usr/local/bin/pmd' \
    && sudo chmod +x /usr/local/bin/pmd