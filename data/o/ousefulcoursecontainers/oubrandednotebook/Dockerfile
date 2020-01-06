FROM jupyter/base-notebook

#Copy required files over
COPY jupyter_custom_files/ jupyter_custom_files/

USER root
RUN chmod u+x jupyter_custom_files/jupyter_styling.sh
RUN jupyter_custom_files/jupyter_styling.sh
RUN pip install --no-cache jupyter_contrib_nbextensions && jupyter contrib nbextension install --system

#Tidy up
RUN rm -rf jupyter_custom_files

#Ensure notebook user owns their files
RUN chown -R jovyan:users /home/$NB_USER/

#Reset notebook user
USER $NB_UID
