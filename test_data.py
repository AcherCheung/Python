import pytest
import yaml


class Test_demo:
    @pytest.mark.parametrize("env", yaml.safe_load(open("./a/env.yml")))
    def test_switchenv(self, env):
        if "test" in env:
            print('this is test enverionment')
        elif "product" in env:
            print('this is product environment')


def test_a():  # test开头的测试函数
    print("------->test_a")
    assert 1  # 断言成功


def test_b():
    print("------->test_b")
    assert 0  # 断言失败


if __name__ == '__main__':
       pytest.main(["-s","test_data.py"])  # 调用pytest的main函数执行测试

