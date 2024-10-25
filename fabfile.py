from fabric import task


# Task to activate virtual environment
@task
def activate(c):
    c.run('make activate')

@task(activate)
def test(c):
    c.run('export DJANGO_ENV=test && pytest')

@task(activate)
def install(c):
    # Check for virtual environment and install dependencies
    c.run('make install')

@task
def migrate(c):
    c.run('export DJANGO_ENV=development && python manage.py migrate')

@task
def build(c):
    # Build the Docker image
    c.run('docker-compose -f docker-compose.override.yml build')


@task
def stop(c):

    env = c.run('echo $DJANGO_ENV', hide=True).stdout.strip()

    if env == 'dev':
        # Stop the local development server (non-containerized)
        print("Stopping local development server...")
        c.run('pkill -f "python manage.py runserver"')
    elif env == 'production':
        # Stop the production Docker containers
        print("Stopping production Docker containers...")
        c.run('docker-compose -f docker-compose.yml -f docker-compose.prod.yml down')
    else:
        # Stop the Dockerized development environment
        print("Stopping Dockerized development environment...")
        c.run('docker-compose --env-file .env.dev -f docker-compose.yml -f docker-compose.override.yml down')


@task
def migrate_prod(c):
    # Run migrations in the production Docker environment
    c.run('docker-compose -f docker-compose.override.yml run web python manage.py migrate')

@task(activate, migrate)
def dev(c):
    c.run('export DJANGO_ENV=development && python manage.py runserver')

@task()
def devcontainer(c):
    env_file = ".env.dev"
    c.run(f'docker-compose --env-file {env_file} -f docker-compose.yml -f docker-compose.override.yml up --build')

@task
def prod(c):
    env_file = ".env.dev"
    c.run('docker-compose --env-file {env_file} -f docker-compose.prod.yml up -d')



