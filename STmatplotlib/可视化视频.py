import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import matplotlib.animation as animation
from IPython.display import HTML
import time

df = pd.read_csv('hs300history.csv',
                 usecols=['name', 'group', 'year', 'value'])

colors = dict(zip(
    ['India', 'Europe', 'Asia', 'Latin America',
     'Middle East', 'North America', 'Africa'],
    ['#adb0ff', '#ffb3ff', '#90d595', '#e48381',
     '#aafbff', '#f7bb5f', '#eafb50']
))
group_lk = df.set_index('name')['group'].to_dict()
scale = 9/16

def draw_barchart(value):
    thisIndex,nextIndex,step = value
    print(thisIndex,nextIndex,step)
    # print(time.time())
    #取出top10

    dffsname = set(df[df['year'].eq(thisIndex)].sort_values(by='value', ascending=True).tail(10)["name"])
    dffename = set(df[df['year'].eq(nextIndex)].sort_values(by='value', ascending=True).tail(10)["name"])
    allname = list(dffsname|dffename)
    dffs = df[(df["year"].isin([thisIndex])) & (df["name"].isin(allname))].sort_values(by='value', ascending=True)
    dffe = df[(df["year"].isin([nextIndex])) & (df["name"].isin(allname))].sort_values(by='value', ascending=True)
    dffs["numbers"] = range(dffs.shape[0])
    dffe["numbers"] = range(dffe.shape[0])
    # print(allname)
    # print(dffs)
    # print(dffe)
    dfft = pd.concat([dffs , dffe])
    # print(dfft)


    # df[(df["year"].eq(year)) & (df["name"].isin(allname)) ]
    # print(df[(df["year"].eq(year)) & (df["name"].eq("Dhaka"))]["group"].values[0])
    # print(dfft[(dfft["year"].eq(thisIndex)) & (dfft["name"].eq("New York"))]["group"].values[0],)
    data = [{"name":name,
             "group":dfft[(dfft["year"].eq(thisIndex)) & (dfft["name"].eq(name))]["group"].values[0],
             "year":thisIndex,
             "value":dfft[(dfft["year"].eq(thisIndex)) & (dfft["name"].eq(name)) ]["value"].values[0]+(dfft[(dfft["year"].eq(nextIndex)) & (dfft["name"].eq(name)) ]["value"].values[0]-dfft[(dfft["year"].eq(thisIndex)) & (dfft["name"].eq(name)) ]["value"].values[0])*step,
             "numbers":dfft[(dfft["year"].eq(thisIndex)) & (dfft["name"].eq(name)) ]["numbers"].values[0]+(dfft[(dfft["year"].eq(nextIndex)) & (dfft["name"].eq(name)) ]["numbers"].values[0]-dfft[(dfft["year"].eq(thisIndex)) & (dfft["name"].eq(name)) ]["numbers"].values[0])*step-(len(allname)-10),
             } for name in allname]
    # print(data)

    dff = pd.DataFrame(data).sort_values(by='value', ascending=True).tail(20)
    # dff["index"] = range(10)
    # dff["index"] = [1,2,3,4,5,6,7,8,9,10]
    # print(dff)
    # print(time.time())
    ax.clear()
    # ax.barh(dff['name'], dff['value'], color=[colors[group_lk[x]] for x in dff['name']],align="center")
    ax.barh( dff['numbers'].values,dff['value'].values, color=[colors[group_lk[x]] for x in dff['name']])
    dx = dff['value'].max() / 200
    for value, name in zip(dff['value'], dff['name']):
        thisnumbers = dff[(dff["year"].eq(thisIndex)) & (dff["name"].eq(name))]["numbers"].values[0]
        if thisnumbers > -0.5:
            ax.text(value - dx, thisnumbers, name, size=14, weight=600, ha='right', va='bottom') # 城市名称
            ax.text(value - dx, thisnumbers-.25, group_lk[name], size=10, color='#444444', ha='right', va='baseline') # 分组名称
            ax.text(value + dx, thisnumbers, f'{value:,.0f}', size=14, ha='left', va='center') # 数值
    
    # ... polished styles
    ax.text(1, 0.4, thisIndex, transform=ax.transAxes, color='#777777', size=46, ha='right', weight=800)#年份
    ax.text(1, 0.6, "{}_{}_{}".format(thisIndex,nextIndex,int(step*addframes)), transform=ax.transAxes, color='#777777', size=46, ha='right', weight=800)  # debug
    ax.text(0, 1.06, 'Population (thousands)', transform=ax.transAxes, size=12, color='#777777')#单位
    ax.xaxis.set_major_formatter(ticker.StrMethodFormatter('{x:,.0f}'))#坐标轴格式
    ax.xaxis.set_ticks_position('top')#坐标轴位置
    ax.tick_params(axis='x', colors='#777777', labelsize=12)#坐标轴格式
    ax.set_yticks([])#取消y坐标

    ax.margins(0, 0.01)#缩放坐标轴
    ax.grid(which='major', axis='x', linestyle='-') # x轴网格线
    ax.set_axisbelow(True) # 置顶数据条
    ax.text(0, 1.10, 'The most populous cities in the world from 1500 to 2018',
            transform=ax.transAxes, size=24, weight=600, ha='left')
    #     ax.text(1, 0, 'by QIML', transform=ax.transAxes, ha='right',
    #             color='#777777', bbox=dict(facecolor='white', alpha=0.8, edgecolor='white'))#添加标题
    plt.ylim(-1,9.5)
    plt.box(False) #去掉边框
    plt.savefig("xx.jpg")

fig, ax = plt.subplots(figsize=(15,15*scale))

addframes = 25

# for f in [(x,x+1,s/addframes)for x in range(2016,2018) for s in range(addframes)]:
#     draw_barchart(f)
# for year in range(2016,2018):
#     print(year , set(df[df['year'].eq(year)].sort_values(by='value', ascending=True).tail(10)["name"]))


# fig, ax = plt.subplots(figsize=(15,15*scale))
animator = animation.FuncAnimation(fig, draw_barchart, frames=[(x,x+1,s/addframes)for x in range(2000,2020) for s in range(addframes)][:-addframes+1])
# animator.save('xx.gif',writer='imagemagick', fps=25)
animator.save('xx.mp4', fps=25)