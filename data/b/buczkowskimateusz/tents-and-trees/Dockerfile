FROM python:3.7
COPY tents_and_trees/requirements.txt /requirements.txt
RUN pip install -r /requirements.txt
COPY tents_and_trees/ /tents_and_trees
WORKDIR /tents_and_trees
RUN useradd -m user
USER user
ENV FLASK_APP=web.py
CMD ["sh", "-c", "./entrypoint.sh"]
