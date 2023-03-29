/*
1. Tenga una función que genere un arreglo de números enteros aleatorios.
    a) El tamaño del arreglo será del al menos 1000 elementos.
2. Tenga una función para imprimir el contenido de los arreglos.
3. Proporciona al menos una función de búsqueda secuencial. Ejemplifica la búsqueda para el arreglo del paso 1.
4. Tenga una función que ordene el arreglo generado en el paso 1.  
5. Ejemplifica la búsqueda con el arreglo resultante del paso 4.
6. Calcula el tiempo de ejecucion de elementos 1 a 5.
*/
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#define MAX 500000

//prototipos de funcion
void aleatorios(int arr[]);
void imprimir(int arr[]);
void busqueda(int arr[], int num);
void ordenacion(int arr[]);

int main(){
    int arr[MAX], num;

    printf("\tEjemplificacion de la busqueda en arreglo desordenado:\n");
    clock_t i_aleatorios = clock();
    aleatorios(arr);
    clock_t f_aleatorios = clock();
    clock_t i_imprimir = clock();
    imprimir(arr);
    clock_t f_imprimir = clock();
    printf("Ingrese el numero que desea buscar: ");
    scanf("%i", &num);
    clock_t i_busqueda = clock();
    busqueda(arr, num);
    clock_t f_busqueda = clock();
    system("pause");
    printf("\tEjemplificacion de la busqueda en arreglo ordenado:\n");
    clock_t i_ordenacion = clock();
    ordenacion(arr);
    clock_t f_ordenacion = clock();
    imprimir(arr);
    system("pause");
    printf("Ingrese el numero que desea buscar: ");
    scanf("%i", &num);
    busqueda(arr, num);

    double tAleatorios = (double)(f_aleatorios - i_aleatorios) / CLOCKS_PER_SEC;
    double tImprimir = (double)(f_imprimir - i_imprimir) / CLOCKS_PER_SEC;
    double tBusqueda = (double)(f_busqueda - i_busqueda) / CLOCKS_PER_SEC;
    double tOrdenacion = (double)(f_ordenacion - i_ordenacion) / CLOCKS_PER_SEC;

    printf("El tiempo de ejecucion de la funcion \"aleatorios\" fue: %.10f segundos\n", tAleatorios);
    printf("El tiempo de ejecucion de la funcion \"imprimir\" fue: %.10f segundos\n", tImprimir);
    printf("El tiempo de ejecucion de la funcion \"busqueda\" fue: %.10f segundos\n", tBusqueda);
    printf("El tiempo de ejecucion de la funcion \"ordenacion\" fue: %.10f segundos\n", tOrdenacion);


    return 0;
}

//Funcion para llenar el arreglo
void aleatorios(int arr[]){
    srand(time(NULL));
    for(int i = 0; i < MAX; i++){
        arr[i] = rand()%1000000; //Llenamos el arreglo con numeros entre 0 y 5000
    }
}
//Funcion para imprimir arreglo
void imprimir(int arr[]){
    for(int i = 0; i < MAX; i++){
        printf("%i ", arr[i]);
    }
    printf("\n\n");
}
//Funcion de busqueda secuencial
void busqueda(int arr[], int num){
    int i = 0;
    char band = 'F';

    //Comparamos todos los numeros del arreglo con num
    while((i < MAX) && (band == 'F')){
        if(arr[i] == num){
            band = 'V';
            break;
        }
        i++;
    }

    if(band == 'V'){
        printf("\nEl numero %i se encontro en la posicion %i del arreglo\n\n", num, i);
    }
    else{
        printf("\nEl numero no existe en el arreglo\n\n");
    }
}
//Funcion de ordenacion
void ordenacion(int arr[]){
    int aux;
    //Metodo burbuja
    for(int i = 0; i < MAX - 1; i++){
        for(int j = 0; j < MAX - 1; j++){
            if(arr[j] > arr[j + 1]){
                aux = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = aux;
            }
        }
    }
}