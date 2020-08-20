# Use the official lightweight Python image.
# https://hub.docker.com/_/python
FROM python:3.8-slim

# Optionally, install some typical packages used for building and network debugging.
RUN apt-get update

# Update to the latest PIP
RUN pip3 install --upgrade pip

# Our application code will exist in the /app directory,
# so set the current working directory to that
ENV APP_HOME /app
WORKDIR $APP_HOME


# Copy our files into the current working directory WORKDIR
COPY ./ ./

# install our dependencies
RUN  pip3 install -r requirements.txt

# Make /app/* available to be imported by Python globally to better support several
# use cases like Alembic migrations.
ENV PYTHONPATH=/app


# Run the web service on container startup. Here we use the gunicorn
# webserver, with one worker process and 8 threads.
# For environments with multiple CPU cores, increase the number of workers
# to be equal to the cores available.
CMD gunicorn --chdir app --bind :$PORT --workers 1 --threads 8 --timeout 0 main:app
