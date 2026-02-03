class TestCase:

    def __init__(self, steps=None, result=None):
        self.steps = steps
        self.result = result
   
    def set_step(self, step_number, step_text):
        if self.steps is None:
            self.steps = {step_number: step_text}
        else:
            self.steps[step_number] = step_text

    def delete_step(self, step_number):
        if step_number in self.steps:
            del self.steps[step_number]
        else:
            print('Шаг не найден')

    def set_result(self, result):
        self.result = result

    def get_test_case(self):
        if self.steps is None:
            print('Тест-кейс создан')
        else:
            print(f'Шаги: {self.steps}, \nОжидаемый результат: {self.result}')


test_case_1 = TestCase()
test_case_1.set_step(1, 'Перейти на сайт')
test_case_1.set_step(3, 'Перейти в раздел Товары')
test_case_1.delete_step(3)
test_case_1.set_step(2, 'Перейти в раздел Товары')
test_case_1.set_step(3, 'Нажать кнопку «В корзину» у первого товара')
test_case_1.set_result('Товар окажется в корзине')
test_case_1.get_test_case()

test_case_2 = TestCase()
test_case_2.set_step(1, 'Перейти на сайт')
test_case_2.set_step(2, 'Перейти в раздел Корзина')
test_case_2.set_step(3, 'Нажать кнопку "Удалить"')
test_case_2.set_result('Товар удален из корзины')
test_case_2.get_test_case()