from fabric import task
import os

# Task to activate virtual environment
@task
def activate(c):
    c.run('make activate')

# Setup the Django environment
def load_django_settings(environment):
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "dbd_randomizer_service.settings")
    import django
    django.setup()
    from django.conf import settings
    return settings

# Helper function to get database settings from environment


@task(activate)
def test(c):
    # Run tests
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
    c.run(f'docker-compose --env-file {env_file} -f docker-compose.prod.yml up -d')


@task
def rebuild_db(c):
    # Check environment
    env = c.run('echo $DJANGO_ENV', hide=True).stdout.strip() or 'development'
    if env == "production":
        print("ERROR: Rebuilding the database in production is not allowed!")
        return
    # Load Django settings
    settings = load_django_settings(environment=env)

    # Get database settings
    db_name = settings.DATABASE_NAME
    db_user = settings.DATABASE_USER
    db_password = settings.DATABASE_PASSWORD
    db_host = settings.DATABASE_HOST
    db_port = settings.DATABASE_PORT

    print(f"Dropping and recreating development database: {db_name}")

    # Use 'postgres' as the default database when connecting
    default_db = "postgres"

    # Drop and recreate the database
    c.run(
        f'psql -h {db_host} -U {db_user} -p {db_port} -d {default_db} -c "DROP DATABASE IF EXISTS {db_name};"',
        warn=True,
    )
    c.run(
        f'psql -h {db_host} -U {db_user} -p {db_port} -d {default_db} -c "CREATE DATABASE {db_name};"',
        warn=True,
    )

    # Run migrations
    c.run('export DJANGO_ENV=development && python manage.py migrate')