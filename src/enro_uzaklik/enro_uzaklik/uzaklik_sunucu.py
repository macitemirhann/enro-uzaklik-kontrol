import math
import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64
from enro_interfaces.srv import UzaklikKontrol


class UzaklikSunucu(Node):
    def __init__(self):
        # Düğümü "uzaklik_sunucu" adıyla başlatıyoruz
        super().__init__('uzaklik_sunucu')

        # İstekleri dinleyecek servisi açıyoruz
        self.servis = self.create_service(
            UzaklikKontrol,
            '/enro/uzaklik_kontrol',
            self.uzaklik_hesapla
        )

        # Başarılı sonuçları yayınlayacağımız topic kanalını açıyoruz
        self.yayinci = self.create_publisher(Float64, '/enro/hedef_uzakligi', 10)
        self.get_logger().info('Uzaklık kontrol sunucusu hazır, istek bekleniyor...')

    def uzaklik_hesapla(self, request, response):
        # Gelen 5 sayıyı tek listede toplayıp geçerli (sonlu) sayı mı diye kontrol ediyoruz
        sayilar = [
            request.robot_x,
            request.robot_y,
            request.hedef_x,
            request.hedef_y,
            request.yakinlik_esigi_m
        ]

        if not all(math.isfinite(s) for s in sayilar):
            response.basarili = False
            response.uzaklik_m = 0.0
            response.hedefe_yakin = False
            response.aciklama = 'Hata: Tüm değerler sonlu (geçerli) sayı olmalıdır.'
            return response

        # Yakınlık eşiği 0 veya negatifse hata döndürüp topic'e yayın yapmıyoruz
        if request.yakinlik_esigi_m <= 0.0:
            response.basarili = False
            response.uzaklik_m = 0.0
            response.hedefe_yakin = False
            response.aciklama = 'Hata: Yakınlık eşiği sıfırdan büyük olmalıdır.'
            return response

        # İki nokta arasındaki uzaklığı Pisagor formülüyle hesaplıyoruz
        dx = request.hedef_x - request.robot_x
        dy = request.hedef_y - request.robot_y
        uzaklik = math.sqrt(dx ** 2 + dy ** 2)

        # Hesaplanan uzaklık eşikten küçük veya eşitse hedefe yakın kabul ediyoruz
        yakin_mi = uzaklik <= request.yakinlik_esigi_m

        # İstemciye dönecek yanıtı dolduruyoruz
        response.basarili = True
        response.uzaklik_m = uzaklik
        response.hedefe_yakin = yakin_mi
        if yakin_mi:
            response.aciklama = 'Robot hedefe yakınlık eşiği içinde.'
        else:
            response.aciklama = 'Robot hedefe yakınlık eşiğinin dışında.'

        # Başarılı olduğu için uzaklığı topic'e bir kez yayınlıyoruz
        mesaj = Float64()
        mesaj.data = uzaklik
        self.yayinci.publish(mesaj)

        return response


def main(args=None):
    rclpy.init(args=args)
    dugum = UzaklikSunucu()
    # Program kapanana kadar gelen istekleri dinlemesini sağlıyoruz
    rclpy.spin(dugum)
    dugum.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()