# Tạo lớp - cập nhật thông tin - xuất
class HocSinh:
    def __init__(self, ten, dia_chi, chieu_cao, can_nang, hoc_luc):
        self.ten = ten
        self.dia_chi = dia_chi
        self.chieu_cao = chieu_cao
        self.can_nang = can_nang
        self.hoc_luc = hoc_luc

    def cap_nhat_dia_chi(self, dia_chi_moi):
        self.dia_chi = dia_chi_moi
        print(f"Địa chỉ của {self.ten} được cập nhật thành {dia_chi_moi}")

    def cap_nhat_suc_khoe(self, chieu_cao_moi, can_nang_moi):
        self.chieu_cao = chieu_cao_moi
        self.can_nang = can_nang_moi
        print(f"Thông tin sức khỏe của {self.ten} đã được cập nhật.")

    def xuat_thong_tin(self):
        print(
            f"Thông tin học sinh:\n Tên:{self.ten} \n Đại chỉ: {self.dia_chi} \n Chiều cao: {self.chieu_cao}cm\n Cân nặng: {self.can_nang}kg\n Học lực: {self.hoc_luc}"
        )


hoc_sinh = HocSinh("Nguyen Van A", "672A28 PVT, TP.HCM", 160, 55, "Yếu")
hoc_sinh.xuat_thong_tin()

hoc_sinh.cap_nhat_dia_chi("672A28 Phan Văn Trị, TP>.HCM")
hoc_sinh.cap_nhat_suc_khoe(171, 78)
hoc_sinh.xuat_thong_tin()
