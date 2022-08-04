
'''
Алгоритм рекомендацій
'''
from math import sqrt,pow
import operator
import json
class UserCf():
    def __init__(self,data):
        self.data=data

    #список фільмів користувача
    def getItems(self,username1,username2):
        return self.data[username1],self.data[username2]

    #коєфіцієнт кореляції для двох користувачів
    def pearson(self,user1,user2):
        sumXY=0.0
        n=0
        sumX=0.0
        sumY=0.0
        sumX2=0.0
        sumY2=0.0
        try:
            for movie1,score1 in user1.items():
                if movie1 in user2.keys():
                    n+=1
                    sumXY+=score1*user2[movie1]
                    sumX+=score1
                    sumY+=user2[movie1]
                    sumX2+=pow(score1,2)
                    sumY2+=pow(user2[movie1],2)

            molecule=sumXY-(sumX*sumY)/n
            denominator=sqrt((sumX2-pow(sumX,2)/n)*(sumY2-pow(sumY,2)/n))
            r=molecule/denominator
        except Exception as e:
            print("Інформація про помилку:", e.message)
            return None
        return r

    #Розрахувати відстань до поточного користувача і знайти найближчого користувача
    def nearstUser(self,username,n=1):
        distances={}#Користувач, схожість
        for otherUser,items in self.data.items():#Переглянути весь набір даних
            if otherUser not in username:#Інший користувач
                distance=self.pearson(self.data[username],self.data[otherUser])#Вирахувати схожість двох користувачів
                distances[otherUser]=distance
        sortedDistance=sorted(distances.items(),key=operator.itemgetter(1),reverse=True)#найбільш схожі користувачі
        print ("Відсортовані користувачі:",sortedDistance)
        return sortedDistance[:n]


    #Рекомендувати фільми
    def recomand(self,username,n=1):
        recommand={}
        for user,score in dict(self.nearstUser(username,n)).items():#найбільш схожф користувачі
            print()
            print (user,"схожість у смаках: ",score)
            for movies,scores in self.data[user].items():#Список фільмів, що рекомендуються
                if movies not in self.data[username].keys():#Ім'я користувача не знайдено
                    print (user, "рекомендує", movies)
                    if movies not in recommand.keys():#Додати в список рекомендацій
                        recommand[movies]=scores

        return sorted(recommand.items(),key=operator.itemgetter(1),reverse=True)

if __name__=='__main__':
    print("Введіть назву файлу:")
    name_file=input()

    with open(name_file, 'r') as f:
        data_u = json.load(f)
    userCf=UserCf(data=data_u)
    recommandList=userCf.recomand('Toby', 3)
    print ("\nОстання рекомендація:", recommandList)


    my_file = open("output.txt", "w")
    my_file.write(str(recommandList))
    my_file.close()