# ⚽ Süper Lig Bilgi Discord Botu

Bu proje, Discord kullanıcılarına Trendyol Süper Lig takımları hakkında detaylı ve güncel bilgiler sunan interaktif bir Discord botudur. 

Bot, Discord'un modern **Açılır Menü (Select Menu)** bileşenini kullanarak kullanıcılara tüm lig takımlarını listeler. Seçilen takımın temel bilgilerini (kuruluş yılı, stadyum, kulüp renkleri) yerel veri tabanından alırken, kulübün detaylı tarihçesini ve özetini **Wikipedia REST API** üzerinden anlık olarak çeker ve şık bir **Embed kartı** ile sunar.

---

## ✨ Özellikler

* **Dinamik Açılır Menü (Dropdown):** Süper Lig'deki tüm takımlar tek bir menüde listelenir.
* **Hibrit Veri Modeli:** Temel kulüp verileri (stadyum, renkler, kuruluş yılı) yerelde tutularak anında yanıt verilir; detaylı tarihçe Wikipedia API üzerinden asenkron (`aiohttp`) olarak çekilir.
* **Görsel Embed Kartları:** Çekilen bilgiler Discord standartlarına uygun renkli ve düzenli bilgi kartları halinde gösterilir.
* **SSL & Ağ Uyumluluğu:** Windows ortamlarında veya antivirüs/güvenlik duvarı arkasında çalışan sistemlerde yaşanan SSL sertifika doğrulama takılmalarını aşacak şekilde yapılandırılmıştır.

---

## 🛠️ Kurulum

### 1. Gereksinimler
* Python 3.10 veya üzeri
* Discord Developer Portal üzerinden alınmış bir **Bot Tokeni**
