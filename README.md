
# dbd_randomizer_service

This project is the backend API server for the [lupogreybeard-ui](https://www.lupogreybeard.com/dbd/) and the dbd randomizer [mobile app](https://github.com/CryptoRAT/dbdrandomizer). It is written in Python, using the Django framework. It is backed by a postgres database.

---

## Build, Test, and Run Lifecycle Operations

This section outlines the typical workflow for building, testing, and running the Django application using Fabric commands. Each step corresponds to a Fabric task and ensures a smooth lifecycle management process.

---

### 1. **Setup and Initialization**

#### Activate Virtual Environment
Before running any other tasks, ensure that the virtual environment is activated:
```bash
fab activate
```

#### Install Dependencies
Install the required Python dependencies:
```bash
fab install
```

#### Initialize the Database
Development uses a local database. Check out the instructions in [database docs](docs/DATABASE.md) to learn how to set this up.

Then run migrations:
```bash
fab migrate
```

If you need to rebuild the database, you can use:
```bash
fab rebuild-db --env=development
```

This will drop and recreate the database for the specified environment (default is `development`, other option is `test`).

---

### 2. **Build the Application**

#### Build Docker Images
To build the Docker images for your application:
```bash
fab build
```

---

### 3. **Development Environment**

#### Run Development Server (Non-Dockerized)
Run the Django development server locally:
```bash
fab dev
```

#### Run Development Environment with Docker
Run the Dockerized development environment:
```bash
fab devcontainer
```

---

### 4. **Testing**

#### Run Tests
Run all tests in the project. This will set the `DJANGO_ENV` to `test` and execute `pytest`:
```bash
fab test
```

To rebuild the test database before running tests:
```bash
fab rebuild-db --env=test
```

---

### 5. **Production Environment**

#### Run Production Environment
Deploy and run the production environment with Docker:
```bash
fab prod
```

#### Apply Migrations in Production
Run database migrations inside the production Docker container:
```bash
fab migrate_prod
```

---

### 6. **Stopping the Application**

#### Stop All Environments
This command detects the current environment (`dev`, `production`, or Dockerized development) and stops the appropriate services:
```bash
fab stop
```

---

### Typical Workflow

Here’s a suggested order for running the lifecycle tasks:

1. **Setup and Initialization**:
   - `fab activate`
   - `fab install`
   - `fab migrate`

2. **Build**:
   - `fab build`

3. **Development**:
   - Non-Dockerized: `fab dev`
   - Dockerized: `fab devcontainer`

4. **Test**:
   - Run Tests: `fab test`
   - Rebuild Test Database: `fab rebuild-db --env=test`

5. **Production**:
   - Deploy: `fab prod`
   - Apply Migrations: `fab migrate_prod`

6. **Stop**:
   - `fab stop`

---

## Deployment
This project is autodeployed to a DigitalOcean app when a merge is made to `main`. This is accomplished using GitHub actions and tools provided by DigitalOcean.

---

## TODOs
You can see a list of things I would like to add to this site here: [wish list](./WISHLIST.md)
