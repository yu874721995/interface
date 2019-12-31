import  requests,time



import arrow


# def isLeapYear(years):
#     '''
#     通过判断闰年，获取年份years下一年的总天数
#     :param years: 年份，int
#     :return:days_sum，一年的总天数
#     '''
#     # 断言：年份不为整数时，抛出异常。
#     assert isinstance(years, int), "请输入整数年，如 2018"
#     if ((years % 4 == 0 and years % 100 != 0) or (years % 400 == 0)):  # 判断是否是闰年
#         # print(years, "是闰年")
#         days_sum = 366
#         return days_sum
#     else:
#         # print(years, '不是闰年')
#         days_sum = 365
#         return days_sum
#
#
# def getAllDayPerYear(years):
#     '''
#     获取一年的所有日期
#     :param years:年份
#     :return:全部日期列表
#     '''
#     start_date = '%s-1-1' % years
#     a = 0
#     all_date_list = []
#     days_sum = isLeapYear(int(years))
#     while a < days_sum:
#         b = arrow.get(start_date).shift(days=a).format("YYYY-MM-DD")
#         a += 1
#         all_date_list.append(b)
#     # print(all_date_list)
#     return all_date_list
#
# all_date_list = getAllDayPerYear("2019")
# num = []
# for i in all_date_list:
#     r = requests.post('https://www.cpyzj.com/req/cpyzj/lotHistory/getLotHistorys',data={
#         'token':'5122d9fbd7524205b963061d6528a0ce',
#         'timestamp':'1577345904515',
#         'lotGroupCode':'0',
#         'lotCode':'10006',
#         'queryPreDrawTime':i,
#         'pageNo':'1',
#         'pageSize':'100',
#         'sign':'8F94B2F5DC4266F32360666A5BF448DB'
#     })
#     for item in r.json()['data']:
#         num.append(item['preDrawCode'])
def reqs_30():
    import pymysql
    conn = pymysql.connect(
        host='127.0.0.1',
        user='root', password='123456',
        database='yu',
        charset='utf8')
    cursor = conn.cursor()
    inputs = input('请输入期数查询：')
    sql = 'select * from js_numpy where qh = %s;'
    cursor.execute(sql, inputs)
    reqs = cursor.fetchall()
    print(reqs)
    sqls = 'select * from (select * from js_numpy where qh < %s order by qh desc limit 30 ) as th order by qh;'
    cursor.execute(sqls,inputs)
    req = cursor.fetchall()
    cursor.close()
    conn.close()
    return req


def reqs():
    import pymysql
    conn = pymysql.connect(
        host= '127.0.0.1',
        user= 'root',password='123456',
        database= 'yu',
        charset= 'utf8')

    cursor = conn.cursor()
    sql = 'select * from js_numpy order by qh;'
    cursor.execute(sql)
    req = cursor.fetchall()
    cursor.close()
    conn.close()
    return req

def Q3():
    s = []
    for i in reqs():
        s.append(i[1])
    k = []
    for i in s:
        p = ''
        p += i[1]
        p += i[4]
        p += i[7]
        k.append(p)

    from collections import  Counter
    print(Counter(k))

def R5():
    s = []
    for i in reqs():
        s.append(i[1])
    k = []
    for i in s:
        try:
            p = ''
            p += i[1]
            p += i[4]
            p += i[7]
            p += i[10]
            p += i[13]
            k.append(p)
        except Exception as e:
            continue

    from collections import Counter
    print(Counter(k))

def one():

    our_query = []#取出每一个30期，合并成一个27万长度的列表
    new_30 = []#最新30期

    for query_new in reqs_30():
        new_30.append(query_new[1])
    print(new_30)

    req_s = reqs()
    for item in range(int(len(req_s)-29)):
        k = []
        el = {}
        ks = req_s[item:item+30]
        for i in ks:
            k.append(i[1])
        try:
            el = {'num':k,'lexqh':req_s[item+30][2],'lexnum':req_s[item+30][1]}
        except Exception as e:
            break
        our_query.append(el)
    num_q = []
    id = 0
    for items in our_query:  #循环取每一个30期
        my30fc = []
        num_fc = 0
        for x, y in zip(new_30,items['num']):#取两个30期中的同一期进行对比
            mywfc = 0
            x = x.split(',')
            y = y.split(',')
            for f,g in zip(x,y):
                if f == g:
                    mywfc += 0.2
            my30fc.append(mywfc)
        for i in my30fc:
            num_fc += (1-i)*(1-i)
        onefc = {'id': id, 'fc': num_fc / 30,'lexnum':items['lexnum'],'lexqh':items['lexqh']}
        id += 1
        num_q.append(onefc)
    import operator
    sorted_x = sorted(num_q, key=operator.itemgetter('fc'),reverse=False)
    p = 0
    for i in sorted_x:
        if p <4:
            print(i)
        else:
            break
        p += 1

one()





