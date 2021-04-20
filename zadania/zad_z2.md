# Zadanie 2

## (kurs zaawansowany)


1. Ściągnij na dysk po czym umieść w swoim środowisku Pythona (Collabie/Jupyter Labie) plik [titanic.csv](../data/titanic.csv)
2. Stosując odpowiednią funkcję zaimportuj jego zawartość do Pandas DataFrame
3. Sprawdź, jaki procent pasażerów przetrwał katastrofę. Skorzystaj z metody `value_counts()` na serii. Czy potrafisz jej wyniki programistycznie przeliczyć na procenty?
4. Znajdź kolumnę, w której przechowywany jest wiek pasażerów. Oblicz średnią i odchylenie standardowe dla wieku. Narysuj histogram, pokazujący rozkład wieku (zastosuj metodę `hist()` na serii)
5. Pokaż nazwisko, płeć i informację o tym czy przeżyli dla dwudziestu pierwszych pasażerów w zbiorze. Skorzystaj z wyrażenia `.loc[]`