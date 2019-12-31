#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
@Time    : 2019/8/8 17:45
@Author  : Careslten
@Site    : 
@File    : js_new.py
@Software: PyCharm
'''

import requests,re,os,time
from bs4 import BeautifulSoup
import time
import json

class our_kJ():

    def __init__(self):
        self.times = time.strftime("%Y-%m-%d", time.localtime(time.time()))
        rs = requests.get('https://info.sporttery.cn/football/match_result.php?page=1&search_league=0&start_date='+self.times+'&end_date='+self.times+'&dan=0')
        rs.encoding = rs.apparent_encoding
        htmls = rs.text
        soup = BeautifulSoup(htmls, 'html.parser')
        liList = re.findall(r'<li[^>]*>(.*?)</li>', htmls, re.I | re.M)

        company_name = soup.find_all('li', class_=re.compile("u-result"))[0].find('span').text
        self.list_len = int(int(company_name) / 30) + 1

    def get_code(self):

        our_list = []
        company_name = ''
        for i in range(self.list_len):
            # urls = 'https://info.sporttery.cn/football/match_result.php?page='+str(i+1)+'&search_league =0&start_date =2019-08-01&end_date=2019-08-31&dan=0'
            urls = 'https://info.sporttery.cn/football/match_result.php?page='+str(i+1)+'&search_league=0&start_date='+self.times+'&end_date='+self.times+'&dan=0'
            r = requests.get(urls)
            r.encoding = r.apparent_encoding
            html = r.text
            soup = BeautifulSoup(html,'html.parser')
            company_name = soup.find_all('li',class_=re.compile("u-result"))[0].find('span').text
            tdList = re.findall(r'<td[^>]*>(.*?)</td>', html, re.I | re.M)
            for s in tdList:
                if 'span' in s:
                    s = re.findall(r'<span[^>]*>(.*?)</span>', s, re.I | re.M)
                if '<a' in s:
                    s = re.findall(r'<a[^>]*>(.*?)</a>', s, re.I | re.M)
                if isinstance(s,list):
                    if s[0] == '赛事选择':
                        continue
                our_list.append(s)
        # ourlists = self.div_list(our_list,int(company_name))
        # ourlists = self.list_of_groups(our_list,12)
        ourlists = self.test2(our_list,12)
        print(len(our_list),len(ourlists))
        for i in ourlists:
            print(i)
        return ourlists

    def div_list(self,ls, n):
        if not isinstance(ls, list) or not isinstance(n, int):
            return []
        ls_len = len(ls)
        if n <= 0 or 0 == ls_len or n > ls_len:
            return []
        elif n == ls_len:
            return [[i] for i in ls]
        else:
            j = ls_len // n
            k = ls_len % n
            ### j,j,j,...(前面有n-1个j),j+k
            # 步长j,次数n-1
            ls_return = []
            for i in range(0, int((n - 1) * j), int(j)):
                ls_return.append(ls[i:i + j])
            # 算上末尾的j+k
            ls_return.append(ls[(n - 1) * j:])
            return ls_return

    def list_of_groups(self,our_list, children_list_len):
        list_of_groups = zip(*(iter(our_list),) * children_list_len)
        end_list = [list(i) for i in list_of_groups]
        count = len(our_list) % children_list_len
        end_list.append(our_list[-count:]) if count != 0 else end_list
        return end_list

    def test1(self,one_data_list, colnum):
        '''
        将一维的列表转化为矩阵形式
        '''
        res_list = []
        for i in range(0, len(one_data_list), colnum):
            res_list.append(one_data_list[i:i + colnum])
        return res_list

    def test2(self,one_list, c):
        '''
        将一个长度为n的列表划分 ，每个子列表中包含m个元素
        '''
        return [one_list[i:i + c] for i in range(len(one_list)) if i % c == 0]




    def Victory_and_defeat(self):
        #获取ID及队伍等信息
        url = 'https://i.sporttery.cn/odds_calculator/get_odds?i_format=json&i_callback=getData&poolcode[]=hhad&poolcode[]=had&_='
        r =requests.get(url)
        response = eval(r.text[8:-2])['data']
        query = []
        query_id = []
        #对数据进行处理
        for key,value in response.items():
            query.append(value)
        for item in query:
            query_id.append(item['id'])

        #一个不知道用来干什么的沙雕接口
        urls = 'https://i.sporttery.cn/api/gsm_league_show/get_show_switch?f_callback=jQuery1706251486117428731_1569307343097'
        for items_id in query_id:
            urls = urls + '&spmid[]='+str(items_id)
        rs =requests.get(urls)
        response_end = eval(rs.text[40:-2])['result']

        #获取胜平负赔率等信息
        Odds_url = 'https://i.sporttery.cn/odds_calculator/get_proportion?i_format=json&pool[]=had&pool[]=hhad&i_callback=getReferData1&_=1569309105579'
        rq = requests.get(Odds_url)
        response_odds = eval(rq.text[14:-2])['data']
        odds = []
        for key,value in response_odds.items():
            odds.append(value)

        #完整胜平负数据
        s = 0
        for num in range(len(query)):
            #有时会空指针报错，且需要过滤掉odd整个没有的情况
            try:
                if query[num]['id'] ==odds[s]['had']['mid']:
                    query[num]['odds'] = odds[s]
                    s += 1
                else:
                    query[num]['odds'] = {}
            except Exception as e:
                if query[num]['id'] ==odds[s]['hhad']['mid']:
                    query[num]['odds'] = odds[s]
                    s += 1
                else:
                    query[num]['odds'] = {}


        backQueryList = []
        for i in query:
            backQuery = {}
            backQuery['id'] = i['id']#mid
            backQuery['num'] = i['num']#赛事编号
            backQuery['match_date'] = i['date']#比赛日期
            backQuery['b_date'] = i['b_date']#所属日期
            backQuery['l_cn_abbr'] = i['l_cn_abbr']#赛事名称
            backQuery['h_order'] = i['h_order']#主队前缀
            backQuery['h_cn_abbr'] = i['h_cn_abbr']#主队队名
            backQuery['a_order'] = i['a_order']#客队前缀
            backQuery['a_cn_abbr'] = i['a_cn_abbr']#客队队名
            backQuery['fixedodds'] = i['hhad']['fixedodds']#让球数
            backQuery['h2'] = i['hhad']['a']#让球负赔率
            backQuery['d2'] = i['hhad']['d']#让球平赔率
            backQuery['a2'] = i['hhad']['h']#让球胜赔率

            #部分返回数据没有had（不让球数据，会显示未开售）
            imss = []
            for im in i:
                imss.append(im)
            if 'had'in imss:
                backQuery['single'] = i['had']['single']  # 是否单关
                backQuery['h1'] = i['had']['a']  # 不让球负赔率
                backQuery['d1'] = i['had']['d']  # 不让球平赔率
                backQuery['a1'] = i['had']['h']  # 不让球胜赔率

            else:
                backQuery['single'] = ''  # 是否单关
                backQuery['h1'] =''  # 不让球负赔率
                backQuery['d1'] =''  # 不让球平赔率
                backQuery['a1'] =''  # 不让球胜赔率

            #部分数据没有odds，或者没有had，需要过滤
            ims = []
            for im in i['odds']:
                ims.append(im)
            if 'had' in ims:
                backQuery['pre_win'] = i['odds']['had']['pre_win']  # 不让球胜
                backQuery['pre_lose'] = i['odds']['had']['pre_lose']  # 不让球负
                backQuery['pre_draw'] = i['odds']['had']['pre_draw']  # 不让球平
            else:
                backQuery['pre_win'] = ''
                backQuery['pre_lose'] =''
                backQuery['pre_draw'] =''

            if 'hhad' in ims:
                backQuery['ot_win'] = i['odds']['hhad']['pre_win']
                backQuery['ot_lose'] = i['odds']['hhad']['pre_lose']
                backQuery['ot_draw'] = i['odds']['hhad']['pre_draw']
            else:
                backQuery['ot_win'] = ''
                backQuery['ot_lose'] = ''
                backQuery['ot_draw'] = ''
            #生成使用数据列表！
            backQueryList.append(backQuery)
        return backQueryList


    #比分
    def score(self):
        h_url = 'https://i.sporttery.cn/odds_calculator/get_odds?i_format=json&i_callback=getData&poolcode[]=crs&_=1569380753301'
        h_r = requests.get(h_url)
        h_response = eval(h_r.text[8:-2])
        h_query = []
        for key, value in h_response['data'].items():
            h_query.append(value)

        t_url = 'https://i.sporttery.cn/odds_calculator/get_proportion?i_format=json&pool[]=had&pool[]=hhad&i_callback=getReferData1&_=1569380753690'
        t_r = requests.get(t_url)
        t_response = eval(t_r.text[14:-2])
        t_query = []
        for key, value in t_response['data'].items():
            t_query.append(value)

        s = 0
        for num in range(len(h_query)):
            #有时会空指针报错，且需要过滤掉odd整个没有的情况
            try:
                if h_query[num]['id'] ==t_query[s]['had']['mid']:
                    h_query[num]['odds'] = t_query[s]
                    s += 1
                else:
                    h_query[num]['odds'] = {}
            except Exception as e:
                if h_query[num]['id'] ==t_query[s]['hhad']['mid']:
                    h_query[num]['odds'] = t_query[s]
                    s += 1
                else:
                    h_query[num]['odds'] = {}
        backQueryList = []
        for i in h_query:
            backQuery = {}
            backQuery['id'] = i['id']#ID
            backQuery['num'] = i['num']#比赛编号
            backQuery['date'] = i['date']#比赛日期
            backQuery['time'] = i['time']#比赛时间
            backQuery['b_date'] = i['b_date']#可买日期
            backQuery['l_cn_abbr'] = i['l_cn_abbr']#赛事简称
            backQuery['h_order'] = i['h_order']#主队编号
            backQuery['h_cn_abbr'] = i['h_cn_abbr']#主队简称
            backQuery['a_order'] = i['a_order']#客队编号
            backQuery['a_cn_abbr'] = i['a_cn_abbr']#客队简称
            backQuery['single'] = i['crs']['single']#是否单关
            backQuery['crs'] = i['crs']#比分赔率-all
            if i['odds'] == {}:
                backQuery['_w'] = ''
                backQuery['_d'] = ''
                backQuery['_l'] = ''
            else:
                backQuery['_w'] = i['odds']['had']['pre_win']#胜支持率
                backQuery['_d'] = i['odds']['had']['pre_draw']#平支持率
                backQuery['_l'] = i['odds']['had']['pre_lose']#负支持率
            backQueryList.append(backQuery)
        return backQueryList

    #总进球数
    def goalNumber(self):
        h_url = 'https://i.sporttery.cn/odds_calculator/get_odds?i_format=json&i_callback=getData&poolcode[]=ttg&_=1569385274587'
        h_r = requests.get(h_url)
        h_response = eval(h_r.text[8:-2])
        h_query = []
        for key, value in h_response['data'].items():
            h_query.append(value)

        t_url = 'https://i.sporttery.cn/odds_calculator/get_proportion?i_format=json&pool[]=had&pool[]=hhad&i_callback=getReferData1&_=1569385275021'
        t_r = requests.get(t_url)
        t_response = eval(t_r.text[14:-2])
        t_query = []
        for key, value in t_response['data'].items():
            t_query.append(value)

        s = 0
        for num in range(len(h_query)):
            #有时会空指针报错，且需要过滤掉odd整个没有的情况
            try:
                if h_query[num]['id'] ==t_query[s]['had']['mid']:
                    h_query[num]['odds'] = t_query[s]
                    s += 1
                else:
                    h_query[num]['odds'] = {}
            except Exception as e:
                if h_query[num]['id'] ==t_query[s]['hhad']['mid']:
                    h_query[num]['odds'] = t_query[s]
                    s += 1
                else:
                    h_query[num]['odds'] = {}
        backQueryList = []
        for i in h_query:
            backQuery = {}
            backQuery['id'] = i['id']#ID
            backQuery['num'] = i['num']#比赛编号
            backQuery['date'] = i['date']#比赛日期
            backQuery['time'] = i['time']#比赛时间
            backQuery['b_date'] = i['b_date']#可买日期
            backQuery['l_cn_abbr'] = i['l_cn_abbr']#赛事简称
            backQuery['h_order'] = i['h_order']#主队编号
            backQuery['h_cn_abbr'] = i['h_cn_abbr']#主队简称
            backQuery['a_order'] = i['a_order']#客队编号
            backQuery['a_cn_abbr'] = i['a_cn_abbr']#客队简称
            backQuery['single'] = i['ttg']['single']#是否单关
            backQuery['e0'] = i['ttg']['s0']#比分赔率0
            backQuery['e1'] = i['ttg']['s1']  # 比分赔率-1
            backQuery['e2'] = i['ttg']['s2']  # 比分赔率-2
            backQuery['e3'] = i['ttg']['s3']  # 比分赔率-3
            backQuery['e4'] = i['ttg']['s4']  # 比分赔率-4
            backQuery['e5'] = i['ttg']['s5']  # 比分赔率-5
            backQuery['e6'] = i['ttg']['s6']  # 比分赔率-6
            backQuery['e7'] = i['ttg']['s7']  # 比分赔率-7
            if i['odds'] == {}:
                backQuery['_w'] = ''
                backQuery['_d'] = ''
                backQuery['_l'] = ''
            else:
                backQuery['_w'] = i['odds']['had']['pre_win']#胜支持率
                backQuery['_d'] = i['odds']['had']['pre_draw']#平支持率
                backQuery['_l'] = i['odds']['had']['pre_lose']#负支持率
            backQueryList.append(backQuery)
        for i in backQueryList:
            print(i)
        return backQueryList

    # 半全场胜平负
    def half_court_to_w_l(self):
        h_url = 'https://i.sporttery.cn/odds_calculator/get_odds?i_format=json&i_callback=getData&poolcode[]=hafu&_=1569393173570'
        h_r = requests.get(h_url)
        h_response = eval(h_r.text[8:-2])
        h_query = []
        for key, value in h_response['data'].items():
            h_query.append(value)

        t_url = 'https://i.sporttery.cn/odds_calculator/get_proportion?i_format=json&pool[]=had&pool[]=hhad&i_callback=getReferData1&_=1569393173851'
        t_r = requests.get(t_url)
        t_response = eval(t_r.text[14:-2])
        t_query = []
        for key, value in t_response['data'].items():
            t_query.append(value)

        s = 0
        for num in range(len(h_query)):
            # 有时会空指针报错，且需要过滤掉odd整个没有的情况
            try:
                if h_query[num]['id'] == t_query[s]['had']['mid']:
                    h_query[num]['odds'] = t_query[s]
                    s += 1
                else:
                    h_query[num]['odds'] = {}
            except Exception as e:
                if h_query[num]['id'] == t_query[s]['hhad']['mid']:
                    h_query[num]['odds'] = t_query[s]
                    s += 1
                else:
                    h_query[num]['odds'] = {}
        backQueryList = []
        for i in h_query:
            backQuery = {}
            backQuery['id'] = i['id']  # ID
            backQuery['num'] = i['num']  # 比赛编号
            backQuery['date'] = i['date']  # 比赛日期
            backQuery['time'] = i['time']  # 比赛时间
            backQuery['b_date'] = i['b_date']  # 可买日期
            backQuery['l_cn_abbr'] = i['l_cn_abbr']  # 赛事简称
            backQuery['h_order'] = i['h_order']  # 主队编号
            backQuery['h_cn_abbr'] = i['h_cn_abbr']  # 主队简称
            backQuery['a_order'] = i['a_order']  # 客队编号
            backQuery['a_cn_abbr'] = i['a_cn_abbr']  # 客队简称
            backQuery['single'] = i['hafu']['single']  # 是否单关
            backQuery['ss'] = i['hafu']['hh']  # 比分赔率-胜胜
            backQuery['sp'] = i['hafu']['hd']  # 比分赔率-胜平
            backQuery['sf'] = i['hafu']['ha']  # 比分赔率-胜负
            backQuery['ps'] = i['hafu']['dh']  # 比分赔率-平胜
            backQuery['pp'] = i['hafu']['dd']  # 比分赔率-平平
            backQuery['pf'] = i['hafu']['da']  # 比分赔率-平负
            backQuery['fs'] = i['hafu']['ah']  # 比分赔率-负胜
            backQuery['fp'] = i['hafu']['ad']  # 比分赔率-负平
            backQuery['ff'] = i['hafu']['aa']  # 比分赔率-负负
            if i['odds'] == {}:
                backQuery['_w'] = ''
                backQuery['_d'] = ''
                backQuery['_l'] = ''
            else:
                backQuery['_w'] = i['odds']['had']['pre_win']  # 胜支持率
                backQuery['_d'] = i['odds']['had']['pre_draw']  # 平支持率
                backQuery['_l'] = i['odds']['had']['pre_lose']  # 负支持率
            backQueryList.append(backQuery)
        for i in backQueryList:
            print(i)
        return backQueryList

    #14场胜负/任选9场
    def win_Lo_14(self,num):
        r_url = 'https://i.sporttery.cn/wap/fb_lottery/fb_lottery_match?key=wilo&num='+str(num)+'&f_callback=getDataBack&_=1569397288277'
        r_r = requests.get(r_url)
        r_response = eval(r_r.text[12:-2])['result']
        mid = []
        r_query = []
        for key,value in r_response.items():
            r_query.append(value)
        for item in r_query:
            try:
                mid.append(item['mid'])
            except:
                mid.append('')

        h_url = 'https://i.sporttery.cn/wap/fb_lottery/fb_odds_his?f_callback=jQuery1701649920211356397_1569397288270'
        for items_id in mid:
            h_url = h_url + '&mid[]=' + str(items_id)
        rs = requests.get(h_url)
        try:
            h_query = eval(rs.text[40:-2])['result']
        except:
            h_query = {}

        time_url = 'https://i.sporttery.cn/wap/fb_lottery/fb_lottery_nums?key=wilo&num='+str(num)+'&f_callback=getNumBack&_=1569397288461'
        time_r = requests.get(time_url)
        time_response = eval(time_r.text[11:-2])['result']

        for item in range(len(r_query)) :
            try:
                r_query[item]['odds'] = h_query[r_query[item]['mid']]
            except:
                r_query[item]['odds'] = ''

        backQueryList = []
        for i in r_query:
            print(i)
            backQuery = {}
            try:
                backQuery['id'] = i['mid']  # mid
            except:
                backQuery['id'] = ''
            backQuery['league'] = i['league']  # 所属赛事
            backQuery['a_cn'] = i['a_cn']  # 客队
            backQuery['h_cn'] = i['h_cn']  # 主队
            backQuery['date'] = i['date']  # 时间

            backQuery['s_jj'] = i['h']  #胜奖金
            backQuery['p_jj'] = i['d']  #平奖金
            backQuery['l_jj'] = i['a']  #负奖金
            backQueryList.append(backQuery)
        print({'backQuery':backQueryList,'time':time_response})
        return {'backQuery':backQueryList,'time':time_response}


if __name__ == '__main__':
    x = our_kJ()
    x.win_Lo_14(19130)