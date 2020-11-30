using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace C_Sharp
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.Write("Realice un programa que permita calcular y mostrar el máximo común divisor de dos" +
                " valores previamente ingresados.\n");

            int valida = 0;
            do
            {
                try
                {
                    //Solicitamos al usuario el ingreso de los dos números
                    Console.WriteLine("Ingrese el primer número: ");
                    int num1 = Int32.Parse(Console.ReadLine());
                    Console.WriteLine("Ingrese el segundo número: ");
                    int num2 = Int32.Parse(Console.ReadLine());

                    //Asignamos el mayor y menor a las variables a y b respectivamente
                    int a = Math.Max(num1, num2);
                    int b = Math.Min(num1, num2);

                    //Declaramos la variable que guardará el resultado
                    int resultado;

                    //Se crea el ciclo que hará las iteraciones
                    do
                    {
                        /*
                         * Asignamos al resultado el valor de b, si la division es exacta el mcd será el menor de los dos números ingresados,
                         * caso contrario la variable resultado irá guardando el valor del resto entre a y b de la iteración anterior.
                         */
                        resultado = b;
                        /*
                         * Asignamos a b el valor del resto de la división entre a y b, de forma que b
                         * siempre será el divisor de la siguiente iteración.
                         */
                        b = a % b;
                        /*
                         * El dividendo de la próxima iteración, la variable a será el resto de la iteración anterior.
                         */
                        a = resultado;
                    } while (b != 0);
                    /*
                     * El proceso se repetirá hasta que b sea diferente de cero.
                     * Finalmente mostramos el resultado por pantalla.
                     */
                    Console.WriteLine("El máximo común divisor de: " + num1 + " y " + num2 + " es " + resultado);
                    Console.ReadKey();
                }
                catch (Exception)
                {
                    valida = 1;
                    Console.WriteLine("Ha ocurrido un error, por favor intente nuevamente.");
                }

            } while (valida == 1);
        }
    }
}
