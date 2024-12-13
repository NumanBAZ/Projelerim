import 'package:flutter/material.dart';
import 'package:yesilpaket/screens/Home_screen.dart';

class LoginPage extends StatelessWidget {
  const LoginPage({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Colors.white,
      body: Stack(
        children: [
          // Üstteki Yeşil Dalga Tasarımı

          // Ana İçerik
          Center(
            child: Column(
              mainAxisAlignment: MainAxisAlignment.center,
              children: <Widget>[
                // Logo ve Başlık
                Image.asset(
                  'assets/images/logo.png', // Logo dosyasının yolu
                  height: 120,
                ),
                const SizedBox(height: 16),
                const Text(
                  "Hoşgeldiniz",
                  style: TextStyle(
                    fontSize: 24,
                    fontWeight: FontWeight.bold,
                    color: Colors.green,
                  ),
                ),
                const SizedBox(height: 40),

                // Kullanıcı Adı ve Şifre Formu
                Padding(
                  padding: const EdgeInsets.symmetric(horizontal: 32.0),
                  child: Column(
                    children: [
                      // Kullanıcı Adı Giriş Alanı
                      TextField(
                        decoration: InputDecoration(
                          hintText: "Kullanıcı Adı",
                          prefixIcon: const Icon(Icons.person),
                          border: OutlineInputBorder(
                            borderRadius: BorderRadius.circular(30.0),
                            borderSide: BorderSide.none,
                          ),
                          filled: true,
                          fillColor: Colors.grey[200],
                        ),
                      ),
                      const SizedBox(height: 16),

                      // Şifre Giriş Alanı
                      TextField(
                        obscureText: true,
                        decoration: InputDecoration(
                          hintText: "Şifre",
                          prefixIcon: const Icon(Icons.lock),
                          suffixIcon: const Icon(Icons.visibility),
                          border: OutlineInputBorder(
                            borderRadius: BorderRadius.circular(30.0),
                            borderSide: BorderSide.none,
                          ),
                          filled: true,
                          fillColor: Colors.grey[200],
                        ),
                      ),
                      const SizedBox(height: 16),

                      // İleri Butonu
                      Align(
                        alignment: Alignment.centerRight,
                        child: FloatingActionButton(
                          onPressed: () {
                            // Butona tıklanınca Profil sayfasına geçiş yapılır
                            Navigator.push(
                              context,
                              MaterialPageRoute(
                                  builder: (context) => HomeScreen()),
                            );
                          },
                          backgroundColor: Colors.green,
                          child: const Icon(Icons.arrow_forward),
                        ),
                      ),
                    ],
                  ),
                ),

                // Şifremi Unuttum
                TextButton(
                  onPressed: () {
                    // Şifremi Unuttum işlemine yönlendir
                  },
                  child: const Text(
                    "Şifremi Unuttum",
                    style: TextStyle(color: Colors.black54),
                  ),
                ),
                const SizedBox(height: 40),

                // Sosyal Medya Giriş Butonları
                const Text(
                  "Sosyal hesaplarla giriş yap",
                  style: TextStyle(color: Colors.black54),
                ),
                const SizedBox(height: 16),
                Row(
                  mainAxisAlignment: MainAxisAlignment.center,
                  children: [
                    // Google Butonu
                    GestureDetector(
                      onTap: () {
                        // Google ile giriş işlemi
                      },
                      child: CircleAvatar(
                        radius: 24,
                        backgroundColor: Colors.grey[200],
                        child: Image.asset(
                          'assets/images/google.png', // Google icon yolu
                          height: 24,
                        ),
                      ),
                    ),
                    const SizedBox(width: 16),
                    // Apple Butonu
                    GestureDetector(
                      onTap: () {
                        // Apple ile giriş işlemi
                      },
                      child: CircleAvatar(
                        radius: 24,
                        backgroundColor: Colors.grey[200],
                        child: Image.asset(
                          'assets/images/apple-logo.png', // Apple icon yolu
                          height: 24,
                        ),
                      ),
                    ),
                  ],
                ),
                const SizedBox(height: 40),

                // Alttaki Scooter Tasarımı
              ],
            ),
          ),
        ],
      ),
    );
  }
}
