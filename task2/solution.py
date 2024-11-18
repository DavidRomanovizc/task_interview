import csv
import json
from collections import Counter

import httpx
from bs4 import BeautifulSoup

BASE_URL = "https://ru.wikipedia.org"
CATEGORY_URL = f"{BASE_URL}/wiki/Категория:Животные_по_алфавиту"
CYRILLIC = 'абвгдеёжзиклмнопрстуфхцчшщэюя'


def fetch_animal_names(url: str) -> list[str]:
    names = []
    with httpx.Client() as client:
        while url:
            response = client.get(url)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, "html.parser")

            names += [li.text for li in soup.select(".mw-category-group ul li a")]

            next_page = soup.find("a", string="Следующая страница")
            url = f"{BASE_URL}{next_page['href']}" if next_page else None

    return names


def count_animals_by_letter(names: list[str]) -> dict[str, int]:
    counts = Counter(name[0].upper() for name in names if name and name[0].lower() in CYRILLIC)

    return dict(counts)


def save_to_csv(data: dict[str, int], filename: str = "beasts.csv") -> None:
    sorted_data = sorted(data.items())

    with open(filename, mode="w", encoding="utf-8", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Word", "Count"])
        writer.writerows(sorted_data)


def save_names(data: list[str], filename: str = "names.json") -> None:
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)


def load_names(filename: str = "names.json") -> list[str]:
    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)


def main():
    try:
        names = load_names()
    except FileNotFoundError:
        names = fetch_animal_names(CATEGORY_URL)
        save_names(names)

    counts = count_animals_by_letter(names)
    save_to_csv(counts)


if __name__ == "__main__":
    main()
