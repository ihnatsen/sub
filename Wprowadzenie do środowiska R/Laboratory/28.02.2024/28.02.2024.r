# ctrl + L - очистка консоли 
# ctrl + shift + C - комент

a0  <- c(1, 0, 2, 3, 1, 0, 4) # иницилизация вектора.
a   <- 3:100 # последовательности 
cop <- rep(10, 5) # копия
a1  <- seq(0, 15 , 3) # start, strop , step

# оператор присваенвания <-, ->, = 

v <- c(3, 2, 4, 5, 1)
v1 <- rep(rep(10,2),2)
3:6 -> n 
n = 100; n = 200

age  <- c(30, 23, 21, 27, 33, 27)

# bool vector
TRUE 
one <- c(TRUE)
one_and_one <- rep(one,2)

c(TRUE, FALSE, T, F)

# txt vector 

s <- c('Python', 'Java', 'R', 'JavaScript')
name <- c('Ivan', 'Ola', 'Jan', 'Bob', 'Tomi')

# random value

# ?sample - doc
random <- sample(10)
sample(20,5) # [0,20]x5 рандомных
sample(20,5, TRUE) # возможный повтор, дифолт нету
sample(LETTERS, 5) # рандомные буквы
sample(20:30, 10) # использование среза [20:30] x 10
sample(name,2) # если уникальных типов есть меньше чем требуется сгенерировать 
# выдаст ошибку

rnorm(10, 0, 1)
# N(0,1) десять рандомных чисел с N(0,1)
x <- rnorm(1e+4,0, 1)
hist(x)

sum(x)
mean(x)
sum(age)
mean(age)
sd(age) # D*0.5

length(v)
sort(v)
y <- sort(v, decreasing = TRUE) # replace
sort(name)
unique(name) # возращает сет
nchar(name)

str(nchar(name))
str(length(name))

min(age)
max(age)

(1:10)^2

1/(1:10)^2

v
v <- c(1:6)
v+v # операции нужно чтобы было кратно 
v + 10
v1 <-c(1:4)
v + v1
v2 <- c(1:3)
v2 + v
c(1, 2, 3) * c(10, 100 , 1000)

5 > 2

1:5 > 2
age == 21

sum(age==21)

!TRUE & FALSE

age > 29 & age <  41

# brak dannych 

x <- c(2, NA, 1, 5, NA, 3, )
is.na(x)

is.numeric(x)

sum(is.na(x))

2%in%x # in 

2+x

sum(x)
sum(x, na.rm = NA)

# index 

age[1:2]
age[c(1, 2, 5)] 
age[2:3]

age[0:1]
age[length(age)]
age[1e+10]

head(age)
head(age, n=3)
tail(age, n=3)

age[]
age[-1]
age[-c(1)]
age[-c(1:2)]

age[age>25] # фильтрация
age[age>29 & age<41]

s[s != 'R']
x[!is.na(x)] # удаление элементов с NA

age
which(age > 25) # возращает index

which(age == 27)
which.max(age)

s[1] <- "MS Excel"

s[s != "R"] <- 'cos'

s[100000000] <- 'Pascal'

# Hierarchy
txt    <-  c('R', 1:2, -6.7, FALSE, 7L)
floats <-  c(1:2, -6.7, F, T, 7L)
ints   <-  c(F, T, 7L)
bools <- c(F, T)
foo <-  c

# type

as.integer()
as.numeric()
as.logical()
as.character()
as.double()

as.character(1:6)
as.numeric('abc')
as.integer(c(1.0, 2.1, 3.1, 4.5))
as.vector(1:6, 'logical')

# checking type of object
is.character()
is.integer()
is.double()
is.logical()
is.character(name)
is.logical(1:6)
is.vector(c(1:6))
