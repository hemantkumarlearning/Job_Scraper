import os
from sqlalchemy import create_engine, Column, Integer, String, UniqueConstraint,DateTime
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.exc import IntegrityError
from datetime import datetime,timedelta

DATABASE_URL = os.getenv("DATABASE_URL") 

Base = declarative_base()

class Job(Base):
    __tablename__ = 'jobs'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    company = Column(String)
    location = Column(String)
    link = Column(String, unique=True)
    source = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)
    __table_args__ = (UniqueConstraint('link', name='uix_link'),)

engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)

def init_db():
    Base.metadata.create_all(engine)

def save_job(job_dict):
    session = Session()
    job = Job(**job_dict)
    try:
        session.add(job)
        session.commit()
    except IntegrityError:
        session.rollback()
    finally:
        session.close()

def get_all_jobs():
    session = Session()
    jobs = session.query(Job).all()
    session.close()
    return jobs

def delete_old_jobs():
    session = Session()
    """Delete jobs older than 3 days."""
    try:
        cutoff_time = datetime.utcnow() - timedelta(days=3)
        session.query(Job).filter(Job.created_at < cutoff_time).delete(synchronize_session=False)
        session.commit()
    finally:
        session.close()