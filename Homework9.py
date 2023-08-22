class MyData:
    def __init__(self, value):
        self.value = value

    def instance_method(self):
        return f"Instance Method: {self.value}"

    @staticmethod
    def static_method():
        return "Static Method"

    @classmethod
    def class_method(cls):
        return f"Class Method: {cls.__name__}"


data_obj = MyData(33)
print(data_obj.instance_method())  # Вызов обычного метода объекта
print(MyData.static_method())  # Вызов статического метода класса
print(MyData.class_method())  # Вызов классового метода класса
