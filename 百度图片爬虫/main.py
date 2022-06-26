import requests
import re
import os


image_name = input('输入爬取的图片名称:')
image_num = input('请输入爬取图片张数:')
# image_name = '蕾姆2'
# image_num = 100
while True:
    try:
        image_num = int(image_num)
        break
    except ValueError:
        print('请输入正确个数')
        image_num = input('请输入爬取图片张数:')

if not os.path.exists('./%s/' % image_name):
    os.mkdir('./%s/' % image_name)

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/102.0.0.0 Safari/537.36'}

saved_image_list = []
not_stop = True
counter = 1
current_num = 1
limit_num = 1
while not_stop:
    url = 'https://image.baidu.com/search/flip?tn=baiduimage&ie=utf-8&word='+image_name+'&pn='+str(counter+current_num)
    res = requests.get(url, headers=headers)
    total_find_result = int("".join(re.findall(r'\d+', re.findall(r"找到相关图片(.*?)张", res.content.decode())[0])))
    ind_image_address = re.findall('"objURL":"(.*?)",', res.content.decode())

    for i in ind_image_address:
        img = requests.get(i)
        if img.content not in saved_image_list:
            saved_image_list.append(img.content)

            with open('./%s/%s.jpg' % (image_name, current_num), 'ab') as f:
                f.write(img.content)

            print('---------第' + str(current_num) + '张图片下载完毕----------')
            current_num += 1
            if current_num >= image_num + 1:
                not_stop = False
                break
        limit_num += 1

    counter += 1
    if current_num >= image_num + 1 or limit_num >= total_find_result - 1:
        not_stop = False
        break
