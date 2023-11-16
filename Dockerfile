# Use the official MySQL image from Docker Hub
FROM mysql:latest

# Environment variables to configure MySQL
ENV MYSQL_ROOT_PASSWORD=password123
ENV MYSQL_DATABASE=MusicDB
# ENV MYSQL_USER=root
ENV MYSQL_PASSWORD=password123

# Copy custom SQL scripts to initialize the database if needed
COPY ./sql-scripts/ /docker-entrypoint-initdb.d/
