import random
ger1={'das Jahr':'year','das Mal':'time','die Arbeit':'work'}
ger2={'die Leute':'people','das Beispiel':'example','das Prozent':'percent'}

ger=ger1.copy()
ger.update(ger2)

'''
for german in ger.values():
    print(german)
'''
right=0
wrong=0
broj_pitanja=input("Unesite broj pitanja (10,20,30) ")

for broj in range(1,int(broj_pitanja)):



    sl1=random.choice(list(ger.keys()))
    rkey=sl1
    rvalue=ger.get(sl1)
    print(rkey)
    qvalue=input('What is an english word for '+rkey+" ")
    if qvalue==rvalue:
        print("You are right!")
        right+=1

    else:
        print("You are wrong.Try again!")
        wrong+=1


#After the loop has finished
print("Right answers: "+str(right))
print("Wrong answers: "+str(wrong))
print("Percent of right answers: "+str(int(100*(right/(right+wrong)))))





'''
1. das Jahr, -e year	14. die Leute (pl.) people
2. das Mal, -e time (as in number of times)	15. die Arbeit, -en work, job
3. das Beispiel, -e example	16. das Prozent, -e percent
4. die Zeit time	17. die Hand, -¨e hand
5. die Frau, -en woman, wife, Mrs.	18. die Stadt, -¨e city
6. der Mensch, -en human being, man	19. der Herr, -en man, gentleman, Mr.
7. das Kind, -er child	20. der/das Teil, -e part
8. der Tag, -e day	21. das Problem, -e problem
9. der Mann, -¨er man	22. die Welt, -en world
10. das Land, -¨er country, land	23. das Recht, -e right, law
11. die Frage, -n question	24. das Ende, -n end
12. das Haus, -¨er house	25. die Million (Mio.), -en million
'''