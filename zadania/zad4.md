## Zadanie 4

Napisz program przeprowadzający _"psychotest"_. Wymyśl swoje własne pytania. Niech użytkownik udziela odpowiedzi na skali Likerta, tj. na przykład na skali od 1 do 5 gdzie 1 oznacza _zupełnie się nie zgadzam_ a 5 oznacza _całkowicie się zgadzam_. Po przejściu całego testu niech program zsumuje punkty i w zależności od wyniku wypluje diagnozę. 

Uwagi:

- Pytań niech będzie co najmniej 5
- Treść pytań jak i diagnozy dowolna. Może a nawet powinna być twórcza/zabawna/lekko głupawa
- Niech treść pytań znajdzie się w pliku `pytania.txt` i niech program sczytuje pytania do listy
- Odpowiedź użytkownika powinna być zbierana za pomocą funkcji `input()`. Sprawdź w dokumentacji/googlu jak działa taka funkcja.
- Każde pytanie powinno być zadawane poprzez funkcję typu `zadaj_pytanie(treść_pytania)`. Funkcja powinna wyświetlić pytanie, opis skali ("1 oznacza _zupełnie się nie zgadzam_ a 5 oznacza _całkowicie się zgadzam_" lub coś podobnego) oraz funkcję `input()` pobierającą odpowiedź. Funkcja powinna **zwrócić odpowiedź użytkownika jako `int`**. Program powinien korzystać z wartości zwracanej przez funkcję aby sformułować diagnozę