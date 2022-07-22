class Cart:
    def __init__(self):
        self.cart = dict()
    
    def tambahProduk(self, kodeProduk: str, kuantitas: int):
        if kodeProduk not in self.cart:
            self.cart[kodeProduk] = 0
        self.cart[kodeProduk] += kuantitas
        
    def hapusProduk(self, kodeProduk: str):
        if kodeProduk in self.cart:
            del self.cart[kodeProduk]
    
    def tampilkanCart(self):
        for kodeProduk, kuantitas in self.cart.items():
            print(f"{kodeProduk} ({kuantitas})")