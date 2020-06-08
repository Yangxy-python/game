#coding:utf-8
import pygal
import pygal_maps_world
import math
import csv


##在csv文件中获得信息

def read_csv_as_nested_dict(filename, keyfield, separator, quote): #读取原始csv文件的数据，格式为嵌套字典
    """
    输入参数:
      filename:csv文件名
      keyfield:键名
      separator:分隔符
      quote:引用符
    #输出:
    读取csv文件数据，返回嵌套字典格式，其中外层字典的键对应参数keyfiled，内层字典对应每行在各列所对应的具体值
    """
    result={}
    with open(filename,newline="")as csvfile:
        csvreader=csv.DictReader(csvfile,delimiter=separator,quotechar=quote)
        for row in csvreader:
            rowid=row[keyfield]
            result[rowid]=row

    return result

##整理信息

def reconcile_countries_by_name(pygal_countries, gdp_countries):  # 返回在世行有GDP数据的绘图库国家代码字典，以及没有世行GDP数据的国家代码集合
    """
    
    输入参数:
    plot_countries: 绘图库国家代码数据，字典格式，其中键为绘图库国家代码，值为对应的具体国名
    gdp_countries:世行各国数据，嵌套字典格式，其中外部字典的键为世行国家代码，值为该国在世行文件中的行数据（字典格式)
    
    输出：
    返回元组格式，包括一个字典和一个集合。其中字典内容为在世行有GDP数据的绘图库国家信息（键为绘图库各国家代码，值为对应的具体国名),
    集合内容为在世行无GDP数据的绘图库国家代码
    """
    c_nam= []
    c1_nam = []

    name_sd_get = []
    name_sd_none = []

    for k, v in gdp_countries.items():

        c_nam.append(v["Country Name"])

    for key, value in pygal_countries.items():
        c1_nam.append(value)

    # 判断哪些不在地图上面，即missing country
    for i in c1_nam:
        if i in c_nam:
            name_sd_get.append(list(pygal_countries.keys())[list(pygal_countries.values()).index(i)])
        else:
            name_sd_none.append(list(pygal_countries.keys())[list(pygal_countries.values()).index(i)])

    c_nam_s = {}
    for i in name_sd_get:
        c_nam_s[i] = pygal_countries[i]
    #print(name_sd_get)
    result = (c_nam_s,name_sd_none)

    return result


#判断没有数据的国家
def build_map_dict_by_name(gdp_countries, No_countries, year,plot_countries):
    """
    输入参数:
    gdpinfo: 
	plot_countries: 绘图库国家代码数据，字典格式，其中键为绘图库国家代码，值为对应的具体国名
	year: 具体年份值
	
    输出：
    输出包含一个字典和二个集合的元组数据。其中字典数据为绘图库各国家代码及对应的在某具体年份GDP产值（键为绘图库中各国家代码，值为在具体年份（由year参数确定）所对应的世行GDP数据值。为
    后续显示方便，GDP结果需转换为以10为基数的对数格式，如GDP原始值为2500，则应为log2500，ps:利用math.log()完成)
    2个集合一个为在世行GDP数据中完全没有记录的绘图库国家代码，另一个集合为只是没有某特定年（由year参数确定）世行GDP数据的绘图库国家代码

    """
    #替换country code，因为gdp_countries比plot大，所以先进行一个判断,再进行替换。

    n_num = {}
    c_N_y = []
    #print(plot_countries.keys())
    for h,l in plot_countries.items():
        for k, v in gdp_countries.items():

            if l == v['Country Name']:

                n = h
                if v[year] == '':

                    c_N_y.append(n)
                else:
                    m = math.log(eval(v[year]),10)
                    n_num[n] = m



    result1 = (n_num,No_countries,c_N_y)
    return result1


def render_world_map(result1, year, map_file):  # 将具体某年世界各国的GDP数据(包括缺少GDP数据以及只是在该年缺少GDP数据的国家)以地图形式可视化
    """
    Inputs:
      
      gdpinfo:gdp信息字典
      plot_countires:绘图库国家代码数据，字典格式，其中键为绘图库国家代码，值为对应的具体国名
      year:具体年份数据，以字符串格式程序，如"1970"
      map_file:输出的图片文件名
    
    目标：将指定某年的世界各国GDP数据在世界地图上显示，并将结果输出为具体的的图片文件
    提示：本函数可视化需要利用pygal.maps.world.World()方法
     

    """

    worldmap_chart = pygal.maps.world.World()
    worldmap_chart.title = "全球GDP分布图"
    #print(result1[0])
    worldmap_chart.add(year,result1[0])
    worldmap_chart.add('missing from the world bank',result1[1])
    worldmap_chart.add('no data at this year',result1[2])
    worldmap_chart.render_to_file(map_file)




gdpinfo = {
        "gdpfile": "isp_gdp.csv",   #数据源csv文件
        "separator": ",",          #csv文件分隔符
        "quote": '"',             #csv文件引用符
        "min_year": 1960,       #数据记载最小年份
        "max_year": 2015,       #数据记载最大年份
        "country_name": "Country Name",    #国家名
        "country_code": "Country Code"     #国家代码
    }

filename = gdpinfo['gdpfile']
keyfield = gdpinfo['country_code']
separator = gdpinfo['separator']
quote = gdpinfo['quote']


pygal_countries = pygal.maps.world.COUNTRIES #这里解决了问题1


gdp_countries = read_csv_as_nested_dict(filename, keyfield, separator, quote) #得到字典
#print(gdp_countries)
result= reconcile_countries_by_name(pygal_countries, gdp_countries)           #进行筛选不在地图中的
plot_countries = result[0]                                                    #代码：国名
No_countries = result[1]

year = input("请输入你想查看的年份（在1960到2015之间）")
map_file = "isp_gdp_world_name_"+year+".svg"

result1 = build_map_dict_by_name(gdp_countries, No_countries, year,plot_countries)         #进行筛选没有数据的
render_world_map(result1, year, map_file)                                   #画图
