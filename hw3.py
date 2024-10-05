# Oski stole your power
def computePower(x,y):
    answer = x
    for i in range(y-1):
        answer = answer * x
    print (answer)

computePower (2,3)


# What should I wear?
def tempRange(readings):
    low = min(readings)
    high = max(readings)
    range = (low, high)
    print (range)

tempRange([15, 14, 17, 20, 23, 28, 20])


# Check if its the weekend
def isWeekend(day):
    if (day == 6 or day == 7):
        return True
    else:
        return False

print (isWeekend(6))


#Fuel efficieny calculator
def fuel_efficiency(distance,fuel):
    eff = distance / fuel
    print (eff)

fuel_efficiency(70, 21.5)


# Secret code
def decodeNumbers(n):
    same = n//10 
    move = n % 10
    print (move,same)

decodeNumbers (12345)


# Min max with for loops
def find_min_for(nums):
    minf = nums[0]
    for number in nums:
        if number < minf:
            minf = number
    print (minf)
nums = [2024, 98, 131, 2, 3, 72]
find_min_for(nums)

def find_max_for(nums):
    maxf = nums[0]
    for number in nums:
        if number > maxf:
            maxf = number
    print (maxf)
find_max_for(nums)

# Min max with while loops
def find_min_while(nums):
    minw = nums[0]
    i = 0
    while (i < len(nums)):
        if nums[i] < minw:
            minw = nums[i]
        i = i + 1
    print (minw)
find_min_while(nums)

def find_max_while(nums):
    maxw = nums[0]
    i = 0
    while (i < len(nums)):
        if nums[i] > maxw:
            maxw = nums[i]
        i = i + 1
    print (maxw)
find_max_while(nums)

# Counting vowels
def vowel_and_consonant_count(text):
    vowels = 0
    consonants = 0
    letters = []
    for i, char in enumerate(text):
        if char.isalpha() == True:
            letters.append(char)
        continue
    for letter in letters:
        if letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u' or letter == "A" or letter == 'E' or letter == 'I' or letter == 'O' or letter == 'U':
            vowels = vowels + 1
        else:
            consonants = consonants + 1
    count = (vowels, consonants)
    print (count)

text = "UC Berkeley, founded in 1868!"
vowel_and_consonant_count(text)

# Calculate digital root
def digital_root(num):
    total = 0
    num_str = str(num)
    for i, value in enumerate(num_str):
        addition = int(value)
        total = total + addition
    print (total)

num = 2468
digital_root(num)