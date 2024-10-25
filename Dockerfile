# base image
FROM python:3.9

# setup environment variable
ENV DockerHOME=/workspace/dbd_randomizer_service \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# set work directory
RUN mkdir -p $DockerHOME

# where your code lives
WORKDIR $DockerHOME

# install dependencies
RUN pip install --upgrade pip

# copy whole project to your docker home directory.
COPY . $DockerHOME

# run this command to install all dependencies
RUN pip install -r requirements.txt

# port where the Django app runs
EXPOSE 8000
# Make both scripts executable
RUN chmod +x start.sh start_prod.sh

# Switch between scripts based on DJANGO_ENV
ENTRYPOINT ["sh", "-c", "if [ \"$DJANGO_ENV\" = 'production' ]; then ./start_prod.sh; else ./start.sh; fi"]