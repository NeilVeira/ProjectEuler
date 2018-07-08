digits = ["one","two","three","four","five","six","seven","eight","nine","ten", \
          "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", \
          "eighteen", "nineteen"]
tens = ["twenty","thirty","forty","fifty","sixty","seventy","eighty","ninety"]
hundred = "hundred"
thousand = "one thousand"

all_words = []
words_99 = list(digits)

first_100 = 0
for x in digits:
    first_100 += len(x)
    
ten_sum = 0
for digit in digits[:9]:
    ten_sum += len(digit)
#print ten_sum

for ten in tens:
    first_100 += len(ten)*10 + ten_sum
    words_99.append(ten)
    for digit in digits[:9]:
        words_99.append(ten+" "+digit)
#print first_100

all_words = list(words_99)
total = first_100
for h in range(9):
    total += len(digits[h]+hundred)
    all_words.append(digits[h]+" "+hundred)
    
    prefix = len(digits[h]+hundred+"and")
    for word in words_99:
        all_words.append(digits[h]+" "+hundred+" and "+word)
    total += first_100 + prefix*99
    

all_words.append(thousand)
total += len(thousand)-thousand.count(" ")

ans = 0
for word in all_words:
    print word
    ans += len(word)-word.count(" ")
print total
print ans