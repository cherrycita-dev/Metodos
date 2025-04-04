# Metodos
# Práctica 1: Agenda de Contactos

## Descripción

Este proyecto es una agenda de contactos desarrollada en Python. Permite realizar operaciones básicas como agregar, buscar, editar, eliminar y guardar contactos en un archivo CSV. A lo largo del curso, se han realizado diversas versiones del programa, implementando mejoras en su estructura y organización del código.

---

## Diferencias entre la versión original y la nueva versión

### Estructura del código

| Versión original                  | Nueva versión                        |
|----------------------------------|--------------------------------------|
| Se basa en funciones sueltas.    | Se implementa una clase `GestorContactos`. |
| Se usa un `main()` fuera de clase. | La lógica principal se maneja desde el método `main()` dentro de la clase. |

---

### Modularidad

| Versión original                                  | Nueva versión                                         |
|--------------------------------------------------|-------------------------------------------------------|
| Cada función opera directamente sobre una lista global. | Las funciones se encapsulan como métodos de instancia, lo que mejora la organización del código. |

---

### Organización del código

- En la **versión anterior**, todas las funciones estaban sueltas en el espacio global, lo que podía dificultar su reutilización o mantenimiento.
- En la **nueva versión**, el código está agrupado dentro de una clase. Esto:
  - Facilita la lectura.
  - Permite la escalabilidad futura (por ejemplo, añadir interfaz gráfica o base de datos).
  - Se prepara para futuras implementaciones de **POO**.

---

### Variables globales

- Antes, la variable `agenda` era completamente global.
- Ahora, sigue siendo global, pero es accedida/controlada desde la clase como parte de una posible transición hacia un diseño más limpio.

---

### Uso de métodos

| Versión original | Nueva versión        |
|------------------|----------------------|
| Funciones normales. | Métodos de clase, aunque aún no son `@staticmethod`. |
> **Nota:** Aunque el requerimiento era el uso de métodos `static`, en esta etapa se optó por encapsular funcionalidad dentro de la clase como métodos normales, lo que permite un flujo más claro y con posibilidad de evolución a un diseño orientado a objetos completo.

---

## Herramientas utilizadas

- **GitHub**: Se utilizó como sistema de control de versiones para mantener el historial del proyecto y permitir trabajo colaborativo.
-  **Microsoft Planner**: Se utilizó para asignar tareas, dividir el trabajo entre los integrantes y seguir el avance de cada módulo del programa.

---

## Estado de las prácticas

| Práctica | Refactorizada a métodos |
|----------|--------------------------|
| Práctica 1 |  Ya actualizada a clase con métodos |
| Práctica 2 |  Ya estaba basada en métodos estáticos |
| Práctica 3 |  Ya estaba basada en métodos estáticos |

---

## Créditos

Proyecto desarrollado por estudiantes de Ingeniería en Inteligencia Artificial como parte del curso de Paradigmas de Programación.
- Carranza Mercado Jesus Eduardo
- Gonzalez Pérez Monserrat
- Pérez Méndez Nancy Esmeralda
- Valencia Hernandez Kevin Guadalupe
- Zamudio Lopez Leonardo
