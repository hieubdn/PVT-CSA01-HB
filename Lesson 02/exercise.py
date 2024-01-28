class Xe: #Class cha
    def __init__(self, hang, mau, gia_tien):
        self.hang = hang
        self.mau = mau
        self.gia_tien = gia_tien
    def khoi_dong(self):
        print(f"Xe {self.hang} dang duoc khoi dong")
#Class Con
class XeDap(Xe):
    def dap_bang_hai_chan(self):
        print(f"Xe {self.hang} dang duoc dap ve phia turoc")
    def chay_bang_bon_banh(self):
        print(f"Xe {self.hang} dang chay ve phia turoc bang dong co")