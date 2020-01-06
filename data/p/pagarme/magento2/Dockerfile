FROM alexcheng/magento2

ADD ./scripts /usr/local/bin/
RUN chmod +x /usr/local/bin/update
RUN chmod +x /usr/local/bin/install_pagarme

RUN composer global require behat/behat:~3.3
RUN composer global require behat/mink:^1.7
RUN composer global require behat/mink-selenium2-driver:^1.3
RUN composer global require behat/mink-extension:~2.2

ENV PATH="${COMPOSER_HOME}vendor/bin:$PATH"
