-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Anamakine: 127.0.0.1
-- Üretim Zamanı: 25 Kas 2022, 10:09:42
-- Sunucu sürümü: 10.4.25-MariaDB
-- PHP Sürümü: 8.1.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Veritabanı: `makromaden`
--

-- --------------------------------------------------------

--
-- Tablo için tablo yapısı `cart`
--

CREATE TABLE `cart` (
  `id` int(11) NOT NULL,
  `title` text COLLATE utf8mb4_turkish_ci NOT NULL,
  `stock` int(11) NOT NULL,
  `price` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_turkish_ci;

-- --------------------------------------------------------

--
-- Tablo için tablo yapısı `edit`
--

CREATE TABLE `edit` (
  `id` int(11) NOT NULL,
  `title` text COLLATE utf8mb4_turkish_ci NOT NULL,
  `content` text COLLATE utf8mb4_turkish_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_turkish_ci;

--
-- Tablo döküm verisi `edit`
--

INSERT INTO `edit` (`id`, `title`, `content`) VALUES
(1, 'Makromaden', '•\r\n        •\r\n        Makromaden 2019 yılında, iplerin dünyasını keşfetmemle başlamış olduğum bir rüyanın gerçeğe dönüşüdür.\r\n        Ürünlerimiz kişiye özel olup;\r\n        ????Renk seçeneklerimiz mevcuttur.\r\n        ????İstenilen ebatlarda yapılabilir.\r\n        ????Tercihe bağlı astarlı ve fermuarlı yapılabilir.\r\n        Biraz benden, biraz sizden ve çokça bizden bir şeyler bulabileceğiniz sayfamıza destek olmak için instagram sayfamızı takip etmeyi unutmayınız ❣\r\n        •\r\n        •'),
(2, 'İletişim Bilgileri', 'Bizi takip etmeyi unutmayınız\r\nEmail Adresi: sedanur.kukmen@gmail.com \r\nTelefon Numarası: 0545 788 56 90\r\nAdresi Bilgisi: Orta mah. Atatürk bulv. 86. sk. No:3/2 Cumayeri- DÜZCE');

-- --------------------------------------------------------

--
-- Tablo için tablo yapısı `product`
--

CREATE TABLE `product` (
  `id` int(11) NOT NULL,
  `title` text COLLATE utf8mb4_turkish_ci NOT NULL,
  `category` text COLLATE utf8mb4_turkish_ci NOT NULL,
  `content` text COLLATE utf8mb4_turkish_ci NOT NULL,
  `stock` int(11) NOT NULL,
  `upload_time` timestamp NOT NULL DEFAULT current_timestamp(),
  `price` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_turkish_ci;

--
-- Tablo döküm verisi `product`
--

INSERT INTO `product` (`id`, `title`, `category`, `content`, `stock`, `upload_time`, `price`) VALUES
(6, 'Makrome Telefon Çantası', 'Çanta', 'Makrome Mini Çanta\r\nSiparişe özel renk ve boyutta çalışılmıştır. Gittiği yere mutluluk götürmesi dileğiyle????????\r\nAçılışa özel fiyatlarımız indirimlidir. Bilgi almak için DM üzerinden iletişime geçebilirsiniz.\r\n•\r\n•\r\n????Renk seçeneklerimiz mevcuttur.\r\n????İstenilen ebatlarda yapılabilir.\r\n????Tercihe bağlı astarlı ve fermuarlı yapılabilir.\r\n•\r\n•\r\nBiraz benden, biraz sizden ve çokça bizden bir şeyler bulabileceğiniz sayfamıza destek olmak için begenmeyi , yorum yapmayı ve takip etmeyi unutmayınız ❣\r\n•\r\n•', 1, '2022-11-18 09:30:17', 200),
(7, 'Pembe Makrome Runner', 'Ev Ürünleri', 'vinize runnerlarımızla farklı bir hava katın ????\r\nAçılışa özel fiyatlarımız indirimlidir. Bilgi almak için DM üzerinden iletişime geçebilirsiniz.\r\n•\r\n•\r\n????Renk seçeneklerimiz mevcuttur.\r\n????İstenilen ebatlarda yapılabilir.\r\n•\r\n•\r\nBiraz benden, biraz sizden ve çokça bizden bir şeyler bulabileceğiniz sayfamıza destek olmak için begenmeyi , yorum yapmayı ve takip etmeyi unutmayınız ❣\r\n•\r\n•\r\n•', 1, '2022-11-18 10:56:16', 400),
(8, 'Makrome Çanta Kiti', 'Kitler', 'Makrome çanta kitimizle sizde kendi çantanızı yapabilecek ve bu benzersiz deneyimin keyfini çıkaracaksınız.\r\nAçılışa özel fiyatlarımız indirimlidir. Bilgi almak için DM üzerinden iletişime geçebilirsiniz.\r\n•\r\n•\r\n????Renk seçeneklerimiz mevcuttur.\r\n????İstenilen ebatlarda yapılabilir.\r\n•\r\n•\r\nBiraz benden, biraz sizden ve çokça bizden bir şeyler bulabileceğiniz sayfamıza destek olmak için begenmeyi , yorum yapmayı ve takip etmeyi unutmayınız ❣\r\n•\r\n•\r\n•', 10, '2022-11-18 10:57:50', 300),
(9, 'Makrome Hamak', 'Ev Ürünleri', 'vinize runnerlarımızla farklı bir hava katın ????\r\nAçılışa özel fiyatlarımız indirimlidir. Bilgi almak için DM üzerinden iletişime geçebilirsiniz.\r\n•\r\n•\r\n????Renk seçeneklerimiz mevcuttur.\r\n????İstenilen ebatlarda yapılabilir.\r\n•\r\n•\r\nBiraz benden, biraz sizden ve çokça bizden bir şeyler bulabileceğiniz sayfamıza destek olmak için begenmeyi , yorum yapmayı ve takip etmeyi unutmayınız ❣\r\n•\r\n•\r\n•', 1, '2022-11-18 10:58:10', 1500),
(10, 'Makrome Hanging Duvar Süsü', 'Ev Ürünleri', 'vinize runnerlarımızla farklı bir hava katın ????\r\nAçılışa özel fiyatlarımız indirimlidir. Bilgi almak için DM üzerinden iletişime geçebilirsiniz.\r\n•\r\n•\r\n????Renk seçeneklerimiz mevcuttur.\r\n????İstenilen ebatlarda yapılabilir.\r\n•\r\n•\r\nBiraz benden, biraz sizden ve çokça bizden bir şeyler bulabileceğiniz sayfamıza destek olmak için begenmeyi , yorum yapmayı ve takip etmeyi unutmayınız ❣\r\n•\r\n•\r\n•', 1, '2022-11-18 10:58:38', 500),
(11, 'Makrome Çanta', 'Çanta', 'vinize runnerlarımızla farklı bir hava katın ????\r\nAçılışa özel fiyatlarımız indirimlidir. Bilgi almak için DM üzerinden iletişime geçebilirsiniz.\r\n•\r\n•\r\n????Renk seçeneklerimiz mevcuttur.\r\n????İstenilen ebatlarda yapılabilir.\r\n•\r\n•\r\nBiraz benden, biraz sizden ve çokça bizden bir şeyler bulabileceğiniz sayfamıza destek olmak için begenmeyi , yorum yapmayı ve takip etmeyi unutmayınız ❣\r\n•\r\n•\r\n•', 1, '2022-11-18 10:58:54', 350),
(12, 'Makrome Gitar Askısı', 'Ev Ürünleri', 'vinize runnerlarımızla farklı bir hava katın ????\r\nAçılışa özel fiyatlarımız indirimlidir. Bilgi almak için DM üzerinden iletişime geçebilirsiniz.\r\n•\r\n•\r\n????Renk seçeneklerimiz mevcuttur.\r\n????İstenilen ebatlarda yapılabilir.\r\n•\r\n•\r\nBiraz benden, biraz sizden ve çokça bizden bir şeyler bulabileceğiniz sayfamıza destek olmak için begenmeyi , yorum yapmayı ve takip etmeyi unutmayınız ❣\r\n•\r\n•\r\n•', 1, '2022-11-18 10:59:45', 200),
(13, 'Supla ', 'Ev Ürünleri', 'vinize runnerlarımızla farklı bir hava katın ????\r\nAçılışa özel fiyatlarımız indirimlidir. Bilgi almak için DM üzerinden iletişime geçebilirsiniz.\r\n•\r\n•\r\n????Renk seçeneklerimiz mevcuttur.\r\n????İstenilen ebatlarda yapılabilir.\r\n•\r\n•\r\nBiraz benden, biraz sizden ve çokça bizden bir şeyler bulabileceğiniz sayfamıza destek olmak için begenmeyi , yorum yapmayı ve takip etmeyi unutmayınız ❣\r\n•\r\n•\r\n•', 20, '2022-11-18 11:00:11', 80),
(14, 'Makrome Duvar Süsü Kiti', 'Kitler', 'vinize runnerlarımızla farklı bir hava katın ????\r\nAçılışa özel fiyatlarımız indirimlidir. Bilgi almak için DM üzerinden iletişime geçebilirsiniz.\r\n•\r\n•\r\n????Renk seçeneklerimiz mevcuttur.\r\n????İstenilen ebatlarda yapılabilir.\r\n•\r\n•\r\nBiraz benden, biraz sizden ve çokça bizden bir şeyler bulabileceğiniz sayfamıza destek olmak için begenmeyi , yorum yapmayı ve takip etmeyi unutmayınız ❣\r\n•\r\n•\r\n•', 5, '2022-11-18 11:01:02', 280),
(15, 'Makrome El Çantası', 'Çanta', 'vinize runnerlarımızla farklı bir hava katın ????\r\nAçılışa özel fiyatlarımız indirimlidir. Bilgi almak için DM üzerinden iletişime geçebilirsiniz.\r\n•\r\n•\r\n????Renk seçeneklerimiz mevcuttur.\r\n????İstenilen ebatlarda yapılabilir.\r\n•\r\n•\r\nBiraz benden, biraz sizden ve çokça bizden bir şeyler bulabileceğiniz sayfamıza destek olmak için begenmeyi , yorum yapmayı ve takip etmeyi unutmayınız ❣\r\n•\r\n•\r\n•', 2, '2022-11-18 11:01:31', 450),
(16, 'Makrome salıncak', 'Ev Ürünleri', 'gfhghadsfdxgfcgv', 1, '2022-11-22 16:31:05', 1500),
(19, 'makrome salıncak', 'Ev Ürünleri', 'sdfghukjhgffgrthfjyg', 1, '2022-11-23 16:38:09', 1500);

-- --------------------------------------------------------

--
-- Tablo için tablo yapısı `sipariş`
--

CREATE TABLE `sipariş` (
  `id` int(11) NOT NULL,
  `name` text COLLATE utf8mb4_turkish_ci NOT NULL,
  `surname` text COLLATE utf8mb4_turkish_ci NOT NULL,
  `adress` text COLLATE utf8mb4_turkish_ci NOT NULL,
  `email` text COLLATE utf8mb4_turkish_ci NOT NULL,
  `phone_number` int(11) NOT NULL,
  `upload_time` int(11) NOT NULL DEFAULT current_timestamp(),
  `cart_info` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_turkish_ci;

-- --------------------------------------------------------

--
-- Tablo için tablo yapısı `user`
--

CREATE TABLE `user` (
  `id` int(11) NOT NULL,
  `name` text COLLATE utf8mb4_turkish_ci NOT NULL,
  `username` text COLLATE utf8mb4_turkish_ci NOT NULL,
  `email` text COLLATE utf8mb4_turkish_ci NOT NULL,
  `password` text COLLATE utf8mb4_turkish_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_turkish_ci;

--
-- Tablo döküm verisi `user`
--

INSERT INTO `user` (`id`, `name`, `username`, `email`, `password`) VALUES
(1, 'Sedanur', 'sdnrkkmn', 'sedanur.kukmen@gmail.com', '$5$rounds=535000$9QvJdZl1KGic21ow$.DdROq.V03KPg7d1Pa5wfJFSlMOSZVyOyfa90AKQ3XA'),
(2, 'Eda Kükmen', 'edakukmen', 'edakukmen@gmail.com', '$5$rounds=535000$TLCO/hUD4LFx1lWe$IgLmbLBJ4EDylwwq/MVS6/M9CVxb3wrj9eNvKTUtdZ/'),
(3, 'ALPER kükmen', 'alperkkmn', 'alper@gmail.com', '$5$rounds=535000$vCw/4sQ720h6hzHB$FVxqAlD2TfmX0GQ9y9xH.58og8HhhkXh7SczHlUlQ58'),
(4, 'Alper Kükmen', 'alperkukmen', 'alperkukmenn@gmail.com', '$5$rounds=535000$hF4uQTYUrc6T.ZuK$d3yn6Zjc594JaBLoxIDbbuN40QW1ppQEPsBDl6Z5oR7');

-- --------------------------------------------------------

--
-- Tablo için tablo yapısı `özelsipariş`
--

CREATE TABLE `özelsipariş` (
  `id` int(11) NOT NULL,
  `username` text COLLATE utf8mb4_turkish_ci NOT NULL,
  `name` text COLLATE utf8mb4_turkish_ci NOT NULL,
  `content` text COLLATE utf8mb4_turkish_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_turkish_ci;

--
-- Dökümü yapılmış tablolar için indeksler
--

--
-- Tablo için indeksler `cart`
--
ALTER TABLE `cart`
  ADD PRIMARY KEY (`id`);

--
-- Tablo için indeksler `product`
--
ALTER TABLE `product`
  ADD PRIMARY KEY (`id`);

--
-- Tablo için indeksler `sipariş`
--
ALTER TABLE `sipariş`
  ADD PRIMARY KEY (`id`);

--
-- Tablo için indeksler `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`id`);

--
-- Tablo için indeksler `özelsipariş`
--
ALTER TABLE `özelsipariş`
  ADD PRIMARY KEY (`id`);

--
-- Dökümü yapılmış tablolar için AUTO_INCREMENT değeri
--

--
-- Tablo için AUTO_INCREMENT değeri `cart`
--
ALTER TABLE `cart`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=61;

--
-- Tablo için AUTO_INCREMENT değeri `product`
--
ALTER TABLE `product`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=20;

--
-- Tablo için AUTO_INCREMENT değeri `sipariş`
--
ALTER TABLE `sipariş`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- Tablo için AUTO_INCREMENT değeri `user`
--
ALTER TABLE `user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- Tablo için AUTO_INCREMENT değeri `özelsipariş`
--
ALTER TABLE `özelsipariş`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
