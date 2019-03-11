def readName():
    x=[0,1,2,3,4]
    for num in x:
        yield {
            'Text':num
        }
result=readName()
print(result.__next__())
print(result.__next__())

# for i in result:
#     print(i)
