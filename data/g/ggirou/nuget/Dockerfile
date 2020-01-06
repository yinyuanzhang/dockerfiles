FROM mono

RUN mozroots --import --sync \
  && nuget update -self \
  && rm -rf /root/.config /root/.local /tmp/*
