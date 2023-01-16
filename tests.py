import pytest

from main import BooksCollector


class TestBooksCollector:

    @pytest.fixture(autouse=True)
    def collector(self):
        self.collector = BooksCollector()
        return self.collector

    @pytest.fixture
    def first_book_name(self):
        return 'Гордость и предубеждение и зомби'

    @pytest.fixture
    def first_book_rating(self):
        return 9

    @pytest.fixture
    def default_book_rating(self):
        return 1

    @pytest.fixture
    def second_book_name(self):
        return 'Что делать, если ваш кот хочет вас убить'

    def test_add_new_book_add_two_books(self, first_book_name,
                                        second_book_name):
        self.collector.add_new_book(first_book_name)
        self.collector.add_new_book(second_book_name)
        assert len(self.collector.get_books_rating()) == 2

    def test_set_book_rating_9_rating_set_ok(self, first_book_name,
                                              first_book_rating):
        self.collector.add_new_book(first_book_name)
        self.collector.set_book_rating(first_book_name, first_book_rating)
        assert (self.collector.get_book_rating(first_book_name) ==
                first_book_rating)

    def test_set_book_rating_below_the_range_default_is_set(
            self, first_book_name, default_book_rating):
        self.collector.add_new_book(first_book_name)
        self.collector.set_book_rating(first_book_name, 0)
        assert (self.collector.get_book_rating(first_book_name) ==
                default_book_rating)

    def test_set_book_rating_above_the_range_default_is_set(
            self, first_book_name, default_book_rating):
        self.collector.add_new_book(first_book_name)
        self.collector.set_book_rating(first_book_name, 11)
        assert (self.collector.get_book_rating(first_book_name) ==
                default_book_rating)

    def test_set_book_rating_noexisting_book_not_set(self, first_book_name):
        self.collector.set_book_rating(first_book_name, 5)
        assert len(self.collector.get_books_rating()) == 0

    def test_get_books_with_specific_rating(self, first_book_name,
                                            second_book_name):
        rating = 5
        self.collector.add_new_book(first_book_name)
        self.collector.add_new_book(second_book_name)
        self.collector.set_book_rating(first_book_name, rating)
        self.collector.set_book_rating(second_book_name, rating)
        assert self.collector.get_books_with_specific_rating(rating) == [
            first_book_name, second_book_name]

    def test_add_book_in_favorites_add_two_books(self, first_book_name,
                                                 second_book_name):
        self.collector.add_new_book(first_book_name)
        self.collector.add_book_in_favorites(first_book_name)
        self.collector.add_new_book(second_book_name)
        self.collector.add_book_in_favorites(second_book_name)
        assert self.collector.get_list_of_favorites_books() == [
            first_book_name, second_book_name]

    def test_delete_book_from_favorites_add_two_books(self, first_book_name,
                                                      second_book_name):
        self.collector.add_new_book(first_book_name)
        self.collector.add_book_in_favorites(first_book_name)
        self.collector.add_new_book(second_book_name)
        self.collector.add_book_in_favorites(second_book_name)
        self.collector.delete_book_from_favorites(first_book_name)
        assert self.collector.get_list_of_favorites_books() == [
            second_book_name]

    def test_add_book_in_favorites_nonexisting_book_not_added(
            self, first_book_name):
        self.collector.add_book_in_favorites(first_book_name)
        assert len(self.collector.get_list_of_favorites_books()) == 0

    def test_add_new_book_add_twice_added_once(self, first_book_name,
                                    default_book_rating):
        self.collector.add_new_book(first_book_name)
        self.collector.add_new_book(first_book_name)
        assert self.collector.get_books_rating() == {
            first_book_name: default_book_rating
        }
