# Selenium UI 自动化测试框架（基于 python 3）
## 框架目录构造： ##


- **[config]()**： 用来存储配置文件和浏览器的 element，如 [config.ini]() 文件，配置了所需浏览器方式及被测地址

- **[data]()**：用来实现 ddt 数据驱动的账号数据文件

- **[framework]()**：框架底层封装层，可以根据自己的想法封装底层方法
  - *[logger.py]()*：封装了日志输入，包括文件输出和控制台的输出
  - *[base_page]()*：封装了 selenium 库中常用的方法，包括对象查找，截图输出，浏览器的前进后退，清除和输入等
  - *[browser_engine]()*：通过读取配置文件去选择浏览器和 url，并返回浏览器对象实例
  - *[browser_info]()*：得到浏览器的配置和 url

- **[screenshots]()**：用于接收测试过程中错误截图文件

- **[logs]()**：用于接收日志文件的输出 

- **[page_objects]()**：用于封装页面对象

- **[Python_HTMLTestReportCN]()**：生成自动化测试报告网页html

- **[test_report]()**：用于接收测试报告文件的输出

- **[test_suites]()**：用于测试用例的存放和用例集合套件

- **[tools]()**：用于存放浏览器的 selenium 驱动

