PageFrames=2    
#pagesInMainMemory
PageRequestsOrder=['A','B','A','C','A','B','D','B','A','C','D']
#order of the requested pages
Pages=['A','B','C','D']
#how many pages are there

def fifo(pageFrames,PageRequestOrder,Pages):
    interrupt=0
    pages=[0]*pageFrames
    currentPage=0
    print("time     page frame in ram       page requested      interrupt")
    for eachPage in range(0,len(PageRequestOrder)):
       # print(" ".join(str(pages)))
        if eachPage%2==0:
            currentPage=0       
            if  PageRequestOrder[eachPage]!=pages[0] or pages[0]==0:
                print("out: "+str(pages[0])+"--> in:"+str(PageRequestOrder[eachPage]))
                pages[0]=PageRequestOrder[eachPage]
                interrupt+=1
        else:
            currentPage=1
            if  PageRequestOrder[eachPage]!=pages[0] or pages[1]==0:
                print("out: "+str(pages[1])+"--> in:"+str(PageRequestOrder[eachPage]))
                pages[1]=PageRequestOrder[eachPage]
                interrupt+=1
        print(str(eachPage)+"        "+str(currentPage)+"                       "+PageRequestOrder[eachPage]+"                   "+str(interrupt))
        #print(" ".join(str(pages)))

fifo(PageFrames,PageRequestsOrder,Pages)




