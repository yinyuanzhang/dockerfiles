FROM node

WORKDIR /app

RUN npm install -g babel-eslint eslint-config-airbnb eslint-plugin-import eslint-plugin-meteor eslint-plugin-react eslint-plugin-jsx-a11y eslint-import-resolver-meteor eslint @meteorjs/eslint-config-meteor eslint-config-meteor

ONBUILD COPY . /app/

CMD eslint .
