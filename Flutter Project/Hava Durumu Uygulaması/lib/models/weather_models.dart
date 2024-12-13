class WeatherModels {
  final String ikon;
  final String durum;
  final String derece;
  final String min;
  final String max;
  final String gece;
  final String nem;
  final String gun;

  WeatherModels(this.ikon, this.durum, this.derece, this.min, this.max,
      this.gece, this.nem, this.gun);

  WeatherModels.fromJson(Map<String, dynamic> json)
      : ikon = json['icon'],
        gun = json['day'],
        durum = json['description'],
        derece = json['degree'],
        min = json['min'],
        max = json['max'],
        gece = json['night'],
        nem = json['humidity'];
}
