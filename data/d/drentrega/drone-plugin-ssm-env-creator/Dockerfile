FROM node:alpine

LABEL vendor="Dr.Entrega" \
      maintainer="Dr.Entrega <technology+docker@drentrega.com>" \
      image="node" \
      tag="alpine"

RUN npm install -g @dre/aws-env \
  && aws-env version

CMD ["sh", "-c", "aws-env -vp -n ${PLUGIN_NAMESPACE} -r ${PLUGIN_REGION} -o ${PLUGIN_OUTPUT}"]

# This dockerfile was auto-generated at 2019-01-10T11:38:35-02:00.

# In case of security branches, please contact technology+security@drentrega.com.