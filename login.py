# login
# 2020/12/1
import requests
import hashlib
import pprint

HOST = 'http://121.41.14.39:8082/'
def get_md5(password):
    # 实例化加密对象
    md5 = hashlib.md5()
    # 进行加密操作
    md5.update(password.encode('utf-8'))
    # 返回机密后的值
    return md5.hexdigest()
# print(get_md5('90862'))

def login(inDate):
    '''
    :param inDate: 帐号密码----字典
    :return:
    '''
    # URL,请求地址
    url = f'{HOST}/account/sLogin'
    # 参入。入参
    # canshu = {'username':'dp0304','password':'948871c9b02dc17517ee3c9ee7dc3f09'}
    inDate['password'] = get_md5(inDate['password'])
    canshu = inDate
    # 请求方法
    resp = requests.post(url,data=canshu)
    # res = resp.json()
    # return res['data']['token']
    res = resp.text
    return res
if __name__ == '__main__':
    res = login({'username':'dp0304','password':'90862'})
    # pprint.pprint(res)
    print(res)