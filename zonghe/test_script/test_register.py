'''
注册的测试脚本
'''

# 注册失败的测试脚本
import pytest
# pytest数据驱动的方式
from zonghe.baw import Member, Db
from zonghe.caw import DataRead
@pytest.fixture(params=DataRead.read_yaml(r"data_case\register_fail.yaml"))
def fail_data(request):
    print(request.param)
    return request.param
@pytest.fixture(params=DataRead.read_yaml(r"data_case\register_pass.yaml"))
def pass_data(request):
    print(request.param["data"])
    return request.param
@pytest.fixture(params=DataRead.read_yaml(r"data_case\repeat.yaml"))
def repeat_data(request):
    return request.param
def test_register_fail(url,baserequests,fail_data):
    # 下发注册请求
    r = Member.register(url,baserequests,fail_data["data"])
    # 断言结果
    print(r.text)
def test_register_pass(url,baserequests,pass_data):
    # 下发注册请求
    r = Member.register(url,baserequests,pass_data["data"])
    # 断言结果
    print(r.text)

def test_repeat(url,baserequests,repeat_data,db):
    Db.delete_user(db, str(repeat_data['data']['mobilephone']))
    r = Member.register(url, baserequests, repeat_data['data'])
    print(r.text)
    r = Member.register(url, baserequests, repeat_data['data'])
    print(r.text)
def test_delete_user(url,baserequests,pass_data,db):
    Db.delete_user(db,'13689105274')
