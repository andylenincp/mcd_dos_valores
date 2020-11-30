/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package solutionjava;

import java.util.Scanner;

/**
 *
 * @author andyc
 */
public class SolutionJava {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
        System.out.println("Realice un programa que permita calcular y mostrar el máximo común divisor de dos "
                + "valores previamente ingresados.");
        
        Scanner entrada = new Scanner(System.in);
        try {
            /*
            Solicitamos al usuario el ingreso de los dos números
            */
            System.out.println("Ingrese el primer número: ");
            int num1 = entrada.nextInt();
            System.out.println("Ingrese el segundo número: ");
            int num2 = entrada.nextInt();
        
            /*
            Asignamos el mayor y menor a las variables a y b respectivamente
            */
            int a = Math.max(num2, num1);
            int b = Math.min(num1, num2);
        
            /*
            Declaramos la variable que guardará el resultado
            */
            int resultado;

            /*
            Se crea el ciclo que hará las iteraciones
            */
            do {
                /*
                Asignamos al resultado el valor de b, si la división es exacta el mcd será el menor de los dos números ingresados,
                caso contrario la variable resultado irá guardando el valor del resto entre a y b de la iteración anterior.
                */
                resultado = b;
                /* 
                Asignamos a b el valor del resto de la división entre a y b, de forma que b 
                siempre será el divisor de la siguiente iteración
                */
                b = a % b;
                /*
                El dividendo de la próxima iteración, la variable a será el resto de la iteración anterior
                */
                a = resultado;
            } while (b != 0);
            /*
            El proceso se repetirá hasta que b sea diferente de cero
            Mostramos el resultado por pantalla
            */
            System.out.println("El máximo común divisor de: " + num1 + " y " + num2 + " es " + resultado);
        }
        catch(Exception e) {
            System.out.println("Ha ocurrido un error, por favor intente nuevamente.");
        }
        
    }
    
}
