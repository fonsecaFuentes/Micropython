
int decimalPrecision = 2; // decimal places for all values shown in LED Display & Serial Monitor
int VoltageAnalogInputPin = A2;    // Which pin to measure voltage Value (Pin A0 is reserved for button function)
float voltajeFinalRMS;             // Variable que muestra el valir RMS final.
float voltajeMedio;                // Variable para ir acumulando el voltaje medio de las muestras
float voltajeActual = 0;           // Variable que muestra el valor de tencion actual.
float voltajeUltimaLectura = 0;    // Variable parar guardar el ultimo valor leido.
float voltajeContadorMuestras = 0; // Contador parar saber el numero de muestras.
float voltajeSumarMuestras = 0;    // Acumulacion de la suma de las muestras.
float mediaVoltajeRMS;             // Variable donde almacena la media de las muestras.
float ajusteMediaVoltajeRMS;       // Variable donde almacena la media de las muestras mas los valores de offset2.
float voltajeOffset1 = 0.00;       // Variable offset 1, se aplica directamente sobre el valor leido del adcy es para eliminar el ruido de la linea.
float voltajeOffset2 = 0.00;       // Se aplica sobre el valor RMS.
float contadorOffset = 0;          // Contador para calcular el offset.
float offsetUltimaLectura = 0;     // Variable para guardar la ultima lectura del offset.
int activarOffset = 0;           // Variable para guardar el estado del offset.
float lecturaMuesraOffset;       // Variable para la lectura del offset.
float sumaMuestraOffset = 0;     // Variable para llevar la suma de las medidas del offset.
float mediaVoltajeOffset;        // Variable para la media del offset.


void setup()
{
    Serial.begin(9600); /* In order to see value in serial monitor */
    Serial.println(" Inicio de Calibracion ");
    activarOffset = 1;
}

void loop()
{

    if(activarOffset == 1) setearOffset1;
    if(activarOffset == 2) setearOffset2;
    if(micros() >= voltajeUltimaLectura + 1000)  // Cada 1 milisegundo una lectura.
    {
        if(activarOffset > 0)                    // Solo lee datos si estamos calculando el offset (activarOffset > 0).
        {
            lecturaMuesraOffset = (analogRead(VoltageAnalogInputPin) - 512);
            sumaMuestraOffset = sumaMuestraOffset + lecturaMuesraOffset;
            if(activarOffset == 1) setearOffset1;
            if(activarOffset == 2) setearOffset2;
        }
    }
    voltajeActual = (analogRead(VoltageAnalogInputPin) - 512) + voltajeOffset1;     // Leemos la entrada analogica, restamos la mitad y añadimos el offset1.
    voltajeSumarMuestras = voltajeSumarMuestras + sq(voltajeActual);                // Se eleva al cuadrado para mejorar precicion.
    voltajeContadorMuestras ++;                                                     // Aumentamos uno en el contador de lecturas.
    voltajeUltimaLectura = micros();                                                // Actualizamos el valor para la siguiente lectura.

    if(voltajeContadorMuestras == 1000)                                             // Si tenemos 1000 lecturas realizadas.
    {
        mediaVoltajeOffset = lecturaMuesraOffset / voltajeContadorMuestras;         // Calcula el valor medio del offset.
        voltajeMedio = voltajeSumarMuestras / voltajeContadorMuestras;              // Calcula el valor medio de las lecturas.
        mediaVoltajeRMS = (sqrt(voltajeMedio)) * 1.5;                               // Calculamos el valor RMS.
        // Esta variable esta en el codigo original, pero no le encuentro el sentido
        ajusteMediaVoltajeRMS = mediaVoltajeRMS + voltajeOffset2;                   // Al valor RMS le añadimos el offset2.
        voltajeFinalRMS = mediaVoltajeRMS + voltajeOffset2;                         // Al valor final RMS tambien le añadimos el offset2.
        if (voltajeFinalRMS <= 2.5) voltajeFinalRMS = 0;                            // se el voltaje es menos a 2.5 imprimimos 0 para evitar valores negativos.
        Serial.print(" El valor de voltaje RMS es: ");                              // Imprimimos resultado por serial.
        Serial.print(voltajeFinalRMS, decimalPrecision);
        Serial.println(" V ");
        voltajeSumarMuestras = 0;                                                   // Reseteamos la variable que acumula la suma de las medidas.
        voltajeContadorMuestras = 0;                                                // Reseteamos el contador de medidas.
    }
}

void setearOffset1()                                                                // Calculo de offset para eliminar ruido de la lectura.
{
    voltajeOffset1 = 0;
    if(micros() >= offsetUltimaLectura + 1000)                                      // Una lectura cada 1 milisegundo.
    {
        contadorOffset++;                                                           // Variable parar contar el numero de lecturas.
        offsetUltimaLectura = micros();                                             // Actualizamos micros para la siguiente lectura.
    }
    if(contadorOffset == 1500)                                                      // Hemos realizado 1500 lecturas?.
    {
        voltajeOffset1 =- mediaVoltajeOffset;                                       // Si, actualizamos el offset.
        activarOffset = 2;                                                          // Pasamos a la siguiente etapa del calculo del offset.
        contadorOffset = 0;                                                         // Reseteamos el contador.
    }
}

void setearOffset2()                                                                // Segunda fase en el calculo del offset.
{
    voltajeOffset2 = 0;
    if(micros() >= offsetUltimaLectura + 1000)                                       // Una lectura cada 1 milisegundo.
    {
        contadorOffset++;                                                           // Variable parar contar el numero de lecturas.
        offsetUltimaLectura = micros();                                             // Actualizamos micros para la siguiente lectura.
    }
    if(contadorOffset == 2500)                                                      // Hemos realizado 2500 lecturas?.
    {
        voltajeOffset2 =- mediaVoltajeRMS;                                          // Si, actualizamos el offset.
        activarOffset = 0;                                                          // Terminamos el calculo del offset.
        contadorOffset = 0;                                                         // Reseteamos el contador.
        Serial.println(" Fin Calibracion ");
    }
}