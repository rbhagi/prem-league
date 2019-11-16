import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

pd.set_option('display.max_rows', 100)
pd.set_option('display.max_columns', 10)
pd.set_option('display.width', 1000)

d = pd.read_csv('league.csv',dtype={"Season": int, "home": str, "visitor" : str, "hgoal" : int, "vgoal" : int, "goaldif" : int, "result" : str})


d = d.drop(['FT','tier','totgoal'], axis = 1)
d = pd.DataFrame(d[d.division == 1])
d1 = d[d.Season >= 2012]
dhome = d1[d1.home == 'Manchester United']
daway = d1[d1.visitor == 'Manchester United']
dh12 = dhome[dhome.Season == 2012]
dh15 = dhome[dhome.Season == 2015]
dh18 = dhome[dhome.Season == 2018]
da12 = daway[daway.Season == 2012]
da15 = daway[daway.Season == 2015]
da18 = daway[daway.Season == 2018]


#Plot for Goals scored and conceded at home for seasons 2012,2015,2018
plt.subplot(1,3,1)
plt.grid(color='black',linestyle=':')
plt.plot(dh12.visitor,dh12.hgoal,marker='s',label = '2012 Scored')
plt.plot(dh12.visitor,dh12.vgoal,marker='^',color='r',label = '2012 Conceded')
plt.xlabel('Opposition')
plt.xticks(rotation=90)
plt.tick_params(axis='x', labelsize=7)
plt.ylabel('Goals')
plt.ylim(-.5, 5.5)
plt.legend(loc = 'upper right')
plt.text(-1.5,6,'Man Utd scored '+str(sum(dh12.hgoal))+' in 2012 and conceded '+str(sum(dh12.vgoal))+' goals in 2012')
plt.text(-1.5,5.8,'Man Utd won '+str(sum(dh12.result == 'H'))+' , lost '+str(sum(dh12.result=='A'))+' and drew '+str(sum(dh12.result=='D'))+' games at Home')

plt.subplot(1,3,2)
plt.grid(color='black',linestyle=':')
plt.plot(dh15.visitor,dh15.hgoal,marker='s',label = '2015 Scored')
plt.plot(dh15.visitor,dh15.vgoal,marker='^',color='r',label = '2015 Conceded')
plt.xlabel('Opposition')
plt.xticks(rotation=90)
plt.tick_params(axis='x', labelsize=7)
plt.ylabel('Goals')
plt.ylim(-.5, 5.5)
plt.legend(loc = 'upper right')
plt.text(-1.5,6,'Man Utd scored '+str(sum(dh15.hgoal))+' in 2015 and conceded '+str(sum(dh15.vgoal))+' goals in 2015')
plt.text(-1.5,5.8,'Man Utd won '+str(sum(dh15.result == 'H'))+' , lost '+str(sum(dh15.result=='A'))+' and drew '+str(sum(dh15.result=='D'))+' games at Home')

plt.subplot(1,3,3)
plt.grid(color='black',linestyle=':')
plt.plot(dh18.visitor,dh18.hgoal,marker='s',label = '2018 Scored')
plt.plot(dh18.visitor,dh18.vgoal,marker='^',color='r',label = '2018 Conceded')
plt.xlabel('Opposition')
plt.xticks(rotation=90)
plt.tick_params(axis='x', labelsize=7)
plt.ylabel('Goals')
plt.ylim(-.5, 5.5)
plt.legend(loc = 'upper right')
plt.text(-1.5,6,'Man Utd scored '+str(sum(dh18.hgoal))+' in 2018 and conceded '+str(sum(dh18.vgoal))+' goals in 2018')
plt.text(-1.5,5.8,'Man Utd won '+str(sum(dh18.result == 'H'))+' , lost '+str(sum(dh18.result=='A'))+' and drew '+str(sum(dh18.result=='D'))+' games at Home')
plt.show()


#Plot for Goals scored and conceded away from home for seasons 2012,2015,2018
plt.subplot(1,3,1)
plt.grid(color='black',linestyle=':')
plt.plot(da12.home,da12.vgoal,marker='s',label = '2012 Scored')
plt.plot(da12.home,da12.hgoal,marker='^',color='r',label = '2012 Conceded')
plt.xlabel('Opposition')
plt.xticks(rotation=90)
plt.tick_params(axis='x', labelsize=7)
plt.ylabel('Goals')
plt.ylim(-.5, 5.5)
plt.legend(loc = 'upper right')
plt.text(-1,6,'Man Utd scored '+str(sum(da12.vgoal))+' goals and conceded '+str(sum(da12.hgoal))+' goals in 2012 ')
plt.text(-1,5.8,'and won '+str(sum(da12.result == 'A'))+' , lost '+str(sum(da12.result=='H'))+' and drew '+str(sum(da12.result=='D'))+' away from Home')

plt.subplot(1,3,2)
plt.grid(color='black',linestyle=':')
plt.plot(da15.home,da15.vgoal,marker='s',label = '2015 Scored')
plt.plot(da15.home,da15.hgoal,marker='^',color='r',label = '2015 Conceded')
plt.xlabel('Opposition')
plt.xticks(rotation=90)
plt.tick_params(axis='x', labelsize=7)
plt.ylabel('Goals')
plt.ylim(-.5, 5.5)
plt.legend(loc = 'upper right')
plt.text(-1,6,'Man Utd scored '+str(sum(da15.hgoal))+' goals and conceded '+str(sum(da15.vgoal))+' goals in 2015 ')
plt.text(-1,5.8,'and won '+str(sum(da15.result == 'A'))+' , lost '+str(sum(da15.result=='H'))+' and drew '+str(sum(da15.result=='D'))+' games away from Home')

plt.subplot(1,3,3)
plt.grid(color='black',linestyle=':')
plt.plot(da18.home,da18.vgoal,marker='s',label = '2018 Scored')
plt.plot(da18.home,da18.hgoal,marker='^',color='r',label = '2018 Conceded')
plt.xlabel('Opposition')
plt.xticks(rotation=90)
plt.tick_params(axis='x', labelsize=7)
plt.ylabel('Goals')
plt.ylim(-.5, 5.5)
plt.legend(loc = 'upper right')
plt.text(-1,6,'Man Utd scored '+str(sum(da18.vgoal))+' goals and conceded '+str(sum(da18.hgoal))+' goals in 2018 ')
plt.text(-1,5.8,'and won '+str(sum(da18.result == 'A'))+' , lost '+str(sum(da18.result=='H'))+' and drew '+str(sum(da18.result=='D'))+' games away from Home')
plt.show()


#Plot for Average number of Goals scored for seasons 2012,2015,2018 grouped by Home Games and Away Games against top 6 oppositions
plt.subplot(1,2,1)
plt.grid(color='grey', linestyle=':')
plt.scatter(dh12.visitor,dh12.goaldif,marker="s",s=125,label = '2012 Home Games')
plt.scatter(dh15.visitor,dh15.goaldif,color='g',s=150,label = '2015 Home Games')
plt.scatter(dh18.visitor,dh18.goaldif,color='red',marker='*',s=175,label = '2018 Home Games')
plt.xlabel('Opposition')
plt.xticks(rotation=90)
plt.tick_params(axis='x', labelsize=7)
plt.ylabel('Goal Difference')
plt.ylim(-5.5, 5.5)
plt.text(-1,6,'MU home games scoring avg: '+str(round(np.mean(dh12.goaldif),1))+' goals in 2012, '+str(round(np.mean(dh15.goaldif),1))+' in 2015 and '+str(round(np.mean(dh18.goaldif),1))+' in 2018')
plt.legend(loc = 'upper right')

plt.subplot(1,2,2)
plt.grid(color='grey', linestyle=':')
plt.scatter(da12.home,da12.goaldif,marker="s",s=125,label = '2012 Away Games')
plt.scatter(da15.home,da15.goaldif,color='g',s=150,label = '2015 Away Games')
plt.scatter(da18.home,da18.goaldif,color='red',s=175,marker='*',label = '2018 Away Games')
plt.xlabel('Opposition')
plt.xticks(rotation=90)
plt.tick_params(axis='x', labelsize=7)
plt.ylabel('Goal Difference')
plt.ylim(-5.5, 5.5)
plt.text(-1,6,'MU away games scoring avg: '+str(-(round(np.mean(da12.goaldif),1)))+' goals in 2012, '+str(-(round(np.mean(da15.goaldif),1)))+' in 2015 and '+str(-(round(np.mean(da18.goaldif),1)))+' in 2018')
plt.legend(loc = 'upper right')
plt.show()


home = ['Arsenal','Chelsea','Liverpool','Tottenham Hotspur','Manchester City']
visitor = ['Arsenal','Chelsea','Liverpool','Tottenham Hotspur','Manchester City']
top5home12 = dh12[dh12.visitor.isin(visitor)]
top5away12 = da12[da12.home.isin(home)]
top5home15 = dh15[dh15.visitor.isin(visitor)]
top5away15 = da15[da15.home.isin(home)]
top5home18 = dh18[dh18.visitor.isin(visitor)]
top5away18 = da18[da18.home.isin(home)]


#Plot for Average number of Goals scored for seasons 2012,2015,2018 grouped by Home Games and Away Games against top 6 oppositions
plt.subplot(1,2,1)
plt.grid(color='grey', linestyle=':')
plt.scatter(top5home12.visitor,top5home12.goaldif,marker="s",s=150,label = '2012 Home Games')
plt.scatter(top5home15.visitor,top5home15.goaldif,color='g',s=175,label = '2015 Home Games')
plt.scatter(top5home18.visitor,top5home18.goaldif,color='red',marker='*',s=200,label = '2018 Home Games')
plt.xlabel('Opposition')
plt.xticks(rotation=90)
plt.tick_params(axis='x', labelsize=7)
plt.ylabel('Goal Difference')
plt.ylim(-5.5, 5.5)
plt.text(-0.5,6,'MU home games scoring avg: '+str(round(np.mean(top5home12.goaldif),1))+' goals in 2012, '+str(round(np.mean(top5home15.goaldif),1))+' in 2015 and '+str(round(np.mean(top5home18.goaldif),1))+' in 2018')
plt.legend(loc = 'upper right')

plt.subplot(1,2,2)
plt.grid(color='grey', linestyle=':')
plt.scatter(top5away12.home,top5away12.goaldif,marker="s",s=150,label = '2012 Away Games')
plt.scatter(top5away15.home,top5away15.goaldif,color='g',s=175,label = '2015 Away Games')
plt.scatter(top5away18.home,top5away18.goaldif,color='red',marker='*',s=200,label = '2018 Away Games')
plt.xlabel('Opposition')
plt.xticks(rotation=90)
plt.tick_params(axis='x', labelsize=7)
plt.ylabel('Goal Difference')
plt.ylim(-5.5, 5.5)
plt.text(-0.5,6,'MU away games scoring avg: '+str(-(round(np.mean(top5away12.goaldif),1)))+' goals in 2012, '+str(-(round(np.mean(top5away15.goaldif),1)))+' in 2015 and '+str(-(round(np.mean(top5away18.goaldif),1)))+' in 2018')
plt.legend(loc = 'upper right')
plt.show()
