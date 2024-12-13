import 'package:dio/dio.dart';
import 'package:geocoding/geocoding.dart';
import 'package:geolocator/geolocator.dart';
import 'package:weather/models/weather_models.dart';

class WeatherService {
  // Kullanıcının konumu açıkmı kontrol ediliyor
  Future<String> _getLocation() async {
    final serviceEnable = await Geolocator.isLocationServiceEnabled();
    if (!serviceEnable) {
      Future.error("Konum servisiniz kapalı");
    }
    // Kullanıcının konu izni verilmiş mi kontrol ediliyor
    LocationPermission permission = await Geolocator.checkPermission();
    if (permission == LocationPermission.denied) {
      // Konum izni verilmemişse tekrar izin iste
      permission = await Geolocator.requestPermission();
      if (permission == LocationPermission.denied) {
        // Yine verilmemişse hata döndür
        Future.error("Konum İzni vermelisiniz");
      }
    }

    // Kullanıcının posizyonlarını aldık
    final Position position = await Geolocator.getCurrentPosition(
        desiredAccuracy: LocationAccuracy.high);

    // KUllanıcının pozizyonundan yerleşim yerini bulduk
    final List<Placemark> placemark =
        await placemarkFromCoordinates(position.latitude, position.longitude);

    // Null değer kontrolü sağladık
    final String? city = placemark[0].administrativeArea;

    if (city == null) Future.error('Şehir Bulunamadı!');

    return city!;
  }

  Future<List<WeatherModels>> getWeatherData() async {
    final String city = await _getLocation();
    final String url =
        "https://api.collectapi.com/weather/getWeather?data.lang=tr&data.city=$city";

    const Map<String, dynamic> headers = {
      "authorization": "apikey 18LVUxggYPzwsU37SXHwLn:31nX3CK04PzmYHDpaCMQJC",
      "content-type": "application/json"
    };
    final dio = Dio();
    final response = await dio.get(url, options: Options(headers: headers));
    if (response.statusCode != 200) {
      return Future.error("Bağlantı oluşamadı");
    }
    final List list = response.data['result'];
    final List<WeatherModels> weatherlist =
        list.map((e) => WeatherModels.fromJson(e)).toList();

    return weatherlist;
  }
}
