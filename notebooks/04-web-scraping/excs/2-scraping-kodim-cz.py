from requests_html import HTMLSession

# Create a session
session = HTMLSession()

# Load the webpage
url = "https://kodim.cz"
response = session.get(url)

# Find elements containing course names
# It is assumed that the course names are in elements with a specific class

sections = response.html.find(".styles_menu__SHkwc a")

links = []
# Print the names of sections
for section in sections:
    # Append the href attribute (link) of each section to the links list
    links.append(section.attrs["href"])
print(links)

# Iterate through each link in the links list
for link in links:
    # Construct the URL for each section
    section_url = url + link
    # Fetch the webpage of the section
    section_page = session.get(section_url)
    # Find all h2 elements, assuming these are the course names
    for title in section_page.html.find(".styles_banner__p1HlQ h2"):
        # Print the text of each h2 element, which is the course name
        print(title.text)

# Close the session
session.close()
