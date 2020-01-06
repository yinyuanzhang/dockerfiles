FROM ruby:2.5.3
RUN apt-get update && apt-get install -y build-essential cmake

# note that we need updated onceover and puppet-strings based on Gemfile for
# real usage to score versions from git pending a couple of tickets being fixed -
# this will do for now
RUN gem install blockenspiel --version 0.5.0 && \
  gem install bundler --version 1.16.6 && \
  gem install coderay --version 1.1.2 && \
  gem install colored --version 1.2 && \
  gem install cri --version 2.15.2 && \
  gem install deep_merge --version 1.2.1 && \
  gem install diff-lcs --version 1.3 && \
  gem install facter --version 2.5.1 && \
  gem install faraday --version 0.13.1 && \
  gem install faraday_middleware --version 0.12.2 && \
  gem install fast_gettext --version 1.1.2 && \
  gem install gettext --version 3.2.9 && \
  gem install gettext-setup --version 0.30 && \
  gem install git --version 1.3.0 && \
  gem install hiera --version 3.4.5 && \
  gem install json --version 2.1.0 && \
  gem install little-plugger --version 1.1.4 && \
  gem install locale --version 2.1.2 && \
  gem install log4r --version 1.1.10 && \
  gem install logging --version 2.2.2 && \
  gem install metaclass --version 0.0.4 && \
  gem install method_source --version 0.9.0 && \
  gem install minitar --version 0.6.1 && \
  gem install mocha --version 1.7.0 && \
  gem install multi_json --version 1.13.1 && \
  gem install multipart-post --version 2.0.0 && \
  gem install onceover-codequality --version 0.3.0 && \
  gem install parallel --version 1.12.1 && \
  gem install parallel_tests --version 2.23.0 && \
  gem install pry --version 0.11.3 && \
  gem install puppet --version 5.5.6 && \
  gem install puppet-lint --version 2.3.6 && \
  gem install puppet-strings --version 2.1.0 && \
  gem install puppet-syntax --version 2.4.1 && \
  gem install puppet_forge --version 2.2.9 && \
  gem install puppetlabs_spec_helper --version 2.11.0 && \
  gem install r10k --version 3.0.3 && \
  gem install rake --version 12.3.1 && \
  gem install rgen --version 0.8.2 && \
  gem install rspec --version 3.8.0 && \
  gem install rspec-core --version 3.8.0 && \
  gem install rspec-expectations --version 3.8.2 && \
  gem install rspec-mocks --version 3.8.0 && \
  gem install rspec-puppet --version 2.7.1 && \
  gem install rspec-puppet-utils --version 3.4.0 && \
  gem install rspec-support --version 3.8.0 && \
  gem install rspec_junit_formatter --version 0.4.1 && \
  gem install semantic_puppet --version 1.0.2 && \
  gem install strscan --version 1.0.0 && \
  gem install table_print --version 1.5.6 && \
  gem install test-unit --version 3.2.5 && \
  gem install text --version 1.3.1 && \
  gem install versionomy --version 0.5.0 && \
  gem install webrick --version 1.4.2 && \
  gem install yard --version 0.9.16 && \
  gem install zlib --version 1.0.0 && \
  gem install onceover
