# -*-coding:UTF-8-*-

"""
定义和使用字典
"""


def main():
    score = {"罗浩": 95, "百源芳": 98, "狄仁杰": 54}
    print(score['罗浩'])
    print(score['百源芳'])
    # elem 获取的是key， score[elem]获取到的是value
    for elem in score:
        print('%s\t -->\t%d' % (elem, score[elem]))
    score['百源芳'] = 96
    score['诸葛王朗'] = 100
    score.update(冷面=67, 放弃核=85)
    print(score)
    # 判断武则天是否存在，第一次输出为空，第二次进行添加
    if '武则天' in score:
        print(score['武则天'])
    print(score.get('武则天'))
    print(score.get('武则天', 60))
    # popitem 是删除最后一个
    print(score.popitem())
    print(score.popitem())
    # pop 指定删除的key
    print(score.pop('罗浩'))
    score.clear()
    print(score)


if __name__ == "__main__":
    main()
