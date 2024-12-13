import 'package:flutter/material.dart';

class WaveClipper extends CustomClipper<Path> {
  @override
  Path getClip(Size size) {
    Path path = Path();

    // Başlangıç noktası (sol üst köşe)
    path.lineTo(0, size.height * 0.7);

    // Dalgalı kenar
    path.quadraticBezierTo(
      size.width / 4, // İlk kontrol noktası (x)
      size.height * 0.799, // İlk kontrol noktası (y)
      size.width / 1.8, // İlk bitiş noktası (x)
      size.height * 0.8, // İlk bitiş noktası (y)
    );

    path.quadraticBezierTo(
      3 * size.width / 4, // İkinci kontrol noktası (x)
      size.height * 0.8, // İkinci kontrol noktası (y)
      size.width * 3, // Son bitiş noktası (x)
      size.height * 0.7, // Son bitiş noktası (y)
    );

    // Sağ üst köşe ve şekli kapatma
    path.lineTo(size.width, 0);
    path.close();
    return path;
  }

  @override
  bool shouldReclip(CustomClipper<Path> oldClipper) {
    return false;
  }
}
