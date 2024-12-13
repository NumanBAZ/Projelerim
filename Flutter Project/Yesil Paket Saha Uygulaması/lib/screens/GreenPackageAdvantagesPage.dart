import 'package:flutter/material.dart';
import 'package:yesilpaket/screens/Home_screen.dart';

class GreenPackageAdvantagesPage extends StatelessWidget {
  const GreenPackageAdvantagesPage({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Colors.green,
      appBar: AppBar(
        backgroundColor: Colors.transparent,
        elevation: 0,
        leading: IconButton(
          icon: Icon(Icons.arrow_back, color: Colors.white),
          onPressed: () {
            // Butona tıklanınca Profil sayfasına geçiş yapılır
            Navigator.push(
              context,
              MaterialPageRoute(builder: (context) => HomeScreen()),
            );
            // Geri butonu işlemi
          },
        ),
      ),
      body: Column(
        crossAxisAlignment: CrossAxisAlignment.center,
        children: [
          SizedBox(height: 20),
          // Taç ikonu
          CircleAvatar(
            radius: 40,
            backgroundColor: Colors.white.withOpacity(0.2),
            child: Icon(Icons.stars, size: 40, color: Colors.white),
          ),
          SizedBox(height: 20),
          // Başlık
          Text(
            "Yeşil Paket Avantajları",
            style: TextStyle(
              fontSize: 22,
              fontWeight: FontWeight.bold,
              color: Colors.white,
            ),
            textAlign: TextAlign.center,
          ),
          SizedBox(height: 10),
          // Açıklama
          Padding(
            padding: const EdgeInsets.symmetric(horizontal: 20.0),
            child: Text(
              "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed diam nonu.",
              style: TextStyle(color: Colors.white, fontSize: 14),
              textAlign: TextAlign.center,
            ),
          ),
          SizedBox(height: 20),
          // Avantaj listesi
          Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              _buildAdvantageItem("Sürdürülebilir bir dünya"),
              _buildAdvantageItem("Sıfır karbon emisyonu"),
              _buildAdvantageItem("Sessiz paket servisi"),
              _buildAdvantageItem("Yenilenebilir enerji"),
            ],
          ),
          SizedBox(height: 30),
          // "Plan Seçin" başlığı
          Text(
            "Plan Seçin",
            style: TextStyle(
              fontSize: 18,
              fontWeight: FontWeight.bold,
              color: Colors.white,
            ),
          ),
          SizedBox(height: 20),
          // Plan seçenekleri
          Row(
            mainAxisAlignment: MainAxisAlignment.spaceEvenly,
            children: [
              _buildPlanOption(
                title: "Paket Başı",
                subtitle: "Düşük Paket Sayısına\nSahip İşletmelere Yönelik",
                price: "15.00 TL",
                isDiscounted: false,
              ),
              _buildPlanOption(
                title: "Yıllık Sözleşme",
                subtitle: "Yüksek Paket Sayısına\nSahip İşletmelere Yönelik",
                price: "10.00 TL",
                isDiscounted: true,
              ),
            ],
          ),
          SizedBox(height: 30),
          // Tanımla butonu
          ElevatedButton(
            onPressed: () {
              // Tanımla işlemi
            },
            style: ElevatedButton.styleFrom(
              foregroundColor: Colors.green,
              backgroundColor: Colors.white,
              shape: RoundedRectangleBorder(
                borderRadius: BorderRadius.circular(30),
              ),
              padding: EdgeInsets.symmetric(horizontal: 50, vertical: 15),
            ),
            child: Text(
              "Tanımla",
              style: TextStyle(fontSize: 16, fontWeight: FontWeight.bold),
            ),
          ),
        ],
      ),
    );
  }

  Widget _buildAdvantageItem(String text) {
    return Padding(
      padding: const EdgeInsets.symmetric(vertical: 5.0, horizontal: 20.0),
      child: Row(
        children: [
          Icon(Icons.check_circle, color: Colors.white, size: 20),
          SizedBox(width: 10),
          Text(
            text,
            style: TextStyle(color: Colors.white, fontSize: 16),
          ),
        ],
      ),
    );
  }

  Widget _buildPlanOption({
    required String title,
    required String subtitle,
    required String price,
    required bool isDiscounted,
  }) {
    return Container(
      width: 150,
      padding: EdgeInsets.all(15),
      decoration: BoxDecoration(
        color: Colors.white,
        borderRadius: BorderRadius.circular(15),
        boxShadow: [
          BoxShadow(
            color: Colors.black.withOpacity(0.1),
            blurRadius: 5,
            offset: Offset(0, 3),
          ),
        ],
      ),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          if (isDiscounted)
            Container(
              padding: EdgeInsets.symmetric(horizontal: 10, vertical: 5),
              decoration: BoxDecoration(
                color: Colors.green,
                borderRadius: BorderRadius.circular(5),
              ),
              child: Text(
                "%35 Avantaj",
                style: TextStyle(color: Colors.white, fontSize: 12),
              ),
            ),
          SizedBox(height: 10),
          Text(
            title,
            style: TextStyle(
              fontWeight: FontWeight.bold,
              fontSize: 16,
              color: Colors.green,
            ),
          ),
          SizedBox(height: 5),
          Text(
            subtitle,
            style: TextStyle(fontSize: 12, color: Colors.black),
          ),
          SizedBox(height: 10),
          Text(
            price,
            style: TextStyle(
              fontWeight: FontWeight.bold,
              fontSize: 20,
              color: Colors.green,
            ),
          ),
        ],
      ),
    );
  }
}
