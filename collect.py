from bs4 import BeautifulSoup
import os
import pandas as pd
import re

d = {'title': [], 'price': [], 'link': []}

for file in os.listdir("data"):
    with open(f"data/{file}", encoding='utf-8') as f:
        html_doc = f.read()
    soup = BeautifulSoup(html_doc, 'html.parser')

    # Title & Link
    div = soup.find("div", {"data-cy": "title-recipe"})
    if not div:
        continue

    a_tag = div.find("a", class_="a-link-normal s-line-clamp-2 s-link-style a-text-normal")
    if not a_tag:
        continue

    title = a_tag.get_text(strip=True)
    link = "https://www.amazon.in" + a_tag["href"]

    # Price
    price_span = soup.find("span", class_="a-price")
    price = price_span.find("span", class_="a-offscreen") if price_span else None
    price = price.get_text(strip=True) if price else "N/A"

    # Clean price to remove ₹ or any special characters
    price = re.sub(r"[^\d,]", "", price)

    d['title'].append(title)
    d['link'].append(link)
    d['price'].append(price)

# Save to CSV
df = pd.DataFrame(data=d)
df.to_csv("data.csv", index=False)

print("Saved data.csv with", len(df), "entries.")
print("Data collection complete.")