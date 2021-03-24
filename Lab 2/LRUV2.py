PageFrames=3    
#pagesInMainMemory
PageRequestsOrder=['A','B','A','C','A','B','D','B','A','C','D']
#order of the requested pages

memoryFrame=[None]*PageFrames
secondChance=[None]*PageFrames

for page in range(0,len(PageRequestsOrder)):
    for chance in range (0,len(memoryFrame)):#untuk initiallize all the spaces in the memory frames
        if memoryFrame[chance]==None:
            memoryFrame[chance]=PageRequestsOrder[page]
            secondChance[chance]=0
            for chance2 in range(0,len(memoryFrame)):
                secondChance[chance]=0
            break
        elif memoryFrame[chance]==PageRequestsOrder[page]:
            secondChance[chance]=1
            break
    if secondChance[PageFrames-1]!=None:
        cutValue=page
        break

for page in range(page+1,len(PageRequestsOrder)):
    if PageRequestsOrder[page] in memoryFrame:#untuk check the memory frame untuk matching ngan sequence (basically nak set second chance ke 1 if ada any)
        match =memoryFrame.index(PageRequestsOrder[page])
        secondChance[match]=1
        continue#kalau dah set the 2ndChance to 1, terus continue to next element in sequence of requests
    else:#if the current element tak match with any element in the memory frames
        for chance in range(0,len(secondChance)):#untuk compare with all the 2ndChance frames dari 0-2 (mana yang kosong) untuk masukkan the element of the request sequence
            if secondChance[chance]==0:
                memoryFrame[chance]=PageRequestsOrder[page]
                for chance2 in range (0,len(secondChance)):#untuk set semua 0 bila dah masuk dah
                    secondChance[chance2]=0
                break

print("second chance: "+str(secondChance))
print("memory frame:  "+str(memoryFrame))


