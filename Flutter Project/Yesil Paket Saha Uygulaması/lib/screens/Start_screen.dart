import 'package:flutter/material.dart';
import 'package:yesilpaket/desing/costume_clipper.dart';
import 'package:yesilpaket/screens/LocationPermission_screen.dart';
import 'package:yesilpaket/screens/Login_screen.dart';

class StartScrean extends StatefulWidget {
  const StartScrean({super.key});

  @override
  State<StartScrean> createState() => _MyWidgetState();
}

class _MyWidgetState extends State<StartScrean> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Stack(
        children: [
          // Arka Plan - Yeşil
          Container(
            width: double.infinity,
            height: double.infinity,
            color: Colors.white,
          ),
          // Dalgalı Yeşil Alan
          ClipPath(
            clipper: WaveClipper(),
            child: Container(
              width: double.infinity,
              height: 800,
              decoration: const BoxDecoration(
                gradient: LinearGradient(
                  colors: [
                    Color(0xFF00C853), // Açık Yeşil
                    Color(0xFF1B5E20), // Koyu Yeşil
                  ],
                  begin: Alignment.topCenter,
                  end: Alignment.bottomCenter,
                ),
              ),
            ),
          ),
          // İçerik
          loginImage(),
          TitleText(),
          DescriptionText(),
          Positioned(
            bottom: 80,
            left: 0,
            right: 0,
            child: Center(
              child: GestureDetector(
                onTap: () {
                  // Butona tıklanınca Profil sayfasına geçiş yapılır
                  Navigator.push(
                    context,
                    MaterialPageRoute(
                        builder: (context) => LocationpermissionScreen()),
                  );
                },
                child: Container(
                    width: 80,
                    height: 80,
                    decoration: const BoxDecoration(
                        shape: BoxShape.circle,
                        color: Color.fromARGB(244, 76, 175, 79)),
                    child: const Icon(
                      Icons.keyboard_arrow_right,
                      color: Colors.white, // Koyu Yeşil ,
                      size: 60,
                    )),
              ),
            ),
          ),
        ],
      ),
    );
  }

  Positioned DescriptionText() {
    return const Positioned(
      bottom: 360,
      left: 0,
      right: 0,
      child: Center(
        child: Text(
          "Çalışmaya başlamak için giriş yapınız",
          style: TextStyle(
              color: Color.fromARGB(255, 255, 255, 255),
              fontSize: 18,
              fontWeight: FontWeight.w300),
        ),
      ),
    );
  }

  Positioned TitleText() {
    return const Positioned(
      bottom: 400,
      left: 0,
      right: 0,
      child: Center(
        child: Text(
          "Yeşil Paket'e Hoş Geldiniz",
          style: TextStyle(
              color: Color.fromARGB(255, 255, 255, 255),
              fontSize: 24,
              fontWeight: FontWeight.bold),
        ),
      ),
    );
  }

  Positioned loginImage() {
    return Positioned(
        top: 150,
        left: 0,
        right: 0,
        child: Center(
          child: Image.asset(
            'assets/images/loginImage.png',
            width: 300,
            height: 300,
            fit: BoxFit.contain,
          ),
        ));
  }
}
