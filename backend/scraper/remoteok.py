
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

def scrape_remoteok():

    options = Options()
    options.add_argument("--headless")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.get("https://remoteok.com/")
    time.sleep(5)
    soup = BeautifulSoup(driver.page_source, "html.parser")
    driver.quit()

    job_rows = soup.find_all("tr", class_="job")
    jobs = []
    for job in job_rows:
        title = job.find("h2").text.strip() if job.find("h2") else None
        company = job.find("h3").text.strip() if job.find("h3") else None
        location = job.find("div", class_="location")
        location = location.text.strip() if location else "Remote"
        link = "https://remoteok.com" + job.get("data-href", "")
        if title and company and link:
            jobs.append({
                "title": title,
                "company": company,
                "location": location,
                "link": link,
                "source": "RemoteOK"
            })
    return jobs
