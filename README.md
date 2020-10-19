# Crawler_of_zhihu
唯一需要修改的地方是browser = webdriver.Chrome("/Users/apple/Downloads/chromedriver_mac_mac") 这里的地址改成你自己chromedriver的地址


运行代码之后，输入你所要爬的网站的url，例如：https://www.zhihu.com/question/288647309/answer/875598429
运行代码，坐等csv格式的文件，如：上述url对应的文件为：Zhihu_problem_data:有大神会爬知乎的数据吗？.csv
（这是这个问题的回答，我只是个卑微的普通学生，并非大神/哭）

我这里给了两个数据，一个是Zhihu_problem_data:有大神会爬知乎的数据吗？.csv，
另一个是我最近爬的关于“如何看待导演张策不再担任《朱一旦枯燥生活》的导演？对于双方来说，是双赢还是双输？”这个问题的一些评论（大概400多条）

这个代码其实从效率方面还是有待改善的，欢迎大家提出一些建议。
