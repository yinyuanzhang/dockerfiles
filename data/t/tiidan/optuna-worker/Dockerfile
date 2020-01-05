FROM python:3.7.5

# envs
ENV ENV=STAGE

# create app dir
RUN mkdir /app
WORKDIR /app

# install dependencies
ADD requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# add app code
ADD . /app/

# optun envs
ENV STUDY=''
ENV STORAGE=''
ENV N_TRIALS=1000000
ENV OBJECTIVE_FILE=study/objective.py
ENV OBJECTIVE_FUNCTION=objective

# other envs
ENV N_JOBS=-1
ENV PYTHONPATH=.

# optimize study
CMD optuna study optimize --study $STUDY --storage $STORAGE --n-trials $N_TRIALS --n-jobs $N_JOBS $OBJECTIVE_FILE $OBJECTIVE_FUNCTION
