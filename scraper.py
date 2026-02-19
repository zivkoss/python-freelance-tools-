import pandas as pd
from bs4 import BeautifulSoup
import argparse

def scrape_test():
    with open('test_page.html', 'r', encoding='utf-8') as f:
        html = f.read()
    
    soup = BeautifulSoup(html, 'html.parser')
    products = soup.find_all('div', class_='product-item')
    all_products = []
    
    for product in products:
        name = product.find('a', class_='product-name').text.strip()
        price = product.find('span', class_='price').text.strip()
        all_products.append({'name': name, 'price': price, 'url': 'test.com'})
    
    df = pd.DataFrame(all_products)
    df.to_csv('test_products.csv', index=False)
    print(f"✅ Сачувано {len(df)} производа!")
    return df

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Web Scraper (test)")
    parser.add_argument("--test", action="store_true", help="Тест мод")
    args = parser.parse_args()
    
    if args.test:
        scrape_test()
    else:
        print("❌ Прво тестирај: python scraper.py --test")
