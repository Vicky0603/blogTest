#!/bin/bash
set -e

psql --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" -v ON_ERROR_STOP=1 \
        -v user="$KODLAND_DB_USER" -v db="$KODLAND_DB_NAME" -v password="$KODLAND_DB_PASSWORD" <<-EOSQL
    CREATE USER :user WITH CREATEDB PASSWORD :'password';
    CREATE DATABASE :db;
    GRANT ALL PRIVILEGES ON DATABASE :db TO :user;
EOSQL
