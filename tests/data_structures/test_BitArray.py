import pyrival.data_structures


def test_BitArray():
    array = pyrival.data_structures.BitArray(262144)

    for i in range(262144):
        assert array[i] == 0
        array[i] = 1
        assert array[i] == 1

    for i in range(262144):
        assert array[i] == 1
        array[i] = 0
        assert array[i] == 0
