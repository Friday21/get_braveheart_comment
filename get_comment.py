# -*- coding: utf-8
import requests
import re
import json
directory = '/root/blog_flask/my_spirit_home/static/'
filename = directory + 'comment.json'

def countdown():
    headers = {
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding':'gzip, deflate, sdch',
    'Accept-Language':'zh-CN,zh;q=0.8,en;q=0.6',
    'Cache-Control':'max-age=0',
    'Connection':'keep-alive',
    'Cookie':'main[UTMPUSERID]=Friday21; main[UTMPKEY]=42578814; main[UTMPNUM]=19282; main[PASSWORD]=rHf%2503Wqx%255C%2507%255BZ%250EP_D%251C%25047N%25107F%255E%250C; main[XWJOKE]=hoho; Hm_lvt_9c7f4d9b7c00cb5aba2c637c64a41567=1494810275,1494893271,1494919029,1494985588; Hm_lpvt_9c7f4d9b7c00cb5aba2c637c64a41567=1494987216',
    'Host':'www.newsmth.net',
    'If-Modified-Since':'Wed, 17 May 2017 02:17:11 GMT',
    'Upgrade-Insecure-Requests':'1',
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
    }

    people_str = """高雨浩 http://www.newsmth.net/nForum/#!article/BraveHeart/1667497873
    涂江汇 http://www.newsmth.net/nForum/#!article/BraveHeart/1667497896
    张华枫 http://www.newsmth.net/nForum/#!article/BraveHeart/1667497879
    李东勇 http://www.newsmth.net/nForum/#!article/BraveHeart/1667497880
    赵超 http://www.newsmth.net/nForum/#!article/BraveHeart/1667497874
    徐小斌 http://www.newsmth.net/nForum/#!article/BraveHeart/1667497875
    王龙泽 http://www.newsmth.net/nForum/#!article/BraveHeart/1667497876
    林健夫 http://www.newsmth.net/nForum/#!article/BraveHeart/1667497878
    曽峰 http://www.newsmth.net/nForum/#!article/BraveHeart/1667497881
    王高远 http://www.newsmth.net/nForum/#!article/BraveHeart/1667497882
    叶一锰 http://www.newsmth.net/nForum/#!article/BraveHeart/1667497883
    李丰果 http://www.newsmth.net/nForum/#!article/BraveHeart/1667497884
    孙搏谦 http://www.newsmth.net/nForum/#!article/BraveHeart/1667497885
    罗文宇 http://www.newsmth.net/nForum/#!article/BraveHeart/1667497886
    陈建凤 http://www.newsmth.net/nForum/#!article/BraveHeart/1667497887
    王寿文 http://www.newsmth.net/nForum/#!article/BraveHeart/1667497888
    杨昕 http://www.newsmth.net/nForum/#!article/BraveHeart/1667497889
    胡传鹏 http://www.newsmth.net/nForum/#!article/BraveHeart/1667497890
    张迅 http://www.newsmth.net/nForum/#!article/BraveHeart/1667497891
    高晓禾 http://www.newsmth.net/nForum/#!article/BraveHeart/1667497892
    唐科 http://www.newsmth.net/nForum/#!article/BraveHeart/1667497893
    舒洁 http://www.newsmth.net/nForum/#!article/BraveHeart/1667497894
    袁梦 http://www.newsmth.net/nForum/#!article/BraveHeart/1667497895
    王阳阳.2017 http://www.newsmth.net/nForum/#!article/BraveHeart/1667498016
    伍震环 http://www.newsmth.net/nForum/#!article/BraveHeart/1667497948
    何茂藤 http://www.newsmth.net/nForum/#!article/BraveHeart/1667497949
    宋梦迪 http://www.newsmth.net/nForum/#!article/BraveHeart/1667498516"""

    people_new_list = people_str.split('\n')
    people_list = list()
    for people in people_new_list:
        url = 'http://www.newsmth.net/nForum/article/BraveHeart/' + people.split(' ')[-1][-10:] + '?ajax&p=10'
        people_list.append(dict(name=people.split(' ')[-2], link=people.split(' ')[-1], url=url))
    session = requests.session()
    comment_list = list()
    for people in people_list:
        session.get(people['link'], headers=headers)
        print people['url']
        r = session.get(people['url'])
        pattern = """<p>发信人: (.*?), 信区: BraveHeart <br /> 标&nbsp;&nbsp;题: Re: 【毕业纪念册】征文——.*? <br /> 发信站: 水木社区 (.*?), 站内 <br />&nbsp;&nbsp;<br /> (.*?)<br />&nbsp;&nbsp;<br />"""
        response = r.text
        response = response.encode('UTF-8')
        comment = re.findall(pattern, response)
        if not comment:
            continue
        comment_list.append(dict(author=people['name'], commenter=comment[-1][0], comment_time=comment[-1][1],
                                 comment_content=comment[-1][2].decode('utf8')[0:200].encode('utf8')+'......'))
    json_content = json.dumps(comment_list)
    file = open(filename,'w')
    file.write(json_content)
    file.close()
countdown()
