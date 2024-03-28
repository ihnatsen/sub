# 20.03.2024

# Zadanie 7 Na ramce danych airports z pakietu nycflights13 zawierającej 
# nazwy lotnisk i ich lokalizacje wykonaj
# następujące polecenia:3
# a) wybierz 100 losowych wierszy,
# b) wybierz 5% losowych wierszy,
# c) wybierz 10 pierwszych wierszy,
# d) wybierz 6 ostatnich wierszy

# install.packages('nycflights13')
# library(nycflights13)
# data(airports)

# a)
random_values <- sample(nrow(airports), 100)
random_values <- airports[random_values, ]

# b)
five_pr <- sample(nrow(airports), 0.05 * nrow(airports))
five_pr <- airports[five_pr, ]

# c) 
top_ten <- airports[1:10, ]

# d)
aoutsid_six <- tail(airports, 6)


# Zadanie 8 Załaduj ramkę danych planes z pakietu nycflights13, zawierającą 
# informacje techniczne o samolotach realizujących loty z lotnisk JFK, LGA, EWR 
# w Nowym Jorku w 2013 roku. Na jej podstawie:
# a) wywołaj summary() na ramce danych planes, co otrzymujemy?
# b) stwórz ramkę zawierającą wszystkie samoloty z określoną średnią prędkość 
# przelotową, tj. różną od NA,
# c) utwórz wektor z wartościami tailnum dla samolotów produkowanych po 2012 
# roku,
# d) utwórz wektor z pierwszymi 20 wartościami tailnum dla samolotów o liczbie 
# miejsc między 100 a 200 (seats),
# e) stwórz ramkę zawierającą wszystkie samoloty pochodzące jedynie od 
# producentów BOEING, AIRBUS,
# EMBRAER,
# f) stwórz ramkę zawierającą wszystkie samoloty pochodzące jedynie od 
# producentów BOEING, AIRBUS,
# EMBRAER i liczbie miejsc większej od 300.


# install.packages('nycflights13')
# library(nycflights13)
data(planes)

# a) 
summary(planes)

# b)
data_set_not_null <- planes[!is.na(planes$speed), ]

# c) 
arg <- planes$tailnum[planes$year > 2012 & !is.na(planes$year)]


# d)
head(planes$tailnum[planes$seats >= 100 & planes$seats<=200], 20)

# e)
names_prod <- c('BOEING', 'AIRBUS', 'EMBRAER')
data_prod <- planes$manufacturer%in%names_prod
data_prod <- planes[data_prod, ]
sum(data_prod)

