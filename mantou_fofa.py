import pandas as pd

print("""\032[31m
================馒头出品=================
博客地址：https://www.cnblogs.com/mantou0/
\033[0m""")
f = open("fofa_语法.txt", 'w')


def mantou_beian():
    df = pd.read_excel('备案信息.xlsx', sheet_name='备案信息', usecols=[2])
    data = df.values
    lis_beian = []
    # fofa的备案信息转fofa
    for i in range(len(data)):
        if data[i] not in lis_beian:
            lis_beian.append(data[i][0])
    # 生成查询语句
    fofa_lis_beian = "利用备案信息来进行fofa查询：\n("
    for l in (lis_beian):
        fofa_lis_beian = fofa_lis_beian + '||icp="' + l + '"'
    fofa_lis_beian = fofa_lis_beian + ')&&header="200"\n\n'
    # 写入文件
    f.write(fofa_lis_beian)

def mantou_domain():
    df2 = pd.read_excel('备案信息.xlsx', sheet_name='备案信息', usecols=[1])
    data2 = df2.values
    lis_beian = []
    # fofa的备案信息转fofa
    for i in range(len(data2)):
        if data2[i] not in lis_beian:
            lis_beian.append(data2[i][0])
    # 生成查询语句
    fofa_lis_domain = "利用子域名进行fofa查询：\n("
    for l in (lis_beian):
        fofa_lis_domain = fofa_lis_domain + '||host="' + l + '"'
    fofa_lis_domain = fofa_lis_domain + ')&&header="200"\n\n'
    # 写入文件
    f.write(fofa_lis_domain)


if __name__ == '__main__':
    print("fofa语句正在生成.......")
    mantou_beian()
    mantou_domain()
    print("fofa语句生成完毕，请在fofa_语法.txt中查看")
    f.close()
