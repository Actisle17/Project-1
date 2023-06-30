def is_sorted(lst):
    """
    Kiểm tra xem một danh sách số đã được sắp xếp hay chưa.
    Nếu danh sách đã được sắp xếp tăng dần hoặc giảm dần, hàm sẽ trả về True. Nếu không, nó sẽ trả về False.
    """
    return lst == sorted(lst) or lst == sorted(lst, reverse=True)

def main():
    """
    Chương trình chính để kiểm tra xem một danh sách số đã được sắp xếp hay chưa.
    """
    numbers = input("Nhập vào một danh sách các số, cách nhau bởi dấu cách: ").split()
    numbers = [int(x) for x in numbers]

    if is_sorted(numbers):
        print("Danh sách đã được sắp xếp.")
    else:
        print("Danh sách chưa được sắp xếp.")

if __name__ == '__main__':
    main()