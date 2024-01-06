from html_parser import fetch_html
from db_manager import ManageDB
print("Imported modules")
db_path = 'html_files.db'

db = ManageDB(db_path)
domains = db._collect_data()
print(domains)
list_of_no_html_domains = []

for category in domains:
    print("Starting to fetch HTML")
    for index, domain in enumerate(domains[category]):
        print(f"Fetching HTML for {domain}")
        html = fetch_html(domain)
        if html:
            print(f"HTML fetched for {domain}")
            db._insert_data(db_path, category, domain, html)
        else:
            list_of_no_html_domains.append(domain)
            print(f"Error fetching HTML for {domain}")
            continue
db._close_database()