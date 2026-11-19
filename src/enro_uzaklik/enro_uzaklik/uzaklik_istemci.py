import sys
import rclpy
from rclpy.node import Node
from enro_interfaces.srv import UzaklikKontrol


class UzaklikIstemci(Node):
    def __init__(self):
        super().__init__('uzaklik_istemci')
        # Sunucunun açtığı servise bağlanan istemciyi oluşturuyoruz
        self.istemci = self.create_client(UzaklikKontrol, '/enro/uzaklik_kontrol')

        # Sunucu henüz açılmadıysa açılana kadar saniyede bir kontrol edip bekliyoruz
        while not self.istemci.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Sunucu bekleniyor...')

    def istek_gonder(self, robot_x, robot_y, hedef_x, hedef_y, esik):
        # Sunucuya gidecek 5 sayılık formu dolduruyoruz
        istek = UzaklikKontrol.Request()
        istek.robot_x = float(robot_x)
        istek.robot_y = float(robot_y)
        istek.hedef_x = float(hedef_x)
        istek.hedef_y = float(hedef_y)
        istek.yakinlik_esigi_m = float(esik)

        # İsteği gönderip cevap gelene kadar bekliyoruz
        gelecek_yanit = self.istemci.call_async(istek)
        rclpy.spin_until_future_complete(self, gelecek_yanit)
        return gelecek_yanit.result()


def main(args=None):
    rclpy.init(args=args)
    dugum = UzaklikIstemci()

    # Terminalden 5 sayı verildiyse onları alıyoruz, verilmediyse ilk örneği kullanıyoruz
    if len(sys.argv) == 6:
        rx, ry, hx, hy, esik = sys.argv[1:6]
    else:
        rx, ry, hx, hy, esik = 0.0, 0.0, 3.0, 4.0, 5.0

    yanit = dugum.istek_gonder(rx, ry, hx, hy, esik)

    # Sunucudan gelen cevabı ekrana yazdırıyoruz
    dugum.get_logger().info(
        f'Sonuç -> basarili: {yanit.basarili}, '
        f'uzaklik_m: {yanit.uzaklik_m:.2f}, '
        f'hedefe_yakin: {yanit.hedefe_yakin}, '
        f'aciklama: {yanit.aciklama}'
    )

    dugum.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()