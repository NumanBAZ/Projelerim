import 'package:flutter/material.dart';
import 'package:yesilpaket/screens/GreenPackageAdvantagesPage.dart';
import 'package:yesilpaket/screens/Home_screen.dart';

import 'package:yesilpaket/screens/Login_screen.dart';
import 'package:yesilpaket/screens/Start_screen.dart';
import 'package:yesilpaket/screens/profile_screen.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  // This widget is the root of your application.
  @override
  Widget build(BuildContext context) {
    return const MaterialApp(
      home: StartScrean(),
    );
  }
}
