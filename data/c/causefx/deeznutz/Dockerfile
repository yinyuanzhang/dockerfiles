FROM mkenney/npm:debian
MAINTAINER xfesuac

# Expose port
EXPOSE 1730

COPY / /deezNutz

# Finish
WORKDIR /deezNutz
RUN ["npm", "install"]
RUN ["npm", "run", "dist:linux"]
WORKDIR /deezNutz/app
CMD ["node", "app.js"]
VOLUME ["/downloads"]