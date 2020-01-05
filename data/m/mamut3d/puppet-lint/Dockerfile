FROM centos/ruby-25-centos7
USER root
RUN yum update -y && yum -y install rubygems-devel
RUN gem install puppet-lint \
  puppet-lint-trailing_newline-check \
  puppet-lint-variable_contains_upcase \
  puppet-lint-param-docs \
  puppet-lint-roles_and_profiles-check \
  puppet-lint-absolute_template_path \
  puppet-lint-strict_indent-check \
  puppet-lint-unquoted_string-check \
  puppet-lint-package_ensure-check \
  puppet-lint-resource_reference_syntax \
  puppet-lint-top_scope_facts-check \
  puppet-lint-legacy_facts-check \
  puppet-lint-concatenated_template_files-check \
  puppet-lint-duplicate_class_parameters-check \
  puppet-lint-no_cron_resources-check \
  puppet-lint-world_writable_files-check \
  puppet-lint-no_symbolic_file_modes-check \
  puppet-lint-no_erb_template-check \
  puppet-lint-no_file_path_attribute-check \
  puppet-lint-template_file_extension-check

USER default

# wait cycle
CMD ["sh", "-c", "tail -f /dev/null"]
