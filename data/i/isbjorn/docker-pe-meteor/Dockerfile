FROM node:11-stretch

RUN npm install -g \
      mup@1.4.5 \
      eslint@5.15.3 \
      eslint-plugin-meteor@5.1.0 \
      eslint-plugin-jasmine@2.10.1 \
      eslint-plugin-import@^2.14.0 \
      eslint-plugin-jsx-a11y@^6.1.1 \
      eslint-plugin-react@^7.11.0 \
      eslint-plugin-import@^2.14.0 \
      eslint-config-airbnb@17.1.0 \
      babel-eslint@10.0.1 \
      eslint-import-resolver-meteor@0.4.0 \
      eslint-plugin-react@7.12.4 \
      eslint-plugin-jsx-a11y@6.2.1 \
      @meteorjs/eslint-config-meteor@1.0.5

RUN curl https://install.meteor.com/ | sh

# switch to ci/cd user
RUN groupadd -g 5000 gitlab-build && \
    useradd -m -s /bin/bash -u 5000 -g 5000 gitlab-build
USER 5000:5000
