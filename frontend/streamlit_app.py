import streamlit as st
from shared.db import Job
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)

def get_all_jobs():
    session = Session()
    jobs = session.query(Job).all()
    session.close()
    return jobs


st.title("Job Listings Aggregator")
st.write("Browse scraped job listings")

jobs = get_all_jobs()
search = st.text_input("Search jobs by title or company")

if search:
    filtered_jobs = [job for job in jobs if search.lower() in job.title.lower() or search.lower() in job.company.lower()]

    if filtered_jobs:
        for job in filtered_jobs:
            st.subheader(job.title)
            st.text(f"{job.company} | {job.location} | {job.created_at.date()} | Source: {job.source}")
            st.markdown(f"[Apply Here]({job.link})")
            st.markdown("---")
    else:
        st.warning("No jobs found matching your search.")
else:
    st.info("Enter a job title or company to search.")
