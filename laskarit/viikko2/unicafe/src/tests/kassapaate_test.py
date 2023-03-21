import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassa = Kassapaate()

    def test_pohjakassa(self):
        self.assertEqual(self.kassa.kassassa_rahaa,100000)

    def test_myydyt_edulliset_alkuarvo(self):
        self.assertEqual(self.kassa.edulliset,0)

    def test_myydyt_maukkaat_alkuarvo(self):
        self.assertEqual(self.kassa.maukkaat,0)

    def test_oikea_rahamaara_kassa_edullisen_myynnin_jalkeen(self):
        self.kassa.syo_edullisesti_kateisella(300)
        self.assertEqual(self.kassa.kassassa_rahaa,100240)

    def test_oikea_vaihtoraha_edullisen_myynnin_jalkeen(self):
        self.assertEqual(self.kassa.syo_edullisesti_kateisella(300),60)
    
    def test_oikea_rahamaara_kassa_maukkaan_myynnin_jalkeen(self):
        self.kassa.syo_maukkaasti_kateisella(500)
        self.assertEqual(self.kassa.kassassa_rahaa,100400)

    def test_oikea_vaihtoraha_maukkaan_myynnin_jalkeen(self):
        self.assertEqual(self.kassa.syo_maukkaasti_kateisella(500),100)

    def test_oikea_myytyjen_lounaiden_maara_edullisen_myynnin_jalkeen(self):
        self.kassa.syo_edullisesti_kateisella(300)
        self.assertEqual(self.kassa.edulliset,1)

    def test_oikea_myytyjen_lounaiden_maara_maukkaan_myynnin_jalkeen(self):
        self.kassa.syo_maukkaasti_kateisella(500)
        self.assertEqual(self.kassa.maukkaat,1)

    def test_oikea_rahamaara_kassa_edullisen_myynnin_jalkeen_kun_maksu_ei_ole_riittava(self):
        self.kassa.syo_edullisesti_kateisella(100)
        self.assertEqual(self.kassa.kassassa_rahaa,100000)

    def test_oikea_rahamaara_kassa_maukkaan_myynnin_jalkeen_kun_maksu_ei_ole_riittava(self):
        self.kassa.syo_maukkaasti_kateisella(200)
        self.assertEqual(self.kassa.kassassa_rahaa,100000)

    def test_oikea_palautus_edullisen_myynnin_jalkeen_kun_maksu_ei_ole_riittava(self):
        
        self.assertEqual(self.kassa.syo_edullisesti_kateisella(100),100)

    def test_oikea_palautus_maukkaan_myynnin_jalkeen_kun_maksu_ei_ole_riittava(self):
        
        self.assertEqual(self.kassa.syo_maukkaasti_kateisella(200),200)

    def test_oikea_lounaiden_maara_edullisen_myynnin_jalkeen_kun_maksu_ei_ole_riittava(self):
        self.kassa.syo_edullisesti_kateisella(100)
        self.assertEqual(self.kassa.edulliset,0)

    def test_oikea_lounaiden_maara_maukkaan_myynnin_jalkeen_kun_maksu_ei_ole_riittava(self):
        self.kassa.syo_maukkaasti_kateisella(200)
        self.assertEqual(self.kassa.maukkaat,0)

    def test_oikea_rahamaara_kortilla_edullisen_myynnin_jalkeen(self):
        kortti = Maksukortti(300)
        self.assertEqual(self.kassa.syo_edullisesti_kortilla(kortti),True)

    def test_oikea_rahamaara_kortilla_maukkaan_myynnin_jalkeen(self):
        kortti = Maksukortti(500)
        self.assertEqual(self.kassa.syo_maukkaasti_kortilla(kortti),True)

    def test_oikea_lounaiden_maara_kortilla_edullisen_myynnin_jalkeen(self):
        kortti = Maksukortti(300)
        self.kassa.syo_edullisesti_kortilla(kortti)
        self.assertEqual(self.kassa.edulliset,1)

    def test_oikea_lounaiden_maara_kortilla_maukkaan_myynnin_jalkeen(self):
        kortti = Maksukortti(500)
        self.kassa.syo_maukkaasti_kortilla(kortti)
        self.assertEqual(self.kassa.maukkaat,1)

    def test_edullisen_myynti_kun_kortilla_ei_ole_rahaa_kortin_arvo(self):
        kortti = Maksukortti(200)
        self.kassa.syo_edullisesti_kortilla(kortti)
        self.assertEqual(kortti.saldo,200)

    def test_maukkaan_myynti_kun_kortilla_ei_ole_rahaa_kortin_arvo(self):
        kortti = Maksukortti(300)
        self.kassa.syo_maukkaasti_kortilla(kortti)
        self.assertEqual(kortti.saldo,300)

    def test_edullisen_myynti_kun_kortilla_ei_ole_rahaa(self):
        kortti = Maksukortti(200)
        self.assertEqual(self.kassa.syo_edullisesti_kortilla(kortti),False)

    def test_maukkaan_myynti_kun_kortilla_ei_ole_rahaa(self):
        kortti = Maksukortti(300)
        self.assertEqual(self.kassa.syo_maukkaasti_kortilla(kortti),False)

    def test_oikea_lounaiden_maara_kortilla_edullisen_myynnin_jalkeen_kun_ei_rahaa(self):
        kortti = Maksukortti(200)
        self.kassa.syo_edullisesti_kortilla(kortti)
        self.assertEqual(self.kassa.edulliset,0)

    def test_oikea_lounaiden_maara_kortilla_maukkaan_myynnin_jalkeen_kun_ei_rahaa(self):
        kortti = Maksukortti(300)
        self.kassa.syo_maukkaasti_kortilla(kortti)
        self.assertEqual(self.kassa.maukkaat,0)

    def test_kassa_ei_muutu_kun_ostetaan_kortilla_edullinen(self):
        kortti = Maksukortti(300)
        self.kassa.syo_edullisesti_kortilla(kortti)
        self.assertEqual(self.kassa.kassassa_rahaa,100000)

    
    def test_kassa_ei_muutu_kun_ostetaan_kortilla_maukas(self):
        kortti = Maksukortti(500)
        self.kassa.syo_maukkaasti_kortilla(kortti)
        self.assertEqual(self.kassa.kassassa_rahaa,100000)

    def test_kortin_lataus_siirtyy_kassaan(self):
        kortti = Maksukortti(0)
        self.kassa.lataa_rahaa_kortille(kortti,1000)
        self.assertEqual(self.kassa.kassassa_rahaa,101000)

    def test_kortin_lataus_nakyy_kortilla(self):
        kortti = Maksukortti(0)
        self.kassa.lataa_rahaa_kortille(kortti,1000)
        self.assertEqual(kortti.saldo,1000)

    def test_kortin_lataus_negativiisella_arvolla(self):
        kortti = Maksukortti(0)
        self.kassa.lataa_rahaa_kortille(kortti,-100)
        self.assertEqual(kortti.saldo,0)
        
