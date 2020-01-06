FROM elixir:1.8-alpine

# Install packages:
# - bash (obviously)
# - inotify-tools to escape warnings
# - git (for dependencies possibly)
# - nodejs (for possible JS deps)
RUN apk add --no-cache inotify-tools bash git nodejs

# Create an application dir/mountpoint
ENV APP_HOME="/app"
RUN mkdir -p $APP_HOME
WORKDIR $APP_HOME

# Add a user for development purposes
# Important: keep it after other operations with files, otherwise
# an access error may happen, like this:
#   mkdir: cannot create directory ‘/app’: Permission denied
ARG APP_USER_ID=1000
RUN adduser -D -u "${APP_USER_ID}" -s "/bin/bash" user
USER user

RUN mix local.hex --force \
  && mix archive.install --force hex phx_new

# Set up prompt to signal more clearly what does shell belong to
ARG PS1="[phoenix-new] \u@\h:\w\n$ "
ENV PS1 "${PS1}"

# Make sure bash runs by default, not an app
CMD /bin/bash
