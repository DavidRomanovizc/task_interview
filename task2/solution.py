import csv
from collections import defaultdict

import httpx
from bs4 import BeautifulSoup


def get_animals_count_by_letter() -> dict[str, int]:
    url = "https://ru.wikipedia.org/wiki/Категория:Животные_по_алфавиту"
    response = httpx.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    category_links = soup.find_all('a', class_='CategoryTreeLabel')

    count = defaultdict(int)

    for link in category_links:
        category_name = link.text.strip()
        if category_name:
            first_letter = category_name[0].upper()
            count[first_letter] += 1

    return count


def write_to_csv(count: dict[str, int]) -> None:
    with open('beasts.csv', mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        for letter, count in sorted(count.items()):
            writer.writerow([letter, count])


if __name__ == '__main__':
    animals_count = get_animals_count_by_letter()
    write_to_csv(animals_count)
    print("Data has been written to beasts.csv")
