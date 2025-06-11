from shared.db import init_db, save_job
from scraper.remoteok import scrape_remoteok
from scraper.jobspresso import scrape_jobspresso_jobs

def main():
    init_db()
    all_scrapers = [scrape_remoteok, scrape_jobspresso_jobs]
    for scraper in all_scrapers:
        print(f"Running scraper: {scraper.__name__}")
        jobs = scraper()
        for job in jobs[:20]:
            save_job(job)
    print("Scraping complete.")

if __name__ == "__main__":
    main()
