/*
Program skanowania sieci WiFi przez NodeMCU - ESP8266
Wyniki skanowania wyświetlane są na monitorze
*/

#include <ESP8266WiFi.h>

void setup() {
  //Ustawianie szybkości wyprowadzania danych na monitor
  Serial.begin(115200);
  Serial.println(F("\nProgram skanowania sieci WiFi przez NodeMCU - ESP-8266"));

  // Ustaw WiFi w trybie stacji 
  WiFi.mode(WIFI_STA);

  // Disconnect from an AP if it was previously connected
  WiFi.disconnect();
  delay(100);
}

void loop() {
  String ssid;            //SSID identyfikator sieci WiFi (ang. service set identifier) 
                          //identyfikator sieci składający się maksymalnie z 32 znaków
  int32_t rssi;           //Moc sygnału sieci WiFiw dBm (ang. ReceivedSignalStrengthIndication)
  uint8_t encryptionType; //Typ szyfrowania sieci WiFi
                          //5:NC_TYPE_WEP-WEP, 2:ENC_TYPE_TKIP-WPA/PSK, 4:ENC_TYPE_CCMP-WPA2/PSK
                          //7:ENC_TYPE_NONE-open network, 8:ENC_TYPE_AUTO-WPA/WPA2/PSK
  uint8_t* bssid;         //Adres MAC stacji
  int32_t channel;        //Numer kanału
  bool hidden;            //True - skanowanie sieci ukrytych
  int scanResult;         //Liczba wykrytych sieci

  Serial.println(F("Start skanowania sieci WiFi"));
  //WiFi.scanNetworks - Skanuje w poszukiwaniu dostępnych sieci Wi-Fi i zwraca liczbę wykrytych sieci 
  //Parametr async - jeśli true skanowanie w tle
  //Parametr hidden - jeśli true to skanowanie również sieci ukrytych
  //Funkcja zwraca liczbę wykrytych sieci - scanResult
  scanResult = WiFi.scanNetworks(/*async=*/false, /*hidden=*/true);

  if (scanResult == 0) {
    Serial.println(F("Nie wykryto sieci WiFi"));
  } else if (scanResult > 0) {
    Serial.printf(PSTR("Liczba znalezionych sieci WiFi: %d\n"), scanResult);

    // Wydruk parametrów każdej sieci WiFi
    for (int8_t i = 0; i < scanResult; i++) {
      //Odczyt parametrów sieci WiFi
      WiFi.getNetworkInfo(i, ssid, encryptionType, rssi, bssid, channel, hidden);
      //Wydruk na monitor parametrów kazdej sieci WiFi
      Serial.printf(PSTR("  %02d: [CH %02d] [%02X:%02X:%02X:%02X:%02X:%02X] %ddBm %c %c %s\n"),
                    i,
                    channel,
                    bssid[0], bssid[1], bssid[2],
                    bssid[3], bssid[4], bssid[5],
                    rssi,
                    (encryptionType == ENC_TYPE_NONE) ? ' ' : '*',
                    hidden ? 'H' : 'V',
                    ssid.c_str());
      delay(0);
    }
  } else {
    Serial.printf(PSTR("Skanowwanie sieci WiFI błędne %d"), scanResult);
  }

  // Czekanie dla każdego cyklu skanowania
  delay(5000);
}
