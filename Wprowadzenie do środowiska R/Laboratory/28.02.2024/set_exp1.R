#zestaw 1 -  28.02.2024

### homework:
    ### zadanie 4
    ### zadanie 5
    ### zadanie 6(c,d)


# command

# rm(n) - del object n
# ls() - create object in memory
# rm(list == ls*()) del all object in memory
# getwd() # path to file
# setwd(path) # go to directory

# Zadanie 1
# Wektor mpg zawiera następujące dane o zużyciu paliwa w milach 
# przejechanych na 1 galonie dla 10
# wybranych losowo samochodów

mpg <- c(19.0, 31.0, 30.0, 32.8, 12.0, 26.6, 25.8, 29.9, 26.0, 17.6)
# 1 mila = 1609m, 1 galon = 3.785l
# mpg * 1609 / 3.785 
# 100 - zp
zp <- (100*3.785)/(mpg * 1.609)

# zadanie 2
# Dla wektora x <- rnorm(20, 350, 30)opisującego wartość 20 losowo wybranych 
# transakcji (w zł) wykonaj następujące polecenia.
 
# a) Oblicz długość wektora x.
# b) Wypisz pierwsze 3 wartości wektora x.
# c) Wypisz 5 ostatnich wartości wektora x.
# d) Oblicz wartość średnią i odchylenie standardowe.
# e) Wyznacz wartość najmniejszą i największą.
# f) Wyznacz medianę.
# g) Podaj liczbę transakcji, których wartość przekracza 400 zł.
# h) Podaj liczbę transakcji, których wartość jest w zakresie 300-350 zł.
# i) Utwórz wektor y z wartością tych transakcji w euro.

x <- rnorm(20, 350, 30)
# a) 
len <- length(x)

# b)
doublet <- x[1:3]
doublet <- x[c(1,2,3)]
doublet <- head(x, 3)

# c)  
last <- tail(x, 5)

# d)
mean(x)
sd(x)

# e) 
min(x)
max(x)

# f)
median(x)

# g)
must <- x[x>400] 
sum(must)

# h)
segment <- x[x >= 300 & x <= 350]

# i)
curs_euro <- 4.31
euro <- x/curs_euro


# Zadanie 3
# Dla wektora x <- c(7, NA, -1, 2.5, 4, 2, 9, -0.8, NA)
# a) Wypisz wartości dodatnie wektora.
# b) Wypisz wartości na nieparzystych indeksach wektora.
# c) Zlicz ile wartości jest większych od 1.
# d) Zlicz ile jest braków danych.
# e) Wypisz indeksy elementów, których wartości są ujemne.
# f) Wypisz indeks największej wartości wektora.

x <- c(7, NA, -1, 2.5, 4, 2, 9, -0.8, NA)

# a)
non_negeative <- x[x > 0]
# b)
odd_idex <- seq(1, length(x), 2)
odd_item <- x[odd_idex]
# c)
sum(x > 1, na.rm = T)
# d)
sum(is.na(x))
# e)
which(x < 0)
# f)
which.max(x)

# (kollokwium) zadanie 4 ...
# zadanie 5 ...

# zadanie 6

# Zadanie 6 Dla wektora o wartościach: 7.9, 6.7, 6.2, 15.0, 5.5, 6.6, 2.8, 7.0, 6.1, 6.2, 6.5, 8.7, 6.8, 8.6
# a) Wyznacz kwartyl dolny Q1, kwartyl górny Q3 oraz rozstęp międzykwartylowy IQR=Q3-Q1.
# b) Podaj wartość największą i najmniejszą.
# c) Zastąp braki danych wartością średnią.
# d) Sprawdź, czy są obserwacje odstające (czyli poniżej Q1-1,5*IQR lub powyżej Q3+1,5*IQR).
# e) Czy wszystkie wartości tego wektora są większe od 6?
# f) Czy jakakolwiek (przynajmniej jedna) wartość wektora jest większa od 6?

args <- c(7.9, 6.7, 6.2, 15.0, 5.5, 6.6, 2.8, 7.0, 6.1, 6.2, 6.5, 8.7, 6.8, 8.6)

# a)
summary(args)
quantile(args, 0.25) # q1
quantile(args, 0.75) # q2
IQR(args) 

# b)
max(args)
min(args)

# c) ...
# d) ...

# e) 
all(args > 6)

# f)
any(args > 6)

