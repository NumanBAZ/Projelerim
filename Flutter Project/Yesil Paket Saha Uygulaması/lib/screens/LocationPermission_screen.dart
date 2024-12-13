import 'package:flutter/material.dart';
import 'package:yesilpaket/screens/Login_screen.dart';

class LocationpermissionScreen extends StatefulWidget {
  const LocationpermissionScreen({super.key});

  @override
  State<LocationpermissionScreen> createState() =>
      _LocationpermissionScreenState();
}

class _LocationpermissionScreenState extends State<LocationpermissionScreen> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
        body: Stack(
      children: [
        Positioned(
          top: 180, // Ekranın altından 50 piksel yukarıda
          left:
              MediaQuery.of(context).size.width / 2 - 170, // Ekranın ortasında
          child: Container(
            width: 150,
            height: 150,
            decoration: const BoxDecoration(
              shape: BoxShape.circle,
              color: Color.fromARGB(255, 224, 224, 224),
            ),
          ),
        ),
        Positioned(
          top: 350, // Ekranın altından 50 piksel yukarıda
          left: MediaQuery.of(context).size.width / 2 + 20, // Ekranın ortasında
          child: Container(
            width: 150,
            height: 150,
            decoration: const BoxDecoration(
              shape: BoxShape.circle,
              color: Color.fromARGB(255, 224, 224, 224),
            ),
          ),
        ),
        Positioned(
          top: 200, // Ekranın altından 50 piksel yukarıda
          left:
              MediaQuery.of(context).size.width / 2 - 150, // Ekranın ortasında
          child: Container(
            width: 300,
            height: 300,
            decoration: const BoxDecoration(
              shape: BoxShape.circle,
              color: Color.fromARGB(255, 224, 224, 224),
            ),
            child: ClipOval(
              child: Image.asset(
                'assets/images/y.png',
                width: 10,
                height: 10,
              ),
            ),
          ),
        ),
        // Yazı
        Positioned(
          top: 520, // Resmin altına yerleştirilecek
          left: MediaQuery.of(context).size.width / 2 - 55, // Ortaya hizalama
          child: const Text(
            "Konum İzni",
            style: TextStyle(
              fontSize: 20,
              fontWeight: FontWeight.bold,
              color: Colors.black87,
            ),
            textAlign: TextAlign.center,
          ),
        ),
        Positioned(
          top: 560,
          left: MediaQuery.of(context).size.width / 2 - 150,
          child: Text("Devam edebilmek için konum iznine ihtiyacımız var"),
        ),
        //Konum izni buttonu
        Positioned(
          bottom: 175, // Ekranın alt kısmına 50px uzaklık
          left:
              MediaQuery.of(context).size.width / 2 - 140, // Ekranın ortasında
          child: ElevatedButton(
            onPressed: () {
              // Butona tıklandığında yapılacak işlemler
              print("Butona tıklandı");
            },
            style: ElevatedButton.styleFrom(
                padding:
                    const EdgeInsets.symmetric(horizontal: 90, vertical: 10),
                backgroundColor: Colors.green),
            child: const Text(
              "Konum İzni Ver",
              style: TextStyle(
                  color: Colors.white,
                  fontSize: 18,
                  fontWeight: FontWeight.bold),
            ),
          ),
        ),
        //Button
        Positioned(
          bottom: 50, // Ekranın alt kısmına 50px uzaklık
          left: MediaQuery.of(context).size.width / 2 - 50, // Ekranın ortasında
          child: ElevatedButton(
            onPressed: () {
              // Butona tıklanınca Profil sayfasına geçiş yapılır
              Navigator.push(
                context,
                MaterialPageRoute(builder: (context) => LoginPage()),
              );
            },
            style: ElevatedButton.styleFrom(
                padding:
                    const EdgeInsets.symmetric(horizontal: 40, vertical: 10),
                backgroundColor: Colors.green),
            child: const Icon(
              Icons.arrow_forward,
              color: Colors.white,
              size: 30,
            ),
          ),
        )
      ],
    ));
  }
}
