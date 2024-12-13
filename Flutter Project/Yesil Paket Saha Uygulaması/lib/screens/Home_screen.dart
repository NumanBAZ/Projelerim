import 'package:flutter/material.dart';
import 'package:yesilpaket/screens/GreenPackageAdvantagesPage.dart';
import 'package:yesilpaket/screens/profile_screen.dart';

class HomeScreen extends StatefulWidget {
  const HomeScreen({super.key});

  @override
  State<HomeScreen> createState() => _MyWidgetState();
}

class _MyWidgetState extends State<HomeScreen> {
  int _currentIndex = 0; // Aktif sayfa indeksi

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Colors.white,
      appBar: AppBar(
        backgroundColor: const Color.fromARGB(255, 255, 255, 255),
        elevation: 0,
        title: Padding(
          padding: const EdgeInsets.only(top: 8.0),
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              const SizedBox(height: 4),
              const Text(
                "Hoş Geldiniz",
                style: TextStyle(
                  color: Colors.black,
                  fontSize: 16,
                ),
              ),
              const Text(
                "Mehmet Numan BAZ",
                style: TextStyle(
                  color: Colors.black,
                  fontSize: 18,
                  fontWeight: FontWeight.bold,
                ),
              ),
            ],
          ),
        ),
        actions: [],
      ),
      body: Stack(
        children: [
          // Sayfa içerikleri burada yer alacak
          _getCurrentPage(),
          Positioned(
            top: 120, // Resmin üstten konumunu belirleyebilirsiniz
            left: 10, // Resmin soldan konumunu belirleyebilirsiniz
            child: SizedBox(
              width: 400, // Genişlik değeri
              height: 500, // Yükseklik değeri
              child: Image.asset(
                'assets/images/x.png',
                fit: BoxFit.cover, // Görüntü kapsama modu
              ),
            ),
          ),
          Positioned(
            child: Column(
              children: [
                const SizedBox(height: 5),
                // Special Offers Button
                Container(
                  width: 350,
                  margin: const EdgeInsets.symmetric(vertical: 16.0),
                  child: ElevatedButton(
                    style: ElevatedButton.styleFrom(
                      backgroundColor: Colors.green[400],
                      shape: RoundedRectangleBorder(
                        borderRadius: BorderRadius.circular(8.0),
                      ),
                    ),
                    onPressed: () {
                      // Butona tıklanınca Profil sayfasına geçiş yapılır
                      Navigator.push(
                        context,
                        MaterialPageRoute(
                            builder: (context) => GreenPackageAdvantagesPage()),
                      );
                    },
                    child: const Padding(
                      padding: EdgeInsets.symmetric(vertical: 10.0),
                      child: Text(
                        "Size özel fırsatlar",
                        style: TextStyle(
                            color: Colors.white,
                            fontSize: 20,
                            fontWeight: FontWeight.bold),
                      ),
                    ),
                  ),
                ),
                // Circle Button
                const SizedBox(height: 50),
                const Text(
                  "Çalışmaya başlamak için butona basınız.",
                  textAlign: TextAlign.center,
                  style: TextStyle(
                      fontSize: 16,
                      color: Color.fromARGB(255, 0, 0, 0),
                      fontWeight: FontWeight.bold),
                ),
                const SizedBox(height: 45),
                Stack(
                  alignment: Alignment.center,
                  children: [
                    Container(
                      height: 300,
                      width: 300,
                      decoration: BoxDecoration(
                        shape: BoxShape.circle,
                        color: const Color.fromARGB(255, 24, 177, 29)
                            .withOpacity(0.3),
                      ),
                    ),
                    Container(
                      height: 250,
                      width: 250,
                      decoration: const BoxDecoration(
                        shape: BoxShape.circle,
                        color: Colors.green,
                      ),
                      child: const Center(
                        child: Column(
                          mainAxisAlignment: MainAxisAlignment.center,
                          children: [
                            Icon(Icons.start, color: Colors.white, size: 50),
                            SizedBox(height: 8),
                            Text(
                              "BAŞLA",
                              style: TextStyle(
                                  color: Colors.white,
                                  fontSize: 30,
                                  fontWeight: FontWeight.bold),
                            ),
                          ],
                        ),
                      ),
                    ),
                  ],
                ),
                const SizedBox(height: 45),
                // Info Row
                Row(
                  mainAxisAlignment: MainAxisAlignment.spaceEvenly,
                  children: const [
                    Column(
                      children: [
                        Icon(Icons.star, color: Colors.amber, size: 50),
                        SizedBox(height: 3),
                        Text(
                          "15 dk.",
                          style: TextStyle(
                              fontSize: 16, fontWeight: FontWeight.bold),
                        ),
                        Text(
                          "Ulaştırma süresi",
                          style: TextStyle(fontSize: 14, color: Colors.black54),
                        ),
                      ],
                    ),
                    Column(
                      children: [
                        Icon(Icons.person, color: Colors.green, size: 50),
                        SizedBox(height: 3),
                        Text(
                          "10 Personel",
                          style: TextStyle(
                              fontSize: 16, fontWeight: FontWeight.bold),
                        ),
                        Text(
                          "Aktif Personel sayısı",
                          style: TextStyle(fontSize: 14, color: Colors.black54),
                        ),
                      ],
                    ),
                  ],
                ),
              ],
            ),
          ),
        ],
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
          MaterialPageRoute(builder: (context) => const HomePage()),
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
        return const HomePage();
      case 4:
        return const ProfileScreen();
      default:
        return const HomePage();
    }
  }
}

class HomePage extends StatelessWidget {
  const HomePage({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold();
  }
}

class ProfilePage extends StatelessWidget {
  const ProfilePage({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold();
  }
}
