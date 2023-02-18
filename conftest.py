import pytest
from main import BooksCollector

#заготовка чтобы начинать любой тест с создания экземпляра класса и добавления туда одной книги
@pytest.fixture()
def collector():
    collector = BooksCollector()
    collector.add_new_book('Гордость и предубеждение и зомби')
    return collector


