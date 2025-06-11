# Web Scraping Dashboard – Job Listings Aggregator

A Python-based job listings aggregator that scrapes data from multiple dynamic job boards and presents it in a Streamlit dashboard with filtering and search functionality.

## Features

-  Scrapes job titles, companies, locations, and application links using **Selenium** and **BeautifulSoup**
-  Stores structured data in a **PostgreSQL** database
-  Displays jobs in a **Streamlit dashboard** with keyword filtering
-  Fully **Dockerized** with support for local development and testing via `docker-compose`

---


## Tech Stack

- **Python 3.11**
- **Selenium** & **BeautifulSoup** for scraping
- **PostgreSQL** for data storage
- **Streamlit** for UI/dashboard
- **Docker** & **Docker Compose** for containerized setup

---

##  Installation

###  Requirements

- Docker & Docker Compose installed
- (Optional) Python 3.11+ and PostgreSQL (if running locally without Docker)
