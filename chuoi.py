s = 'abc'
print(len(s))
s = 'abcd'
print(len(s))  # function tra ve do dai cua string

s = 'HOANG XUAN HUNG'  # Dùng để chuyển một string về dạng in thường
print(s.lower())

s = 'nguyen bao trang'  # Dùng để chuyển một string về dạng in hoa
print(s.upper())

# function dùng để kiểm tra string một xâu có chỉ chứa các kí tự chữ và số hay không
s = 'codelearn2020'
print(s.isalnum())
s = 'codelearn2020.io'  # False vì trong string có chứa dấu .
print(s.isalnum())

s = 'codelearn'
print(s.isalpha())  # function kiểm tra xem string toàn chữ đko
s = 'codelearn2020'
print(s.isalpha())  # false vì trong string có số 2020

s = '2020'
print(s.isnumeric())  # function kiểm tra xem string có toàn kí tự số không
s = 'c2020'
print(s.isnumeric())  # False vì trong string có kí tự "c"

# function dùng để cắt một chuỗi ra thành list các chuỗi khác dựa trên một phần tử trong chuỗi đầu vào
s = 'Welcome to Codelearn.io!'
print(s.split(" "))
s = "A1B1C1D1E1"
print(s.split('1'))

# function dung để cắt một list thành string
lst = ['Welcome', 'to', 'Codelearn.io!']
print(' '.join(lst))
lst = ['A', 'B', 'C']
print('-'.join(lst))

# dùng hàm split() và hàm join() để loại bỏ các khoảng trắng thừa trong chuỗi
message = '    Welcome    to    Codelearn.io '
print(' '.join(message.split()))

name = 'Cod3l3arn'
print(name.replace('3', 'e'))

Hung ngu vcl

