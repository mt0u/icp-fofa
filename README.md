# icp-fofa

1、将要查询的公司名称或者网址放进mm.txt

2、生成备案信息---->生成文件	备案信息.xlsx

3、生成fofa语句----->生成文件 mm_fofa_语法.txt

4、复制fofa语法去fofa采集器去下载数据

5、然后用漏洞扫描器去跑

注意：如果不想再原本的基础上添加内容，请将 备案信息.xlsx 删除


可以输入一个或多个公司名或域名，得到备案信息，转为fofa语句，供你查询

必要库
opencv_python==4.5.5.64

openpyxl==3.0.9

requests==2.26.0

pandas



照片展示：
![image](https://user-images.githubusercontent.com/88358139/186873882-05dca86a-a1c0-4d27-9a1f-571fc5afbded.png)
![image](https://user-images.githubusercontent.com/88358139/186873913-26429dd1-b726-449d-9097-1be714e596f6.png)
![image](https://user-images.githubusercontent.com/88358139/186873933-ac097bc3-9315-4646-be9f-dd3f8d9846c6.png)




再注：这是简单修改了另一位师傅的代码，使其可以进行批量的备案查询

核心代码来自：https://github.com/wongzeon/ICP-Checker
