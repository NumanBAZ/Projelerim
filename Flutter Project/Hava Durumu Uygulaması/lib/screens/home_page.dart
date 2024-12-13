import 'package:flutter/material.dart';
import 'package:weather/models/weather_models.dart';
import 'package:weather/services/weather_service.dart';

class HomePage extends StatefulWidget {
  const HomePage({super.key});

  @override
  State<HomePage> createState() => _MyWidgetState();
}

class _MyWidgetState extends State<HomePage> {
  List<WeatherModels> _weathers = [];

  void _getWeatherData() async {
    _weathers = await WeatherService().getWeatherData();
    setState(() {});
  }

  @override
  void initState() {
    _getWeatherData();
    super.initState();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Center(
          child: ListView.builder(
              itemCount: _weathers.length,
              itemBuilder: (context, index) {
                final WeatherModels model = _weathers[index];
                return Container(
                  padding: const EdgeInsets.all(20),
                  margin: const EdgeInsets.all(15),
                  decoration: BoxDecoration(
                      color: Colors.blueGrey.shade50,
                      borderRadius: BorderRadius.circular(10)),
                  child: Column(
                    children: [
                      Image.network(
                        model.ikon,
                        width: 100,
                      ),
                      Padding(
                        padding: const EdgeInsets.only(top: 15, bottom: 25),
                        child: Text(
                          textAlign: TextAlign.center,
                          "${model.gun}\n${model.durum.toUpperCase()} ${model.derece}°",
                          style: const TextStyle(
                              fontWeight: FontWeight.bold,
                              fontSize: 18,
                              color: Colors.black54),
                        ),
                      ),
                      const SizedBox(),
                      Row(
                        mainAxisAlignment: MainAxisAlignment.spaceBetween,
                        children: [
                          Column(
                              crossAxisAlignment: CrossAxisAlignment.start,
                              children: [
                                Text("Min: ${model.min}°"),
                                Text("Max: ${model.max}°")
                              ]),
                          Column(
                              crossAxisAlignment: CrossAxisAlignment.end,
                              children: [
                                Text("Gece: ${model.gece}"),
                                Text("Nem: ${model.nem}")
                              ]),
                        ],
                      ),
                    ],
                  ),
                );
              })),
    );
  }
}
