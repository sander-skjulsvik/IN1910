from vector import Vector3D

def test_init():
    u = Vector3D(1,2,3)

def test_str():
    u = Vector3D(1,2,3)
    # print(u)
    assert str(u) == '1, 2, 3'

def test_repr():
    assert repr(Vector3D(1,2,3)) == 'Vector(1, 2, 3)'

def test_add():
    u = Vector3D(2,0,-2)
    v = Vector3D(2,4,2)
    print(Vector3D(4,4,0))
    assert u + v == Vector3D(4,4,0)

if __name__ == "__main__":
    test_init()
    test_str()
    test_add()
