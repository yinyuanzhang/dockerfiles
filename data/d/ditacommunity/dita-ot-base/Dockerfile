FROM ditaot/dita-ot-base
#
# Sets up a DITA-OT container
# with all of the DITA Community 
# open toolkit plugins integrated.
USER dita-ot
WORKDIR ${DITA_HOME}
ENV DITA_COMM_URL=https://github.com/dita-community/ BRANCH=master
#
# Common XSLT
#
RUN wget ${DITA_COMM_URL}org.dita-community.common.xslt/archive/${BRANCH}.zip && unzip ${BRANCH}.zip -d plugins && rm ${BRANCH}.zip
RUN wget ${DITA_COMM_URL}org.dita-community.common.mapdriven/archive/${BRANCH}.zip && unzip ${BRANCH}.zip -d plugins && rm ${BRANCH}.zip
#
# PDF Flagging:
# NOTE: This plugin requires a flagging preprocess extension that doesn't exist in the 1.8.5 or earlier OTs.
# RUN wget ${DITA_COMM_URL}org.dita-community.pdf.flagging/archive/${BRANCH}.zip && unzip ${BRANCH}.zip -d plugins && rm ${BRANCH}.zip
#
# PDF extensions
#
RUN wget ${DITA_COMM_URL}org.dita-community.pdf-page-break/archive/${BRANCH}.zip && unzip ${BRANCH}.zip -d plugins && rm ${BRANCH}.zip
RUN wget ${DITA_COMM_URL}org.dita-community.pdf-dl-as-dl/archive/${BRANCH}.zip && unzip ${BRANCH}.zip -d plugins && rm ${BRANCH}.zip
#
# Preprocessing extensions: (Not yet working with OT 2.2.2)
#
#RUN wget ${DITA_COMM_URL}org.dita-community.adjust-copy-to/archive/${BRANCH}.zip && unzip ${BRANCH}.zip -d plugins && rm ${BRANCH}.zip
#RUN wget ${DITA_COMM_URL}org.dita-community.xhtml-adjct/archive/${BRANCH}.zip && unzip ${BRANCH}.zip -d plugins && rm ${BRANCH}.zip
#RUN wget ${DITA_COMM_URL}org.dita-community.preprocess-extensions/archive/${BRANCH}.zip && unzip ${BRANCH}.zip -d plugins && rm ${BRANCH}.zip
#
# Preprocess tester:
#
# RUN wget ${DITA_COMM_URL}org.dita-community.preprocess-tester/archive/${BRANCH}.zip && unzip ${BRANCH}.zip -d plugins && rm ${BRANCH}.zip
#
# DITA Community doctypes
#
RUN wget ${DITA_COMM_URL}org.dita-community.doctypes/archive/${BRANCH}.zip && unzip ${BRANCH}.zip -d plugins && rm ${BRANCH}.zip
#
# DITA Community Q/A plugin
#
RUN wget ${DITA_COMM_URL}org.dita-community.qa/archive/${BRANCH}.zip && unzip ${BRANCH}.zip -d plugins && rm ${BRANCH}.zip
#
# Ruby domain:
#
RUN wget ${DITA_COMM_URL}org.dita-community.ruby-d.doctypes/archive/${BRANCH}.zip && unzip ${BRANCH}.zip -d ${DITA_HOME}/plugins && rm ${BRANCH}.zip
RUN wget ${DITA_COMM_URL}org.dita-community.ruby-d.fo/archive/${BRANCH}.zip && unzip ${BRANCH}.zip -d ${DITA_HOME}/plugins && rm ${BRANCH}.zip 
RUN wget ${DITA_COMM_URL}org.dita-community.ruby-d.html/archive/${BRANCH}.zip && unzip ${BRANCH}.zip -d ${DITA_HOME}/plugins && rm ${BRANCH}.zip
#
# Media domain:
#
RUN wget ${DITA_COMM_URL}org.dita-community.media-d.doctypes/archive/${BRANCH}.zip && unzip ${BRANCH}.zip -d ${DITA_HOME}/plugins && rm ${BRANCH}.zip
RUN wget ${DITA_COMM_URL}org.dita-community.media-d.html/archive/${BRANCH}.zip && unzip ${BRANCH}.zip -d ${DITA_HOME}/plugins && rm ${BRANCH}.zip
#
# Integrate new plugins
#
RUN ant -f integrator.xml
#
# End of Dockerfile
#

