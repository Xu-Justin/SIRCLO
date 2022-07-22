from perahu_layar import PerahuLayar
from perahu_motor import PerahuMotor
from kapal_pesiar import KapalPesiar

def main():
    perahu_andi = PerahuLayar("Andi", number_of_sail=2)
    perahu_budi = PerahuMotor("Budi", number_of_motor=1)
    perahu_cika = KapalPesiar("Cika", captain="Dinda", number_of_crew=10)
    
    print("Cost of perahu_andi:", perahu_andi.get_cost())
    print("Cost of perahu_budi:", perahu_budi.get_cost())
    print("Cost of perahu_cika:", perahu_cika.get_cost())
    
    print()
    
    print("horn from perahu_andi", end="\t: ")
    perahu_andi.horn()
    
    print("horn from perahu_budi", end="\t: ")
    perahu_budi.horn()
    
    print("horn from perahu_cika", end="\t: ")
    perahu_cika.horn()

if __name__ == '__main__':
    main()