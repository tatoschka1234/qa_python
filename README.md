# qa_python

### test_add_new_book_add_two_books
* **test steps**: two new books were added
* **expected result, positive**: dictionary `books_rating` contains 2 books

### test_set_book_rating_9_rating_set_ok
* **test steps**: add book, set rating
* **expected result, positive**: dictionary `books_rating` contains book's rating

### test_set_book_rating_below_the_range_default_is_set
* **test steps**: add book, set rating below the range
* **expected result, negative**: rating were set to default

### test_set_book_rating_above_the_range_default_is_set
* **test steps**: add book, set rating below the range
* **expected result, negative**: rating were set to default

### test_set_book_rating_noexisting_book_not_set
* **test steps**: set rating for not added books
* **expected result, negative**: rating is not set

### test_get_books_with_specific_rating
* **test steps**: add 2 books with the same rating
* **expected result, positive**: got these 2 books by the rating

### test_add_book_in_favorites_add_two_books
* **test steps**: add two books, add them to favorites
* **expected result, positive**: these two books are in `favorites` list

### test_delete_book_from_favorites_add_two_books
* **test steps**: add two books, add them to favorites, delete one from favorites
* **expected result, positive**: `favorites` list contains just one book

### test_add_book_in_favorites_nonexisting_book_not_added
* **test steps**: add not existing books to favorites
* **expected result, negative**: `favorites` list is empty

### test_add_new_book_add_twice_added_once
* **test steps**: add the same books twice
* **expected result, negative**: dictionary `books_rating` contains just one book