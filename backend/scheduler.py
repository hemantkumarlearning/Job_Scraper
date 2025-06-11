from apscheduler.schedulers.blocking import BlockingScheduler
from backend.main import main  
from shared.db import delete_old_jobs
scheduler = BlockingScheduler()
from datetime import datetime

@scheduler.scheduled_job('interval', days=1,next_run_time=datetime.now())
def scheduled_job():
    
    print("[Job Scheduler] Starting daily scraping job...")
    main()
    delete_old_jobs()
    print("[Job Scheduler] Scraping completed.")

if __name__ == "__main__":
    print("[Scheduler] Daily job scheduling started. Press Ctrl+C to exit.")
    scheduler.start()