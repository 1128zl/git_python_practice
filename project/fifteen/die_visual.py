from die import Die 
import plotly.express as px
die =Die()

results=[]

for roll_num in range(1000):
    result=die.roll()
    results.append(result)
    
#print(results)

#分析结果
frequencies=[]
poss_results=range(1,die.num_sides+1)
for value in poss_results:
    frequency=results.count(value)
    frequencies.append(frequency)

#print(frequencies)

title="Results of Rolling One D6 1000 Times"
labels={'x':'Result','y':'Frequency Of Result'}
fig=px.bar(x=poss_results,y=frequencies,title=title,labels=labels)
fig.update_traces(marker_color='green', width=0.5)
fig.show()
