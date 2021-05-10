# Zadanie 4

## (kurs zaawansowany)

1. Dla zmiennej `Survived` zamień kodowanie w ten sposób, że zamień `0` na `no` i `1` na `yes`. Umieść przekodowane wartości w nowej zmiennej `survived_r`.
2. Sprawdź, czy istnieje istotna statystycznie korelacja pomiędzy wiekiem a ceną biletu (`Fare`). Użyj `Pingouin.corr()`.
3. Zweryfikuj hipotezę mówiącą, że grupa osób, które przeżyły katastrofę była istotnie statystycznie **młodsza** niż grupa osób, która nie przeżyła katastrofy. Użyj `Pingouin.ttest()`.
4. Zweryfikuj hipotezę mówiącą, że mężczyźni mieli większą szansę na przetrwanie niż kobiety. Sprawdź, jaki procent osób nie przeżyło katastrofy łącznie oraz osobno dla każdej płci. Sprawdź, czy te proporcje są niezależne testem Chi^2. Skorzystaj z `Pingouin.chi2_independence()`.