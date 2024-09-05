import pytest as pytest


# autouse=True 每个测试方法执行前自动调用该方法
@pytest.fixture(scope='function', autouse=True)
def fixture01():
    print('前置步骤1...')
    return 1


@pytest.fixture(scope='function')
def fixture02():
    print('前置步骤2...')
    return 2


@pytest.fixture(scope='function')
def fixture03():
    print('前置步骤3...')
    return 3


# 将fixture方法名写入测试方法形参中 fixture方法会按顺序先调用
def test_func01(fixture01, fixture02, fixture03):
    assert fixture01 == 1
    assert fixture02 == 2
    assert fixture03 == 3


def test_func02(fixture03):
    assert 1 == 1
    # 只有前置1 前置3
