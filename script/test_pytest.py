import allure


class TestLogin:
    def test_a(self):
        print('\n aaa')
        assert 1
    @allure.step('测试描述步骤')
    def test_b(self):

        print('\n bbb')
        allure.attach('描述1','请输入用户名:')
        print('\n ccc')
        allure.attach('描述1','请输入密码:')
        assert 0