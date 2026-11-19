# ENRO Yazılım Ekibi Aday Ödevi – Hedef Uzaklığı Kontrol Servisi

Bu proje, ENRO robot köpeğinin hedef konuma olan uzaklığını ve belirlenen yakınlık eşiğine ulaşıp ulaşmadığını hesaplayan bir ROS 2 Jazzy uygulamasıdır.

## Programın Çalışması

- **İstemci (`uzaklik_istemci`):** Sunucuya 5 adet sayısal değer gönderir: `robot_x`, `robot_y`, `hedef_x`, `hedef_y` ve `yakinlik_esigi_m`.
- **Sunucu (`uzaklik_sunucu`):** `/enro/uzaklik_kontrol` servisi üzerinden gelen koordinatları kontrol eder. Tüm değerler sonlu ve `yakinlik_esigi_m > 0` ise $\sqrt{(hedef\_x - robot\_x)^2 + (hedef\_y - robot\_y)^2}$ formülüyle uzaklığı hesaplar, mesafe eşikten küçük veya eşitse `hedefe_yakin = true` döndürür.
- **Topic Yayını:** Yalnızca başarılı isteklerde hesaplanan uzaklık `/enro/hedef_uzakligi` topic'ine `std_msgs/msg/Float64` tipinde bir kez yayınlanır. Sonlu olmayan sayılarda veya sıfır/negatif eşik değerinde `basarili = false` döndürülür ve **topic'e yayın yapılmaz**.

## Derleme ve Çalıştırma

### 1. Workspace Derleme
```bash
cd ~/ros2_ws
colcon build
source install/setup.bash