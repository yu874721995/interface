# a = '01,02,03,04,05'
# b = '2,3,4,5,6'
# for i in eval(b):
#     if str(i) in a:
#         print(i)
import pymysql,requests,time


import arrow


def isLeapYear(years):
    '''
    通过判断闰年，获取年份years下一年的总天数
    :param years: 年份，int
    :return:days_sum，一年的总天数
    '''
    # 断言：年份不为整数时，抛出异常。
    assert isinstance(years, int), "请输入整数年，如 2018"
    if ((years % 4 == 0 and years % 100 != 0) or (years % 400 == 0)):  # 判断是否是闰年
        # print(years, "是闰年")
        days_sum = 366
        return days_sum
    else:
        # print(years, '不是闰年')
        days_sum = 365
        return days_sum


def getAllDayPerYear(years):
    '''
    获取一年的所有日期
    :param years:年份
    :return:全部日期列表
    '''
    start_date = '%s-1-1' % years
    a = 0
    all_date_list = []
    days_sum = isLeapYear(int(years))
    while a < days_sum:
        b = arrow.get(start_date).shift(days=a).format("YYYY-MM-DD")
        a += 1
        all_date_list.append(b)
    # print(all_date_list)
    return all_date_list
num = []
for i in ['2010','2011','2012','2013','2014','2015','2016','2017','2018','2019','2020']:
    all_date_list = getAllDayPerYear(i)
    import re
    for i in all_date_list:
        print(i)
        try:
            r = requests.post('https://kaijiang.aicai.com/open/kcResultByDate.do',data={
                'gameIndex':305,
                'searchDate':i,
                'gameFrom':''
            })
            li_list = re.findall(r'<td[^>]*>(.*?)</td>',r.json()['resultHtml'],re.I|re.M)
            lens = int(len(li_list) / 3)
            s = {}
            p = 0
            for i in range(0,lens):
                s['preDrawIssue'] = li_list[p]
                s['otherStyleTime'] = li_list[p+1]
                s['preDrawCode'] = li_list[p+2]
                p += 3
                num.append((s['preDrawCode'], s['preDrawIssue'], s['otherStyleTime']))

            # for item in r.json()['data']:
            #     timeStamp = int(item['preDrawTime']) / 1000
            #     timeArray = time.localtime(timeStamp)
            #     otherStyleTime = time.strftime("%Y-%m-%d", timeArray)
            #     num.append((item['preDrawCode'], item['preDrawIssue'], otherStyleTime))
        except Exception as e:
            print(e)
for i in num:
    print(i)
print(len(num))



conn = pymysql.connect(
    host= '127.0.0.1',
    user= 'root',password='123456',
    database= 'yu',
    charset= 'utf8')

cursor = conn.cursor()
sql = 'insert into js_numpy(kj_num,qh,time) values(%s,%s,%s);'
cursor.executemany(sql,num)
conn.commit()
cursor.close()
conn.close()
