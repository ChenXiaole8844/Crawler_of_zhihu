#!/usr/bin/env python
# coding: utf-8

# In[1]:


#!/usr/bin/env python
# coding: utf-8
import os
import pandas as pd
from selenium import webdriver
from lxml import etree
import time
import jieba
import re
import numpy as np


url1 = input("请输入您所需要爬取的网页（知乎）")

browser = webdriver.Chrome("/Users/apple/Downloads/chromedriver_mac_mac")
browser.get(url1)



try:
    #点击问题全部内容
    button1 = browser.find_elements_by_xpath("""//div[@class= "QuestionHeader-detail"]
    //button[contains(@class,"Button") and contains(@class,"QuestionRichText-more") 
    and contains(@class , "Button--plain")
    ]""")[0]
    button1.click()
except:
    print('这个问题比较简单，并没有问题的全部内容哦！')


#此网页就属于异步加载的情况
#那么我们就需要多次下滑
for i in range(20):
    browser.execute_script('window.scrollTo(0,document.body.scrollHeight)')
    time.sleep(0.5)
    print(i)

#点击知乎的登陆弹窗
button2 = browser.find_elements_by_xpath("""//button[@aria-label = '关闭']""")[0]
button2.click()    

# #点击知乎的“查看全部回答”按钮
# button3 = browser.find_elements_by_xpath("""//div[@class = 'Question-main']
# //a[contains(@class,"ViewAll-QuestionMainAction")    and contains(@class , "QuestionMainAction")  ]""")[1]
# button3.click()


final_end_it = browser.find_elements_by_xpath("""//button[contains(@class,"Button") 
and contains(@class ,'QuestionAnswers-answerButton')
and contains(@class ,'Button--blue')

and contains(@class ,'Button--spread')
]""")
while final_end_it == []:
    final_end_it = browser.find_elements_by_xpath("""//button[contains(@class,"Button") 
and contains(@class ,'QuestionAnswers-answerButton')
and contains(@class ,'Button--blue')

and contains(@class ,'Button--spread')
]""")
    js="var q=document.documentElement.scrollTop=0"  
    browser.execute_script(js)
    for i in range(30):
        browser.execute_script('window.scrollTo(0,document.body.scrollHeight)')
        time.sleep(0.5)
        print(i)


    # #定位按钮
    # #查看全部 6,376 个回答
    # #得到事件的具体描述，以及网友的评论文本（或许要？）
    # button = browser.find_elements_by_xpath("""//a[@class='load']""")[0]
    # button.click()


#应该在爬取的时候，进行存储，不然之后若是过多，会有事情的！可能会加载不出来？？


# In[ ]:



final_end_it = browser.find_elements_by_xpath("""//button[contains(@class,"Button") 
and contains(@class ,'QuestionAnswers-answerButton')
and contains(@class ,'Button--blue')

and contains(@class ,'Button--spread')
]""")
while final_end_it == []:
    final_end_it = browser.find_elements_by_xpath("""//button[contains(@class,"Button") 
and contains(@class ,'QuestionAnswers-answerButton')
and contains(@class ,'Button--blue')

and contains(@class ,'Button--spread')
]""")
    js="var q=document.documentElement.scrollTop=0"  
    browser.execute_script(js)
    for i in range(30):
        browser.execute_script('window.scrollTo(0,document.body.scrollHeight)')
        time.sleep(0.5)
        print(i)


    # #定位按钮
    # #查看全部 6,376 个回答
    # #得到事件的具体描述，以及网友的评论文本（或许要？）
    # button = browser.find_elements_by_xpath("""//a[@class='load']""")[0]
    # button.click()


#应该在爬取的时候，进行存储，不然之后若是过多，会有事情的！可能会加载不出来？？


# In[2]:


dom = etree.HTML(browser.page_source)


# # 对于问题本身的数据

# In[4]:


Followers_number_first = dom.xpath("""//div[@class="QuestionFollowStatus"]//div[@class = "NumberBoard-itemInner"]/strong/text()""")[0]
Browsed_number_first = dom.xpath("""//div[@class="QuestionFollowStatus"]//div[@class = "NumberBoard-itemInner"]/strong/text()""")[1]

#关注者数量
Followers_number_final = re.sub(",","",Followers_number_first)
#浏览数量
Browsed_number_final = re.sub(",","",Browsed_number_first)


#问题链接
problem_url =  url1

#问题ID

problem_id = re.findall(r"\d+\.?\d*",url1)

#问题标题
problem_title =  dom.xpath("""//div[@class = 'QuestionHeader']//h1[@class = "QuestionHeader-title"]/text()""")

#问题点赞数
problem_endorse = dom.xpath("""//div[@class = 'QuestionHeader']//div[@class = "GoodQuestionAction"]/button/text()""")
#问题评论数
problem_Comment = dom.xpath("""//div[@class = 'QuestionHeader']//div[@class = "QuestionHeader-Comment"]/button/text()""")

#问题回答数
answer_number = dom.xpath("""//div[@class = 'Question-main']//h4[@class = "List-headerText"]/span/text()""")

#问题标签
problem_tags_list = dom.xpath("""//div[@class = 'QuestionHeader-topics']//a[@class = "TopicLink"]/div/div/text()""")


# # 对于回答本身的数据

# In[5]:


#具体内容
comment_list = dom.xpath("""//div[@class = 'List-item']//div[@class = "RichContent-inner"]""")
comment_list_text = []
for comment in comment_list:
    comment_list_text.append(comment.xpath("string(.)"))
    
#发表时间

time_list = dom.xpath("""//div[@class = 'List-item']//div[@class = "ContentItem-time"]//span/@data-tooltip""")

edit_time_list = dom.xpath("""//div[@class = 'List-item']//div[@class = "ContentItem-time"]//span/text()""")


#点赞数

endorse_list = dom.xpath("""//div[@class = 'List-item']//button[contains(@class,"Button") and contains(@class,"VoteButton") and contains(@class , "VoteButton--up")]/@aria-label""")
#评论人数
number_of_endorse_list = dom.xpath("""//div[@class = 'List-item']//svg[contains(@class,"Zi")   and contains(@class,"Zi--Comment") 
and contains(@class,"Button-zi")]/../../text()""")




#回答链接
answers_url_list = dom.xpath("""//div[@class = 'List-item']//div[contains(@class,"ContentItem") and contains(@class,"AnswerItem")]
/meta[@itemprop = "url"]/@content""")


authors_list = dom.xpath("""//div[@class = 'List-item']//div[contains(@class,"ContentItem") and contains(@class,"AnswerItem")]
/@data-zop""")

#作者姓名
authorName_list = []
#作者id
authorid_list = []
for i in authors_list:
    authorName_list.append(eval(i)['authorName'])
    authorid_list.append(eval(i)["itemId"])


# # 合成数据框

# In[6]:


data = pd.DataFrame()

data['具体内容'] = comment_list_text
data["发表时间"] = time_list
data["点赞数"] = endorse_list
data["评论人数"] = number_of_endorse_list
data["回答链接"] = answers_url_list
data["作者姓名"]  = authorName_list
data['作者id'] = authorid_list


data["问题关注者数量"] = Followers_number_final
data["问题浏览数量"] = Browsed_number_final
data["问题链接"] = problem_url
data["问题ID"]  = problem_id[0]
data["问题标题"] = problem_title[0]
data["问题点赞数"] = problem_endorse[0]
data["问题评论数"] = problem_Comment[0]
data["问题回答数"] = answer_number[0]
data["问题标签"] = "&".join(problem_tags_list)


data


# # 数据预处理

# In[1]:


# import pandas as pd
# import re
# data  = pd.read_csv("排名在前 1% 的高中生是靠天赋还是靠努力？（知乎）.csv")


# In[5]:


# del data["Unnamed: 0"]


# In[7]:


def str_to_number(str1):
    mid = re.findall(r"\d+\.?\d*",str1)
    if mid != []:
        return mid[0]
    else:
        return 0
data["点赞数"] = data["点赞数"].apply(str_to_number)
data["评论人数"] = data["评论人数"].apply(str_to_number)
data["问题点赞数"] = data["问题点赞数"].apply(str_to_number)
data["问题评论数"] = data["问题评论数"].apply(str_to_number)
data["问题回答数"] = data["问题回答数"].apply(str_to_number)


# In[8]:


def time_to_datetime(x):
    x1 = re.sub('[\u4e00-\u9fa5]', '',x)
    if len(x1) < 15 :  
    #15的根据是data["发表时间_1"] = data["发表时间"].apply(lambda x : re.sub('[\u4e00-\u9fa5]', '',x))
    #data["发表时间_1"].apply(lambda x : len(x)).value_counts()
        x2 = re.sub(' ', '2020-',x1,count=1)
        return x2
    return x1
data["发表时间"] = data["发表时间"].apply(time_to_datetime)
data.sort_values('发表时间', inplace=True) 
data = data.reset_index(drop = True)
data


# In[9]:


data.to_csv("Zhihu_problem_data:{}.csv".format(data["问题标题"][0]) )


# In[10]:


data.iloc[1:2,:]


# In[13]:


data.shape


# In[ ]:




