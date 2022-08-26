# icp-fofa
输入公司名或域名，得到备案信息，转为fofa语句，供你查询

必要库
opencv_python==4.5.5.64
openpyxl==3.0.9
requests==2.26.0
pandas

1、将要查询的公司名称或者网址放进mm.txt
2、生成备案信息---->生成文件	备案信息.xlsx
3、生成fofa语句----->生成文件 mm_fofa_语法.txt
4、复制fofa语法去fofa采集器去下载数据
5、然后用漏洞扫描器去跑

注意：如果不想再原本的基础上添加内容，请将 备案信息.xlsx 删除
