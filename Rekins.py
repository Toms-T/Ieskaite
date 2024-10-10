from datetime import date

 class Rekins:
    def __init__(self, vards, veltijums, izmers, materials):
        self.vards = vards
        self.veltijums = veltijums
        self.izmers = izmers  # [platums, garums, augstums]
        self.materials = materials
        self.laiks = date.today()
        self.samaksa = self.aprekins()

    def aprekins(self):
        darba_samaksa = 15
        PVN = 21
        platums, garums, augstums = self.izmers
        produkta_cena = (len(self.veltijums) * 1.2) + (platums/100 * garums/100 * augstums/100) / 3 * self.materials
        PVN_summa = (produkta_cena + darba_samaksa) * PVN / 100
        rekina_summa = produkta_cena + darba_samaksa + PVN_summa
        return rekina_summa

     def info(self):
        print(f"Rēķins izveidots: {self.laiks}")
        print(f"Klients: {self.klients}")
        print(f"Veltījums: {self.veltijums}")
        print(f"Izmēri: Platums: {self.izmers[0]} mm, Garums: {self.izmers[1]} mm, Augstums: {self.izmers[2]} mm")
        print(f"Kokmateriāla cena: {self.materials} EUR/m2")
        print(f"Kopējā summa (ar PVN): {self.samaksa:.2f} EUR")
     
    












