FROM circleci/php:5.6.40

# GitHubのPull Requestにコメントをするために必要なgemのインストール
RUN sudo apt update && sudo apt install ruby-full
RUN sudo gem install --no-document checkstyle_filter-git saddler saddler-reporter-github

# コードシンタックスチェック用のライブラリをインストール
RUN composer global require squizlabs/php_codesniffer:2.9.* --dev
RUN composer global require eviweb/fuelphp-phpcs:~1 --dev
ARG COMPOSER_HOME=/home/circleci/.composer
ENV PATH $PATH:$COMPOSER_HOME/vendor/bin
RUN echo $PATH
RUN phpcs --config-set installed_paths $COMPOSER_HOME/vendor/eviweb/fuelphp-phpcs/Standards

# MemoryLimit設定
RUN sudo sh -c "echo \"memory_limit = 4G\" > /usr/local/etc/php/conf.d/memory.ini"