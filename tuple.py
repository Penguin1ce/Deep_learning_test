# 字典
# 键 值   元组
slang_dict = {
    "觉醒年代": "一部热门电影",
    "YYDS": "很厉害的意思",
}
slang_dict["双减"] = "根据教育部指示，减少作业"
query = input("请输入你想查询的流行语：")
if query in slang_dict:
    print("你查询的" + query + "含义如下")
    print(slang_dict[query])
    print("当前本词典收录词条数为：" + str(len(slang_dict)))
else:
    print("您查询的流行语暂未收录。")
    print("当前本词典收录词条数为：" + str(len(slang_dict)))

# This is my first Python
get_url = "http://1147129830@qq.com"
print(get_url.removeprefix("http://"))
new_url = get_url.removeprefix("http://")
print(new_url)
name = ["a", "b", "c", "d", "e"]
print(name[0])
