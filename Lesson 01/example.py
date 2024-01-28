# Ví dụ khởi tạo class
class dog:
    tuoi = ""  # thuộc tính
    mau_long = ""
    can_nang = ""

class dog:
    def __init__(self, tuoi, mau_long, can_nang):
        # init <=> initialize - công dụng chính của hàm là thực hiện các công việc khởi tạo ban đầu cho đối tượng
        # self: Khi một phương thức được gọi, self được tự động truyền vào và trở thành đối tượng hiện tại của lớp đó. Giúp xác định đối tượng mà phương thức đang được gọi để có thể thực hiện với các thuộc tính và phương thức của đối tượng đó.
        self.tuoi = tuoi  # đối tượng
        self.mau_long = mau_long
        self.can_nang = can_nang

# Ví dụ.
class VatNuoi:
    def __init__(self, ten, giong, mausac, tuoi, cannang):
        self.ten = ten
        self.giong = giong
        self.mausac = mausac
        self.tuoi = tuoi
        self.cannang = cannang
thu_cung = VatNuoi("Milu", "Chó mặt xệ", "Đen - Trắng", 3, 15)
print("Thông tin về: ", thu_cung.ten)
print("Giống loài: ", thu_cung.giong)
print("Màu lông: ", thu_cung.mausac)
print("Tuổi: ", thu_cung.tuoi)
print("Cân nặng: ", thu_cung.cannang)


