# 18:06:2024

# list of string 
lst <- list('apple', 'orange', 'cherry', 'lemon')

# length list
length(lst)

# cheaking element in list
'apple' %in% lst

# add element in the end list
# after position where item will be add
new_lst <- append(lst, 'banana', after=0)

# slices Remove elements from list
new_lst <- lst[-1]
# remove list from the first element from list

thislist <- list("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
thislist[2:5]
print((thislist)[2:5])

# Loop through lst

for(item in lst){
  print(item)
}

# join lst
lst_one = list('R', 'Python', 'Java')
lst_two = list('are language')

# return list
join = c(lst_one, lst_two)

# String
the_first_str <- 'Hello, World!'

# return number char in string
number <- '123456789'
nchar(number)

# search char or substring:
str <- 'Hello, Ivan!'
I <- 'I'
Hello <- 'Hello'
grepl(I, str)
grepl(Hello, str)

# join string:
str_one <- 'Hello'
str_two <- 'Ivan'
paste(str_one, str_two)

# ternary operator R 
ifelse(-10 > -1, 1, 'oops')

# split string by chars
strsplit('Value for split', split = ' ')

# dict
map <- list()
map['name'] = 'Ivan'

# return null
print(map['nope'])

# slice string:
string <- 'Abandon hope all ye who enter here ...'
substring(string, 1, 7)

# R not have set. Use the crutch.
x <- list(1, 1, 2, 2, 3, 3, 4, 4, 5, 5)
x[!duplicated(x)]

# library for working date: 
install.packages("lubridate")
library(lubridate)

ymd(20230602) # year-month-date
ymd_hm(202306021533) # year-month-date-hour-minute
mdy("April 13, 1978") # month date year
dmy(241216) # day-month-year


# Step 1: Define the date string
date_three <- 'April 13, 1978'

# If it's not in English, set it to English
Sys.setlocale("LC_TIME", "C")

# Step 2: Convert the string to a date object using as.Date
date_converted <- as.Date(date_three, '%B %d, %Y', )

# Print the converted date
print(date_converted)

# get year date:
myDate <- Sys.Date()
format(myDate, '%Y')

# as numeric:
as.numeric(format(myDate, "%Y"))

# get day of week:
weekdays(myDate)

# get month of date:
months(myDate)

# get quarters
quarters(myDate)

# sequence date
start <- '2023/6/1'
end <- '2023/7/31'
# by = list['day', 'month', week, 2 weeks, ...]
seq(as.Date(start), as.Date(end), '2 week')
