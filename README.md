# FaceDetection
Face Detection


OpenCV (Açık Kaynak Görsel Kütüphane) , Intel tarafından 1999 yılında başlatılan popüler bir bilgisayarlı görsel kütüphanesidir ve BSD lisansı altında 
yayımlandığı için akademik projelerde ve ticari ürünlerde kullanılabiliyor.

OpenCV'nin barındırdığı algoritmalar:

      Eigenfaces (createEigenFaceRecognizer())
      Fisherfaces (createFisherFaceRecognizer())
      Local Binary Patterns Histograms (createLBPHFaceRecognizer())
      Kullanacağımız diğer modül ise face_recognition

Face Recognition'ın barındırdığı algoritmalar:

      Find faces in pictures
      Find and manipulate facial features in pictures
      Digital make-up
      Identify faces in pictures
      Real-time face recognition (Biz bu özelliği kullanacağız)
      Real-time face recognition

Real-time face recognition ile python içerisinde kamerayı açacağız ve anlık olarak yüz tarama yapacağız. Realtime olarak sizi tanıyabilmesi için bir veri 
ile karşılaştırması ve sizi önceden tanıması gerekiyor. Bunu da kişiye ait bir profil resmi uygulamamıza import ederek halledeceğiz.

Yani programa kendimizi tanıtıyoruz;

[foto1] => Ronaldo, [foto2] => Messi, [foto1] => Neymar  

Sonraki aşamada yazacağımız uygulama, sisteme tanıtılan "Ronaldo","Messi" ve "Neymar" resimlerine ait yüzleri kamerada arıyor ve bulduğu zaman gerekli 
işlemleri yaptırabiliyoruz.
