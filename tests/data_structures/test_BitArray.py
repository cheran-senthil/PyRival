import pyrival.data_structures


def test_BitArray():
    array = pyrival.data_structures.BitArray(524288)
    for i in range(524288):
        assert array[i] == 0
        array[i] = 1
        assert array[i] == 1
