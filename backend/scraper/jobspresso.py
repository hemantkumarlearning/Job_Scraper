
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup

def scrape_jobspresso_jobs():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    url = "https://jobspresso.co/remote-jobs/"
    driver.get(url)

    try:
        # Wait until job listings container loads
        WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.CLASS_NAME, "job_listing"))
        )
    except Exception as e:
        print("Timeout waiting for jobs:", e)
        driver.quit()
        return []

    soup = BeautifulSoup(driver.page_source, "html.parser")
    driver.quit()

    jobs = []
    listings = soup.find_all("li", class_="job_listing")
    for listing in listings:
        title_tag = listing.find("h3", class_="job_listing-title")
        company_tag = listing.find("div", class_="job_listing-company")
        company = company_tag.find("strong")
        location_tag = listing.find("div", class_="job_listing-location job_listing__column")
        link_tag = listing.find("a", href=True)

        if title_tag and company and link_tag:
            jobs.append({
                "title": title_tag.text.strip(),
                "company": company.text.strip(),
                "location": location_tag.text.strip() if location_tag else "N/A",
                "link": link_tag["href"],
                "source": "Jobspresso"
            })

    return jobs


