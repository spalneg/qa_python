import pytest
from main import BooksCollector


class TestBooksCollector:

    def test_add_new_book_two_books_added(self):
        collector = BooksCollector()
        collector.add_new_book('Вино из одуванчиков')
        collector.add_new_book('Посёлок')
        assert len(collector.books_genre) == 2
        

    def test_add_new_book_add_same_book_inability(self):
        collector = BooksCollector()
        collector.add_new_book('Звёздные войны: Войны клонов')
        collector.add_new_book('Звёздные войны: Войны клонов')
        assert len(collector.books_genre) == 1 

    def test_set_book_genre_genre_added(self):
        collector = BooksCollector()
        collector.add_new_book('Застава на Якорном поле')
        collector.set_book_genre('Застава на Якорном поле', 'Фантастика')
        assert collector.books_genre['Застава на Якорном поле'] == 'Фантастика'
    
    def test_set_book_genre_set_nonexistent_genre_inability(self):
        collector = BooksCollector()
        collector.add_new_book('Вархаммер 40к для чайников')
        collector.set_book_genre('Вархаммер 40к для чайников', 'Учебники')
        assert collector.books_genre['Вархаммер 40к для чайников'] == ''
    
    @pytest.mark.parametrize('book,genre',            
        [['Москва - Петушки', 'Ужасы'],   
        ['Колобок', 'Детективы'],  
        ['Думай и богатей', 'Фантастика']])
    def test_get_book_genre_return_genre(self, book, genre):
        collector = BooksCollector()
        collector.add_new_book(book)
        collector.set_book_genre(book, genre)
        assert collector.get_book_genre(book) == genre

    def test_get_books_with_specific_genre_get_two_books_list(self):
        collector = BooksCollector()
        collector.add_new_book('1984')
        collector.add_new_book('Молчание ягнят')
        collector.add_new_book('Скотный двор')
        collector.set_book_genre('1984', 'Фантастика')
        collector.set_book_genre('Молчание ягнят', 'Детективы')
        collector.set_book_genre('Скотный двор', 'Фантастика')
        assert len(collector.get_books_with_specific_genre('Фантастика')) == 2

    def test_get_books_genre_return_two_books_dictionary(self):
        collector = BooksCollector()
        collector.add_new_book('Cто лет одиночества')
        collector.add_new_book('Дети дюны')
        collector.set_book_genre('Дети дюны', 'Фантастика')
        assert collector.get_books_genre() == {'Cто лет одиночества': '', 'Дети дюны': 'Фантастика'}
    
    @pytest.mark.parametrize('book,genre',            
        [['Москва - Петушки', 'Ужасы'],   
        ['Колобок', 'Детективы']])
    def test_get_books_for_children_exclude_age_rating_books(self, book, genre):
        collector = BooksCollector()
        collector.add_new_book(book)
        collector.set_book_genre(book, genre)
        assert collector.get_books_for_children() == []
    

    def test_add_book_in_favorites_add_same_book_inability(self):
        collector = BooksCollector()
        collector.add_new_book('Герой должен быть один')
        collector.add_book_in_favorites('Герой должен быть один')
        collector.add_book_in_favorites('Герой должен быть один')
        assert len(collector.get_list_of_favorites_books()) == 1

    def test_delete_book_from_favorites_added_book_deleted(self):
        collector = BooksCollector()
        collector.add_new_book('Чапаев и Пустота')
        collector.add_book_in_favorites('Чапаев и Пустота')
        collector.delete_book_from_favorites('Чапаев и Пустота')
        assert collector.get_list_of_favorites_books() == []


    def test_get_list_of_favorites_books_return_favorite_books(self):
        collector = BooksCollector()
        collector.add_new_book('Человек в Высоком замке')
        collector.add_new_book('Последняя битва')
        collector.add_book_in_favorites('Последняя битва')
        assert len(collector.get_list_of_favorites_books()) == 1