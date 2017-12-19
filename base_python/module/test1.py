__all__ = ["test11"]
def test11():
    print("这是test1.py里面的test11函数")

# test11()
def test12():
    print("test12")
if __name__ == "__main__":
    test11()

# 如果不想别人引用你这个模块时使用某个值，则可以用__all__，只有在这个里面写过的才能用。