# tính chu vi hình vuông
class HinhVuong:
    def __init__ (self, canh):
        self.canh = canh
    def tinh_chu_vi(self):
        chu_vi = self.canh * 4
        return chu_vi
canh_hinh_vuong = 5
hinhvuong = HinhVuong(canh_hinh_vuong)
ket_qua = hinhvuong.tinh_chu_vi()
print(ket_qua)