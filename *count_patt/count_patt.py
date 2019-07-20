'用于统计一个文件中某些字段出现的次数'
import re

def count_patt(fname, patt):
    patt_dict = {}
    cpatt = re.compile(patt)   #将patt编译,后面匹配更方便

    with open(fname) as fobj:
        for line in fobj:
            m = cpatt.search(line)  #匹配的模式
            if m:       # 如果匹配不到返回None，表示False,匹配到了，是True
                key = m.group()
                # 模式不在字典中，计数1，在字典中，加1
                patt_dict[key] = patt_dict.get(key, 0) + 1
                # if key not in patt_dict:  #如果key是第一次出现,则值为1
                #     patt_dict[key] = 1
                # else:
                #     patt_dict[key] += 1   #如果key之前存在,则值加1

    return patt_dict

if __name__ == '__main__':
    fname = 'access_log'
    ip = '^(\d+\.){3}\d+'   #正则匹配
    br = 'Firefox|MSIE|Chrome'
    ip_count = count_patt(fname, ip)
    br_count = count_patt(fname, br)
    print(ip_count)
    print(br_count)
