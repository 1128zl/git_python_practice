from die import Die 
import plotly.express as px

die1=Die()
die2=Die(10)
die3=Die(8)

results=[]

for roll_num in range(5000):
    result=die1.roll()+die2.roll()+die3.roll()
    results.append(result)
    
#print(results)

#分析结果
frequencies=[]
poss_results=range(1,die1.num_sides+die2.num_sides+die3.num_sides+1)
for value in poss_results:
    frequency=results.count(value)
    frequencies.append(frequency)

#print(frequencies)

title="Results of Rolling a D6 , a D10 and a D8 Dice 5000 Times"
labels={'x':'Result','y':'Frequency Of Result'}
fig=px.bar(x=poss_results,y=frequencies,title=title,labels=labels)
fig.update_traces(marker_color='green', width=0.5)
fig.update_layout(xaxis_dtick=1)

fig.show()

fig.write_html('dice_visual_d6d10d8.html')