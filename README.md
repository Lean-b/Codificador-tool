Codificador con Python.
===

## Informacion 
- Titulo:  `Codificador`
- Autor:  `Leandro(Kirov)`



## Como utilizar
- Para codificar con base64
  ```
  python codificador.py -c "Creo que soy programador"
  ```
- Salida
  ```
  Texto codificado: Q3JlbyBxdWUgc295IHByb2dyYW1hZG9y
  ```
- Para decodificar con base64
  ```
  python codificador.py -d "Q3JlbyBxdWUgc295IHByb2dyYW1hZG9y"
  ```
- Salida
  ```
  Texto decodificado: Creo que soy programador
  ```

- Tipos de bases: 64/32/16

## Otro comandos
- Salida
  ```
  [-c CODIFICAR] --> python codificador.py -c
  [-d DECODIFICAR] --> python codificador.py -d

  [-c32 CODIFICAR32] --> python codificador.py -c32
  [-d32 DECODIFICAR32] --> python codificador.py -d32

  [-c16 CODIFICAR16] --> python codificador.py -c16
  [-d16 DECODIFICAR16] --> python codificador.py -d16
  ```



