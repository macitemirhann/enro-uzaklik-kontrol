
## ROS2

ROS2 ubuntu işletim sistemi üzerinde çalışan, robotları geliştirmek için hazırlanmış açık kaynaklı bir yazılım çatısıdır. Sensör okuma, haritalama, karar verme gibi farklı görevleri küçük parçalara bölüp birbirleriyle haberleşmelerini sağlar. Hazır kütüphaneler sağlar ve ekip içi çalışmayı kolaylaştırır.

## Çalışma düzeni

- **Workspace** : Tüm projeyi içinde barındıran ana klasördür.
- **Package** : Belirli göreve yönelik kodları, mesaj veya servis tanımlarını tutan modüler yazılım birimidir.
- **Node** : Sistemde tek bir görevi yerine getiren programdır.

## Mesajlaşma

- **Topic** : Düğümler arası veri akışının sağlandığı kanaldır.
- **Message** : Bu kanaldan akan verinin tipidir.
- **Publisher** : Belirli bir topic'e gerektiğinde mesaj gönderen düğümdür.
- **Subscriber** : O topic'i dinleyip gelen mesajları alan düğümdür. Bir topic'te birden fazla subscriber veya puplisher olabilir.

## İstek ve yanıt

- **Service** : Sadece ihtiyaç duyulduğunda çalışan soru cevap iletişim yöntemidir.
- **Client** : Servise bir iş yaptırmak için çağrı yapan düğümdür.
- **Request** : İstemcinin servise gönderdiği girdi verileridir.
- **Response** : Servisin işi bitirip cliente döndürdüğü sonuçtur.

## Uzun görevler: action, goal, feedback ve result

Ne zaman kullanılır? Anlık olmayan, saniyeler veya dakikalar süren bir görevin takip edilmesinde ya da gerektiğinde iptal edilmesinde kullanılır. (Bir robotun oda değiştirmesi gibi)

Action 3 bileşenden oluşur :

- **Goal** : İstemcinin başlattığı ana görevdir.
- **Feedback** : Görev sırasında gönderilen durum bilgisidir.
- **Result** : Görev bitince ya da iptal edilince dönen sonuçtur.

## Diğer temel araçlar

- **Parameter** : Düğümlerin ayarlarını (hız limiti, eşik değeri vs) kodu tekrar derlemeden dışarıdan değiştirmeye yarar.
- **Launch** : Birden çok düğümü, parametreleri ve yapılandırmaları tek bir dosya ile aynı anda başlatmaya yarar.
- **ros2 komutları**: Terminalden sistemi yönetmek ve hata ayıklamak için kullanılır.

---

- topic->tek yönlü ->kamera görüntüsü paylaşımı
- service->çift yönlü ->robot şu an hedefe 5 metreden yakın mı?
- action->çift yönlü, uzun görev->robota a noktasından b noktasına yürü demek ve bu sırada feedback almak, gerekirse durdurmak.