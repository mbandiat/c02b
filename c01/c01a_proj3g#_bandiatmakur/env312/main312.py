def test_312():
    test_version = '3.12'
    new_feature = f"A f-string can contain \\ in {test_version}"
    abc = ['A', 'B', 'C']
    heart_symbol = '\N{BLACK HEART SUIT}'
    print(f"""{new_feature} such as {heart_symbol.join(abc)} """)

if __name__ == '__main__':
    print("Test c01a_proj4g0_sy")
    test_312()
