import pytest
#в фикстуре collector создаем экземпляр класса и добавляем туда книгу "Гордость и предубеждение и зомби"
initial_book = 'Гордость и предубеждение и зомби'
books_list = ['Дизайн для реального мира', 'Рождение сложности', 'Слепой часовщик']
book_not_in_dictionary = 'Задача трех тел'
class TestBooksCollector:
    def test_add_new_book_add_two_books(self, collector):
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_rating()) == 2

    def test_add_new_book_name_is_as_assigned(self, collector):
      # проверяем словарь - там одна книга - название соотвествует добавленному
        assert list(collector.books_rating.keys()) == [initial_book]

    #параметризация чтобы проверить тестовые значения для КЭ (1,10)
    @pytest.mark.parametrize('correct_rating', [1, 2, 7, 9, 10])
    def test_set_book_rating_in_range_rating_as_assigned(self, collector, correct_rating):
        # меняем рейтинг добавленной книги
        collector.set_book_rating(initial_book, correct_rating)
        # проверяем, что рейтинг соотвествует назначенному
        assert collector.books_rating[initial_book] == correct_rating

    # параметризация чтобы проверить тестовые значения для <=1 и КЭ >= 11)
    @pytest.mark.parametrize('not_correct_rating', [-1, 0, 11, 12, 27])
    def test_set_book_rating_outside_range_rating_stays_1(self, collector, not_correct_rating):
        # меняем рейтинг добавленной книги на рейтинг вне диапазона (1,11)
        collector.set_book_rating('Гордость и предубеждение и зомби', not_correct_rating)
        # проверяем, что рейтинг остался 1
        assert collector.books_rating['Гордость и предубеждение и зомби'] == 1

    def test_add_new_book_name_adding_existing_book_with_rating_not_1_doesnt_change_rating(self, collector):
        #меняем рейтинг добавленной книги
        collector.set_book_rating(initial_book, 7)
        #снова пытаемся добавить эту книгу
        collector.add_new_book(initial_book)
        #проверяем что рейтинг не поменялся на 1
        assert collector.books_rating[initial_book] != 1

    def test_get_book_rating_default_rating_is_1(self, collector):
        # проверяем что рейтинг добавленной книги 1
        assert collector.books_rating.get(initial_book) == 1

    @pytest.mark.parametrize('rating', [1, 2, 5, 8, 9, 10])
    def test_get_book_rating_check_rating_is_as_assigned(self, collector, rating):
        collector.set_book_rating(initial_book, rating)
        # проверяем, что рейтинг соотвествует назначенному
        assert collector.get_books_rating() == {initial_book: rating}

    @pytest.mark.parametrize('names, rating', [['Эгоистичный ген', 10], ['День триффидов', 6], ['Чайка по имени Джонатан Ливингстон', 7]])
    def test_get_books_with_specific_rating_returns_book_by_rating(self, collector, names, rating):
        collector.add_new_book(names)
        collector.set_book_rating(names, rating)
        assert collector.get_books_with_specific_rating(rating) == [names]

    def test_get_books_with_specific_rating_returns_rating_1_returns_all_books_with_default_rating(self, collector):
        #добавляем книги списком
        for book in books_list:
            collector.add_new_book(book)
        #добавляем в список ту книгу, с которой создавался экземпляр класса в фикстуре
        books_list.insert(0, initial_book)
        #проверяем что все добавленные книги выводятся по рейтингу 1
        assert collector.get_books_with_specific_rating(1) == books_list

    def test_get_books_with_specific_rating_rating_not_exist_result_in_empty_list(self, collector):
        #проверяем что если запросить тот рейтинг которого нет - будет пустой список
        assert collector.get_books_with_specific_rating(7) == []

    def add_book_in_favorites_added_book_is_in_favorites(self, collector):
        collector.add_book_in_favorites(initial_book)
        assert collector.favorites == [initial_book]

    def delete_book_from_favorites_deleted_book_is_not_in_favorites(self,collector):
        collector.add_book_in_favorites(initial_book)
        collector.delete_book_from_favorites(initial_book)
        assert collector.favorites == []

    def get_list_of_favorites_books_list_is_as_added(self, collector):
        # добавляем книги списком
        for book in books_list:
            collector.add_new_book(book)
            collector.add_book_in_favorites(book)
        assert collector.favorites == books_list

    def get_books_rating_for_not_added_book_no_rating(self, collector):
        assert collector.get_books_rating(book_not_in_dictionary) == None

    def add_books_in_favorites_book_is_not_in_dictionary_cannot_add_to_favorites(self, collector):
        collector.add_book_in_favorites(book_not_in_dictionary)
        assert collector.favorites == []

    #нельзя добавить одну и ту же книгу дважды в словарь
    def add_new_book_cannot_add_same_book_again(self, collector):
        collector.add_new_book(initial_book)
        assert len(collector.get_books_rating()) == 1

    #нельзя добавить одну и ту же книгу дважды в избранное
    def add_book_in_favorites_cannot_add_same_book_again(self, collector):
        collector.add_book_in_favorites(initial_book)
        collector.add_book_in_favorites(initial_book)
        assert len(collector.favorites) == 1
