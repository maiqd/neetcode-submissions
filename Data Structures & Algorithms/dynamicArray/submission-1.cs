public class DynamicArray {
    private int _length = 0;
    private int _capacity;
    private int[] _arr;
    public DynamicArray(int capacity) {
        _arr = new int[capacity];
        _capacity = capacity;
    }

    public int Get(int i) {
        return _arr[i];
    }

    public void Set(int i, int n) {
        _arr[i] = n;
    }

    public void PushBack(int n) {
        if (_length == _capacity)
        {
            this.Resize();
        }
        _arr[_length] = n;
        _length += 1;

    }

    public int PopBack() {
        _length--;
        return _arr[_length];
    }

    private void Resize() {
        _capacity *= 2;
        var newArr = new int[_capacity];
        for (int i = 0; i < _length; i++){
            newArr[i] = _arr[i];
        }
        _arr = newArr;
    }

    public int GetSize() {
        return _length;
    }

    public int GetCapacity() {
        return _capacity;
    }
}
