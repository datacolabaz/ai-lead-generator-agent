# # import requests
# # import re
# # import pandas as pd
# # from bs4 import BeautifulSoup
# # from urllib.parse import urljoin

# # websites = [
# #     "https://adzone.az",
# #     "https://sharafmedia.com",
# #     "https://digitalagency.az",
# #     "https://facemark.az",
# #     "https://crocusoft.com",
# #     "https://okmedia.az",
# #     "https://pronet.az",
# #     "https://smartbee.az",
# #     "https://allstars.az",
# #     "https://bakuwebstudio.az",
# #     "https://webcoder.az",
# #     "https://code.edu.az",
# #     "https://maxgraph.az",
# #     "https://pixel.az",
# #     "https://morpho.az"
# # ]

# # email_pattern = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"
# # phone_pattern = r"\+994[\s\-]?\d{2}[\s\-]?\d{3}[\s\-]?\d{2}[\s\-]?\d{2}"

# # results = []

# # for site in websites:

# #     email_found = "Not found"

# #     try:
# #         response = requests.get(site, headers={"User-Agent": "Mozilla/5.0"}, timeout=8)

# #         soup = BeautifulSoup(response.text, "html.parser")

# #         # 1️⃣ homepage email check
# #         emails = re.findall(email_pattern, response.text)
# #         phones = re.findall(phone_pattern, response.text)
# #         phone = phones[0] if phones else "Not found"

# #         if emails:
# #             email_found = emails[0]

# #         else:

# #             # 2️⃣ mailto link check
# #             mailto_links = soup.select('a[href^=mailto]')

# #             if mailto_links:
# #                 email_found = mailto_links[0]["href"].replace("mailto:", "")
            
# #             else:

# #         # footer email check
# #              footer = soup.find("footer")

# #             if footer:
# #                   emails = re.findall(email_pattern, footer.text)
# #                   if emails:
# #                      email_found = emails[0]
# #             else:

# #                 # 3️⃣ contact page check
# #                 for link in soup.find_all("a", href=True):

# #                     href = link["href"].lower()

# #                     if "contact" in href:

# #                         contact_url = urljoin(site, href)

# #                         try:
# #                             contact_page = requests.get(
# #                                 contact_url,
# #                                 headers={"User-Agent": "Mozilla/5.0"},
# #                                 timeout=8
# #                             )

# #                             emails = re.findall(email_pattern, contact_page.text)

# #                             if emails:
# #                                 email_found = emails[0]
# #                                 break

# #                         except:
# #                             pass

# #     except:
# #         pass

# #     results.append({
# #         "Website": site,
# #         "Email": email_found,
# #         "Phone": phone
# #     })

# # df = pd.DataFrame(results)

# # df.to_excel("leads.xlsx", index=False)

# # print(df)

# import googlemaps
# import pandas as pd
# import requests
# import re
# from bs4 import BeautifulSoup

# API_KEY = "BURAYA_API_KEY"

# gmaps = googlemaps.Client(key=API_KEY)

# query = "marketing agencies in Baku"

# places = gmaps.places(query=query)

# results = []

# email_pattern = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"
# phone_pattern = r"\+994[\s\-]?\d{2}[\s\-]?\d{3}[\s\-]?\d{2}[\s\-]?\d{2}"

# for place in places["results"]:

#     name = place.get("name")
#     website = None
#     email = "Not found"
#     phone = "Not found"

#     place_id = place["place_id"]

#     details = gmaps.place(place_id=place_id)

#     result = details["result"]

#     if "website" in result:
#         website = result["website"]

#         try:
#             response = requests.get(
#                 website,
#                 headers={"User-Agent":"Mozilla/5.0"},
#                 timeout=8
#             )

#             emails = re.findall(email_pattern,response.text)

#             if emails:
#                 email = emails[0]

#             phones = re.findall(phone_pattern,response.text)

#             if phones:
#                 phone = phones[0]

#         except:
#             pass

#     results.append({
#         "Company": name,
#         "Website": website,
#         "Email": email,
#         "Phone": phone
#     })

# df = pd.DataFrame(results)

# df.to_excel("google_maps_leads.xlsx",index=False)

# print(df)






# import requests
# import pandas as pd
# import re
# from bs4 import BeautifulSoup

# queries = [
#     "marketing agency Baku",
#     "digital marketing Baku",
#     "reklam agentliyi Bakı"
# ]

# headers = {"User-Agent": "Mozilla/5.0"}

# email_pattern = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"
# phone_pattern = r"\+994[\s\-]?\d{2}[\s\-]?\d{3}[\s\-]?\d{2}[\s\-]?\d{2}"

# results = []

# for query in queries:

#     print("Searching:", query)

#     url = "https://html.duckduckgo.com/html/"
#     data = {"q": query}

#     response = requests.post(url, data=data, headers=headers)

#     soup = BeautifulSoup(response.text, "html.parser")

#     for a in soup.select("a.result__a"):

#         website = a.get("href")

#         email = "Not found"
#         phone = "Not found"

#         try:
#             page = requests.get(website, headers=headers, timeout=8)

#             emails = re.findall(email_pattern, page.text)
#             phones = re.findall(phone_pattern, page.text)

#             if emails:
#                 email = emails[0]

#             if phones:
#                 phone = phones[0]

#         except:
#             pass

#         results.append({
#             "Website": website,
#             "Email": email,
#             "Phone": phone
#         })

# df = pd.DataFrame(results).drop_duplicates()

# df.to_excel("lead_generator.xlsx", index=False)

# print(df)





# import requests
# import pandas as pd
# import re
# from bs4 import BeautifulSoup

# queries = [
#     "marketing agency Baku",
#     "digital marketing Baku",
#     "reklam agentliyi Bakı"
# ]

# headers = {"User-Agent": "Mozilla/5.0"}

# email_pattern = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"
# phone_pattern = r"\+994[\s\-]?\d{2}[\s\-]?\d{3}[\s\-]?\d{2}[\s\-]?\d{2}"

# # spam saytlar
# blocked_domains = [
#     "youtube",
#     "reddit",
#     "tripadvisor",
#     "facebook",
#     "instagram",
#     "linkedin",
#     "wikipedia"
# ]

# results = []

# for query in queries:

#     print("Searching:", query)

#     url = "https://html.duckduckgo.com/html/"
#     data = {"q": query}

#     response = requests.post(url, data=data, headers=headers)

#     soup = BeautifulSoup(response.text, "html.parser")

#     for a in soup.select("a.result__a"):

#         website = a.get("href")

#         if not website.startswith("http"):
#             continue

#         # spam filter
#         if any(domain in website for domain in blocked_domains):
#             continue

#         email = "Not found"
#         phone = "Not found"

#         try:
#             page = requests.get(website, headers=headers, timeout=8)

#             emails = re.findall(email_pattern, page.text)
#             phones = re.findall(phone_pattern, page.text)

#             if emails:
#                 email = emails[0]

#             if phones:
#                 phone = phones[0]

#         except:
#             pass

#         results.append({
#             "Website": website,
#             "Email": email,
#             "Phone": phone
#         })

# df = pd.DataFrame(results).drop_duplicates()

# df.to_excel("lead_generator.xlsx", index=False)

# print(df)





# import requests
# import pandas as pd
# import re
# from bs4 import BeautifulSoup

# queries = [
#     "marketing agency Baku",
#     "digital marketing Baku",
#     "reklam agentliyi Bakı"
# ]

# headers = {"User-Agent": "Mozilla/5.0"}

# email_pattern = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"
# phone_pattern = r"\+994[\s\-]?\d{2}[\s\-]?\d{3}[\s\-]?\d{2}[\s\-]?\d{2}"

# results = []

# for query in queries:

#     print("Searching:", query)

#     for page in range(0, 90, 30):

#         url = "https://html.duckduckgo.com/html/"
#         data = {"q": query, "s": page}

#         response = requests.post(url, data=data, headers=headers)

#         soup = BeautifulSoup(response.text, "html.parser")

#         for a in soup.select("a.result__a"):

#             website = a.get("href")

#             email = "Not found"
#             phone = "Not found"

#             try:
#                 page_data = requests.get(
#                     website,
#                     headers=headers,
#                     timeout=8
#                 )

#                 emails = re.findall(email_pattern, page_data.text)
#                 phones = re.findall(phone_pattern, page_data.text)

#                 if emails:
#                     email = emails[0]

#                 if phones:
#                     phone = phones[0]

#             except:
#                 pass

#             results.append({
#                 "Website": website,
#                 "Email": email,
#                 "Phone": phone
#             })

# df = pd.DataFrame(results).drop_duplicates()

# df.to_excel("lead_generator.xlsx", index=False)

# print(df)







# import requests
# import pandas as pd
# import re
# from bs4 import BeautifulSoup
# import time

# queries = [
#     "marketing agency Baku",
#     "digital marketing Baku",
#     "reklam agentliyi Bakı",
#     "SEO agency Baku",
#     "social media marketing Baku"
# ]

# headers = {"User-Agent": "Mozilla/5.0"}

# email_pattern = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"
# phone_pattern = r"(\+994[\s\-]?\d{2}[\s\-]?\d{3}[\s\-]?\d{2}[\s\-]?\d{2}|0\d{2}[\s\-]?\d{3}[\s\-]?\d{2}[\s\-]?\d{2})"

# results = []

# for query in queries:

#     print("Searching:", query)

#     for page in range(0, 210, 30):

#         url = "https://html.duckduckgo.com/html/"
#         data = {"q": query, "s": page}

#         response = requests.post(url, data=data, headers=headers)

#         soup = BeautifulSoup(response.text, "html.parser")

#         for a in soup.select("a.result__a"):

#             website = a.get("href")

#             email = "Not found"
#             phone = "Not found"
#             linkedin = "Not found"
#             instagram = "Not found"

#             try:

#                 page_data = requests.get(
#                     website,
#                     headers=headers,
#                     timeout=8
#                 )

#                 html = page_data.text

#                 emails = re.findall(email_pattern, html)
#                 phones = re.findall(phone_pattern, html)

#                 if emails:
#                     email = emails[0]

#                 if phones:
#                     phone = phones[0]

#                 soup2 = BeautifulSoup(html, "html.parser")

#                 for link in soup2.find_all("a", href=True):

#                     href = link["href"]

#                     if "linkedin.com" in href:
#                         linkedin = href

#                     if "instagram.com" in href:
#                         instagram = href

#             except:
#                 pass

#             results.append({
#                 "Website": website,
#                 "Email": email,
#                 "Phone": phone,
#                 "LinkedIn": linkedin,
#                 "Instagram": instagram
#             })

#             time.sleep(1)

# df = pd.DataFrame(results).drop_duplicates()

# df.to_excel("lead_generator_pro.xlsx", index=False)

# print("Total leads:", len(df))









# from concurrent.futures import ThreadPoolExecutor
# import requests
# import re
# from bs4 import BeautifulSoup

# email_pattern = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"
# phone_pattern = r"(\+994[\s\-]?\d{2}[\s\-]?\d{3}[\s\-]?\d{2}[\s\-]?\d{2})"

# headers = {"User-Agent": "Mozilla/5.0"}

# def scrape_site(website):

#     email = "Not found"
#     phone = "Not found"
#     linkedin = "Not found"
#     instagram = "Not found"

#     try:

#         page = requests.get(website, headers=headers, timeout=6)

#         html = page.text

#         emails = re.findall(email_pattern, html)
#         phones = re.findall(phone_pattern, html)

#         if emails:
#             email = emails[0]

#         if phones:
#             phone = phones[0]

#         soup = BeautifulSoup(html, "html.parser")

#         for link in soup.find_all("a", href=True):

#             href = link["href"]

#             if "linkedin.com" in href:
#                 linkedin = href

#             if "instagram.com" in href:
#                 instagram = href

#     except:
#         pass

#     return {
#         "Website": website,
#         "Email": email,
#         "Phone": phone,
#         "LinkedIn": linkedin,
#         "Instagram": instagram
#     }

# with ThreadPoolExecutor(max_workers=10) as executor:
#     results = list(executor.map(scrape_site, websites))




# import requests
# import pandas as pd
# import re
# from bs4 import BeautifulSoup
# from concurrent.futures import ThreadPoolExecutor

# queries = [
#     "marketing agency Baku",
#     "digital marketing Baku",
#     "reklam agentliyi Bakı"
# ]

# headers = {"User-Agent": "Mozilla/5.0"}

# email_pattern = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"
# phone_pattern = r"\+994[\s\-]?\d{2}[\s\-]?\d{3}[\s\-]?\d{2}[\s\-]?\d{2}"

# websites = []

# # SEARCH
# for query in queries:

#     print("Searching:", query)

#     url = "https://html.duckduckgo.com/html/"
#     data = {"q": query}

#     response = requests.post(url, data=data, headers=headers)

#     soup = BeautifulSoup(response.text, "html.parser")

#     for a in soup.select("a.result__a"):
#         website = a.get("href")

#         if website and website.startswith("http"):
#             websites.append(website)

# websites = list(set(websites))


# # SCRAPER
# def scrape_site(website):

#     email = "Not found"
#     phone = "Not found"
#     linkedin = "Not found"
#     instagram = "Not found"

#     try:

#         page = requests.get(website, headers=headers, timeout=6)

#         html = page.text

#         emails = re.findall(email_pattern, html)
#         phones = re.findall(phone_pattern, html)

#         if emails:
#             email = emails[0]

#         if phones:
#             phone = phones[0]

#         soup = BeautifulSoup(html, "html.parser")

#         for link in soup.find_all("a", href=True):

#             href = link["href"]

#             if "linkedin.com" in href:
#                 linkedin = href

#             if "instagram.com" in href:
#                 instagram = href

#     except:
#         pass

#     return {
#         "Website": website,
#         "Email": email,
#         "Phone": phone,
#         "LinkedIn": linkedin,
#         "Instagram": instagram
#     }


# # PARALLEL SCRAPE
# with ThreadPoolExecutor(max_workers=10) as executor:
#     results = list(executor.map(scrape_site, websites))


# df = pd.DataFrame(results).drop_duplicates()

# df.to_excel("lead_generator_pro.xlsx", index=False)

# print("Total leads:", len(df))
# print(df)






import requests
import pandas as pd
import re
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor
from urllib.parse import urljoin

queries = [
"marketing agency Baku",
"digital marketing Baku",
"seo agency Baku",
"social media agency Baku",
"advertising agency Baku",
"branding agency Baku",
"web design agency Baku",
"reklam agentliyi Bakı",
"digital agency Azerbaijan",
"SEO company Azerbaijan"
]

headers = {"User-Agent": "Mozilla/5.0"}

email_pattern = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"
phone_pattern = r"\+994[\s\-]?\d{2}[\s\-]?\d{3}[\s\-]?\d{2}[\s\-]?\d{2}"

blocked_domains = [
    "youtube",
    "facebook",
    "instagram",
    "linkedin",
    "wikipedia",
    "clutch",
    "sortlist",
    "manifest",
    "techbehemoths"
]

websites = []

# SEARCH
for query in queries:

    print("Searching:", query)

    url = "https://html.duckduckgo.com/html/"
    data = {"q": query}

    response = requests.post(url, data=data, headers=headers)

    soup = BeautifulSoup(response.text, "html.parser")

    for a in soup.select("a.result__a"):

        website = a.get("href")

        if not website:
            continue

        if any(domain in website for domain in blocked_domains):
            continue

        if website.startswith("http"):
            websites.append(website)

websites = list(set(websites))


# SCRAPER
def scrape_site(website):

    email = "Not found"
    phone = "Not found"
    linkedin = "Not found"
    instagram = "Not found"
    company = "Unknown"

    try:

        page = requests.get(website, headers=headers, timeout=6)

        html = page.text

        soup = BeautifulSoup(html, "html.parser")

        # company name
        if soup.title:
            company = soup.title.text.strip()

        # emails + phones
        emails = re.findall(email_pattern, html)
        phones = re.findall(phone_pattern, html)

        if emails:
            email = emails[0]

        if phones:
            phone = phones[0]

        # social links
        for link in soup.find_all("a", href=True):

            href = link["href"]

            if "linkedin.com" in href:
                linkedin = href

            if "instagram.com" in href:
                instagram = href

        # contact page scraping
        for link in soup.find_all("a", href=True):

            href = link["href"].lower()

            if "contact" in href:

                contact_url = urljoin(website, href)

                try:

                    contact_page = requests.get(
                        contact_url,
                        headers=headers,
                        timeout=6
                    )

                    emails = re.findall(email_pattern, contact_page.text)
                    phones = re.findall(phone_pattern, contact_page.text)

                    if emails:
                        email = emails[0]

                    if phones:
                        phone = phones[0]

                except:
                    pass

    except:
        pass

    return {
        "Company": company,
        "Website": website,
        "Email": email,
        "Phone": phone,
        "LinkedIn": linkedin,
        "Instagram": instagram
    }


# PARALLEL SCRAPE
with ThreadPoolExecutor(max_workers=10) as executor:
    results = list(executor.map(scrape_site, websites))


df = pd.DataFrame(results).drop_duplicates()

df.to_excel("lead_generator_pro.xlsx", index=False)

print("Total leads:", len(df))
print(df)