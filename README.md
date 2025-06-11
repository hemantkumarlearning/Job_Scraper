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

### Run Manually (Without Docker)

#### 1. Clone the repository

```
git clone https://github.com/hemantkumarlearning/Job_Scraper.git
cd Job_Scraper
```

#### 2. Create a virtual environment

```
python -m venv venv
venv\Scripts\activate

```

#### 3. Set the database URL (env variable)

```
DATABASE_URL=postgresql://user:password@localhost:5432/jobsdb
```

#### 3. Go to backend folder and install dependencies

```
cd backend
pip install -r requirements.txt
```

#### 4. Run the scraper

```
python scheduler.py
```
This will scrape job listings and insert them into your PostgreSQL database and run every 24 hrs

#### 3. Go to frontend folder and install dependencies

```
cd .
cd frontend
pip install -r requirements.txt
```

#### 5. Run the Streamlit dashboard

```
streamlit run streamlit_app.py
```

