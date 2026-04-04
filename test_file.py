from xxx import add_mistake, view_mistakes

def test_add():
    add_mistake("1", "2", "3","blablabla")
    print("Add test")

def test_view():
    mistakes = view_mistakes()
    print("View test:", mistakes)

if __name__ == "__main__":
    test_add()
    test_view()
