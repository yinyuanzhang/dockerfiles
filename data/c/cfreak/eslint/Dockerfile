FROM node:10-alpine

# Install eslint globally and the styles Standard, Google and Airbnb.
# Airbnb and Standard require some additional peer dependencies that are
# installed as well
RUN npm i -g --no-optional eslint@5.9.0 \
                           eslint-plugin-import@latest \
                           eslint-config-google@latest \
                           eslint-config-standard@latest \
                           eslint-plugin-node@latest \
                           eslint-plugin-promise@latest \
                           eslint-plugin-standard@latest \
                           eslint-config-airbnb@latest \
                           eslint-plugin-jsx-a11y@latest \
                           eslint-plugin-react@latest

CMD ["eslint"]
