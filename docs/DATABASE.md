
# Database Setup for Development Environment

This document outlines the steps required to configure the roles, users, and permissions needed for the development database (`dbd_randomizer_db_dev`).

## Prerequisites

1. PostgreSQL installed and running.
2. Access to the PostgreSQL `psql` command-line tool or equivalent database management tool.
3. Sufficient privileges to create roles, users, and databases.

---

## Steps to Configure the Development Database

### 1. Connect to PostgreSQL as a Superuser
Use the following command to connect to PostgreSQL as a superuser (e.g., `postgres`):
```bash
psql -U postgres
```

---

### 2. Create the Development Role and User

#### Create the Role
```sql
CREATE ROLE dev_user WITH LOGIN PASSWORD 'dev_password';
```

#### Grant Privileges
Allow the role to create databases:
```sql
ALTER ROLE dev_user CREATEDB;
```

---

### 3. Create the Development Database

Create the development database and assign ownership to the `dev_user` role:
```sql
CREATE DATABASE dbd_randomizer_db_dev OWNER dev_user;
```

---

### 4. Verify Permissions

Check that the `dev_user` role has the correct privileges:
```sql
\c dbd_randomizer_db_dev
\du
```

---

### 2. Create the Test Environment Role and User

#### Create the Role
```sql
CREATE ROLE test_user WITH LOGIN PASSWORD 'test_password';
```

#### Grant Privileges
Allow the role to create databases:
```sql
ALTER ROLE test_user CREATEDB;
```

---

### 3. Create the Test Database

Create the test database and assign ownership to the `test_user` role:
```sql
CREATE DATABASE dbd_randomizer_db_test OWNER test_user;
```

---

### 4. Verify Permissions

Check that the `test_user` role has the correct privileges:
```sql
\c dbd_randomizer_db_test
\du
```
---

## Notes

- **Default Roles and User**:
- - Development
  - - Role: `dev_user`
  - - Password: `dev_password`
  - - Database: `dbd_randomizer_db_dev`
- - Test
- - - Role: `test_user`
- - - Password: `test_pazssword`
- - - Database: `dbd_randomizer_db_test`

- **Database Host**: `localhost`
- **Port**: `5432`

- These values are defined in the `settings_dev.py`, `settings_test.py`, and `settings_prod.py` files. Update the corresponding file if changes are made to the database configuration.

- **Security**:
  - Do not use the development credentials in production.
  - Do not use the test credentials in production

---

## Additional Commands

### Drop the Database (if needed)
```sql
DROP DATABASE IF EXISTS dbd_randomizer_db_dev;
```

### Drop the Role (if needed)
```sql
DROP ROLE IF EXISTS dev_user;
```

### Recreate the Database and Role
Repeat steps 2 and 3 if you need to recreate the database or role.

---

## Troubleshooting

- **Permission Denied**: Ensure the `dev_user` role has the `CREATEDB` privilege.
- **Connection Issues**: Verify that PostgreSQL is running and the `DATABASE_HOST` and `DATABASE_PORT` in `settings_dev.py` match your local setup.

---

Following these steps will ensure that the development and test databases is correctly configured and ready for use.
