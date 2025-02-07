# Python  3.8
from string import digits

class HinddenPass(object):
    def __init__(self):
        self.data, self.res = [], []

    def _get_data(self, path = 'input.txt'): # Read dokumen
        f = open(path)
        self.data = f.readlines()[1:]
        f.close()

    @staticmethod
    def cek_input(string_case): # Fungsi untuk mengecek input
        if '@' in string_case and '.' in string_case: # Mengecek apakah Email atau bukan
            temp = string_case.lower().split('@')
            if len(temp[0]) >= 2 and len(string_case) >= 8: # Mengecek apakah Email valid atau tidak
                return 'E'
        else:
            banyak_digit = len([x for x in string_case if x in digits])
            if 10 <= banyak_digit <= 13: # Mengecek apakah input adalah nomor yang valid
                return 'T'
        return 'Invalid Input' # Jika tidak ada kondisi yang terpenuhi

    def solve(self, case): # Fungsi penyelesaian masalah
        kondisi = self.cek_input(case) # Cek input
        if kondisi == 'E': # Jika input adalah Email yang valid
            res = case.strip().lower().split('@') # lower & split by @
            res[0] = res[0][0] + '*' * 5 + res[0][-1] # buat pola seperti yang di perintah
            res = '@'.join(res) 
        elif kondisi == 'T': # Jika input adalah nomor telpon yang valid
            digit_bersih = ''.join([x for x in case.strip() if x in digits]) # ambil hanya digit saja dari input
            res = (("*" * 3)+'-')*2 + digit_bersih[-4:] # buat pola untuk 10 digit terakhir (lokal)
            if len(digit_bersih) > 10: # cek apakah digit > 10
                res = "+" + "*" * (len(digit_bersih) - 10) + '-' + res # tambahkan kode negara
        else: # Jika tidak ada kondisi yang memenuhi
            res = kondisi 
        return res

    def solve_doc(self, path): # Fungsi untuk menyelesaikan masalah di dokumen .txt
        self._get_data(path) # Read data terlebih dahulu
        for i, case in enumerate(self.data): # looping setiap kasus
            res = "Kasus #{} : {}".format(i+1, self.solve(case))
            self.res.append(res) # Append ke res
            print(res)

    def solve_input(self): # Fungsi untuk menerima input dari console dan menyelesaikannya
        kond, counter = "n", 0
        while kond.lower() != "y":
            counter += 1
            case = input("\nPercobaan ke-{} : ".format(counter))
            res = self.solve(case)
            print("Kasus ke-{}     : {}".format(counter, res))
            kond = input("\nExit (y/n) : ")

# Main
HP = HinddenPass()         # Inisiasi kelas
HP.solve_doc('input.txt')  # Menyelesaikan masalah di input.txt
HP.solve_input()           # Connsole input
