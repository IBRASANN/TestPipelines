def add(a, b):
    return a + b

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0
    assert add(-2, -3) == -5
    print("All tests passed!")

def create_report():
    result = add(10, 20)
    with open("build_report.txt", "w") as f:
        f.write(f"Build successful. Result of 10 + 20 is {result}")
    print("Report generated!")

if __name__ == "__main__":
    test_add()
    create_report()