import 'package:flutter/material.dart';
import 'package:yesilpaket/screens/Home_screen.dart';

class ProfileScreen extends StatefulWidget {
  const ProfileScreen({Key? key}) : super(key: key);

  @override
  State<ProfileScreen> createState() => _ProfileScreenState();
}

class _ProfileScreenState extends State<ProfileScreen> {
  int _currentIndex = 4; // Aktif sekmeyi takip eder

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        leading: IconButton(
          icon: Icon(Icons.arrow_back, color: Colors.black),
          onPressed: () {
            // Geri butonu işlemi
          },
        ),
        title: Text(
          "Profil",
          style: TextStyle(color: Colors.black),
        ),
        centerTitle: true,
        backgroundColor: Colors.transparent,
        elevation: 0,
        actions: [
          IconButton(
            icon: Icon(Icons.settings, color: Colors.black),
            onPressed: () {
              // Ayarlar işlemi
            },
          ),
        ],
      ),
      body: SingleChildScrollView(
        child: Column(
          children: [
            // Profil Bilgileri
            SizedBox(height: 20),
            CircleAvatar(
              radius: 50,
              backgroundColor: Colors.green,
              child: Icon(Icons.person, size: 60, color: Colors.white),
            ),
            SizedBox(height: 10),
            Text(
              "Ahmet Yılmaz",
              style: TextStyle(fontSize: 22, fontWeight: FontWeight.bold),
            ),
            SizedBox(height: 5),
            Row(
              mainAxisAlignment: MainAxisAlignment.center,
              children: [
                Text(
                  "ahmetyilmaz@hotmail.com",
                  style: TextStyle(color: Colors.grey),
                ),
                SizedBox(width: 5),
                Icon(Icons.edit, size: 16, color: Colors.grey),
              ],
            ),
            SizedBox(height: 20),

            // Kullanıcı Adı ve Şifre
            buildInfoCard("Kullanıcı adı", "ahmetyilmaz"),
            buildInfoCard("Şifre", "********"),

            // Diğer Bilgiler
            buildInfoCard("Adreslerim", ""),
            buildInfoCard("Ödeme Yöntemlerim", ""),
            buildInfoCard("Kuponlarım", ""),
            buildInfoCard("Hakkımızda", ""),

            SizedBox(height: 20),

            // Çıkış Yap ve Hesabı Sil Butonları
            ElevatedButton(
              onPressed: () {
                // Çıkış yap işlemi
              },
              style: ElevatedButton.styleFrom(
                backgroundColor: Colors.red,
                minimumSize: Size(200, 50),
              ),
              child: Text(
                "ÇIKIŞ YAP",
                style: TextStyle(fontSize: 16, color: Colors.white),
              ),
            ),
            SizedBox(height: 1),
            TextButton.icon(
              onPressed: () {
                // Hesabı sil işlemi
              },
              icon: Icon(Icons.delete, color: Colors.red),
              label: Text(
                "HESABI SİL",
                style: TextStyle(color: Colors.red),
              ),
            ),
            SizedBox(height: 20),
          ],
        ),
      ),
      bottomNavigationBar: _buildBottomNavigationBar(),
    );
  }

  Widget _buildBottomNavigationBar() {
    return BottomNavigationBar(
      currentIndex: _currentIndex,
      onTap: (index) {
        setState(() {
          _currentIndex = index;
        });
        // Navigasyon tıklamasıyla ilgili sayfa geçişi yapalım
        _navigateToPage(index);
      },
      selectedItemColor: const Color.fromARGB(255, 31, 179, 31),
      unselectedItemColor: const Color.fromARGB(255, 110, 107, 107),
      showSelectedLabels: true,
      showUnselectedLabels: true,
      type: BottomNavigationBarType.fixed, // Sabit ikon boyutları için
      items: const [
        BottomNavigationBarItem(
          icon: Icon(Icons.home),
          label: 'Ana Sayfa',
        ),
        BottomNavigationBarItem(
          icon: Icon(Icons.watch_later_outlined),
          label: 'Geçmiş',
        ),
        BottomNavigationBarItem(
          icon: Icon(Icons.headset_mic_rounded, size: 40),
          label: 'Destek',
        ),
        BottomNavigationBarItem(
          icon: Icon(Icons.timeline),
          label: 'Finans',
        ),
        BottomNavigationBarItem(
          icon: Icon(Icons.person),
          label: 'Profil',
        ),
      ],
    );
  }

  // Bu fonksiyon, tıklanan sekmeye göre sayfa geçişini sağlıyor.
  void _navigateToPage(int index) {
    // Sayfa değişimi işlemi
    switch (index) {
      case 0:
        Navigator.pushReplacement(
          context,
          MaterialPageRoute(builder: (context) => const HomeScreen()),
        );
        break;

      case 4:
        Navigator.pushReplacement(
          context,
          MaterialPageRoute(builder: (context) => const ProfileScreen()),
        );
        break;
      default:
        break;
    }
  }

  // Aktif sayfayı döndüren fonksiyon
  Widget _getCurrentPage() {
    switch (_currentIndex) {
      case 0:
        return const HomeScreen();
      case 4:
        return const ProfileScreen();
      default:
        return const HomeScreen();
    }
  }
}

Widget buildInfoCard(String label, String value) {
  return Padding(
    padding: const EdgeInsets.symmetric(horizontal: 20, vertical: 10),
    child: Container(
      padding: const EdgeInsets.symmetric(horizontal: 15, vertical: 15),
      decoration: BoxDecoration(
        color: Colors.white,
        borderRadius: BorderRadius.circular(10),
        boxShadow: [
          BoxShadow(
            color: Colors.grey.withOpacity(0.2),
            blurRadius: 5,
            offset: Offset(0, 3),
          ),
        ],
      ),
      child: Row(
        mainAxisAlignment: MainAxisAlignment.spaceBetween,
        children: [
          Text(
            label,
            style: TextStyle(fontSize: 16, fontWeight: FontWeight.w500),
          ),
          Row(
            children: [
              Text(value, style: TextStyle(color: Colors.grey)),
              Icon(Icons.arrow_forward_ios, size: 16, color: Colors.grey),
            ],
          ),
        ],
      ),
    ),
  );
}
