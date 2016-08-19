__author__ = 'Drew'

import random
import urllib

totalRating = 0.0
num = 0.0
nums = []

def getRating(index):
    titles = open('NFTitles', 'r')
    authors = open('NFAuthors', 'r')

    nameOfBook = ""
    author = ""

    numBooks = 0
    for line in titles:
        numBooks+=1
        if(numBooks == index):
            nameOfBook = replaceSpaceWithPlus(line, '')

    numAuthors = 0
    for line in authors:
        numAuthors+=1
        if(numAuthors == index):
            author = replaceSpaceWithPlus(line, '')

    print('index: ' + str(index))
    print(nameOfBook)
    print(author)

    try:
        stream = urllib.urlopen('http://www.amazon.com/s/ref=nb_sb_noss?url=search-alias%3Dstripbooks&field-keywords=' + nameOfBook + '+' + author)
        for line in stream:
            if('out of 5 stars' in line):
                ind = line.index('out of 5 stars')
                num = line[ind-4:ind-1]
                if (('.') in num) == False:
                    num = num[2:]
                stream.close()
                titles.close()
                authors.close()
                stream.close()
                return float(num)
        stream.close()
    except:
        print('error')

    titles.close()
    authors.close()
    return 0.0

def replaceSpaceWithPlus(str, newstr):
    for a in str:
        if a == ' ':
            newstr += '+'
        elif a == ',':
            newstr += ''
        else:
            newstr += a
    return newstr

for x in range(12165, 12166):
    rating = getRating(x)
    if rating != 0.0:
        nums += [rating]
        totalRating += rating
        num += 1
        print('rating: ' + str(rating))
        try:
            with open('NFRatings', 'a') as ratings:
                ratings.write(str(rating) + ', ')
        except:
            print('error1')
        print('current average: ' + str(totalRating/num))
        print(' ')
        print('--------------------------------------')
        print(' ')

numsFile = open('NFArray', 'r+')
numsFile.write(str(nums))
numsFile.close()
