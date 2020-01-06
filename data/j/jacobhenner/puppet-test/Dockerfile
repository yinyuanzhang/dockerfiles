FROM ruby:2.4

MAINTAINER Jacob Henner <code@ventricle.us>

RUN apt-get update && apt-get install -y jq && apt-get clean 

RUN gem install puppet puppet-lint puppet-syntax rspec-puppet puppetlabs_spec_helper jsonlint yaml-lint metadata-json-lint semantic_puppet rubocop rubocop-rspec pdk puppet-strings rgen
