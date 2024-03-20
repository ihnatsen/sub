# 13.03.2024

# Zadanie 1 Utwórz listę złożoną z dwóch wektorów napisów:
#     warzywa <- c('burak', 'seler', 'marchew')
#     owoce <- c('gruszka', 'banan', 'cytryna', 'ananas')
#     Dla tej listy wykonaj następujące polecenia:
# a) Wypisz do konsoli zawartość pierwszego elementu listy.
# b) Zastąp dwie ostatnie wartości pierwszego elementu listy nazwami ulubionych dwóch warzyw i wyświetl
# w konsoli zmodyfikowaną listę.
# c) Rozszerz listę o trzeci element, którym jest wektor liczbowy z długościami wektorów warzywa i owoce.
# d) Połącz wszystkie elementy listy w jeden wektor.
# ...


vector = c(1:10, 0, 0, -1, -2, -4)
arg = list(vector[vector > 0], vector[vector < 0], vector[vector == 0])


pigs <- as.list(ToothGrowth)
pigs[[2]] <- as.character(pigs[[2]])

split_ = split(pigs$len, pigs$supp)

mean_one = mean(split_[[1]])
mean_two = mean(split_[[2]])

