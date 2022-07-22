from cart import Cart

def main():
    keranjang = Cart()
    
    keranjang.tambahProduk("Pisang Hijau", 2)
    
    keranjang.tambahProduk("Semangka Kuning", 3)
    
    keranjang.tambahProduk("Apel Merah", 1)
    keranjang.tambahProduk("Apel Merah", 4)
    keranjang.tambahProduk("Apel Merah", 2)
    
    keranjang.hapusProduk("Semangka Kuning")
    
    keranjang.hapusProduk("Semangka Merah")
    
    keranjang.tampilkanCart()

if __name__ == '__main__':
    main()