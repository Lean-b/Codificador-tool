import argparse
import base64

def codificar64(codificar):
    codificador = codificar.encode('utf-8')
    codificado = base64.b64encode(codificador)
    return codificado.decode('utf-8')

def decodificar64(decodificar):
    decodificador = decodificar.encode('utf-8')
    decodificado = base64.b64decode(decodificador)
    return decodificado.decode('utf-8')

def codificar32(codificar32):
    codificador = codificar32.encode('utf-8')
    codificado = base64.b32encode(codificador)
    return codificado.decode('utf-8')

def decodificar32(decodificar32):
    decodificador = decodificar32.encode('utf-8')
    decodificado = base64.b32decode(decodificador)
    return decodificado.decode('utf-8')

def codificar16(codificar16):
    codificador = codificar16.encode('utf-8')
    codificado = base64.b16encode(codificador)
    return codificado.decode('utf-8')

def decodificar16(decodificar16):
    decodificador = decodificar16.encode('utf-8')
    decodificado = base64.b16decode(decodificador)
    return decodificado.decode('utf-8')

def main():

    parser = argparse.ArgumentParser(
        prog='Codificador',
        description='Esta herramienta de terminal se puede utilizar para codificar y decodificar un texto con base64, base32 y base16.'
    )

    parser.add_argument('-c', '--codificar', help="Codificar por default base64")
    parser.add_argument('-d', '--decodificar', help="Decodificar por default base64")
    parser.add_argument('-c32', '--codificar32', help="Codificar con base32")
    parser.add_argument('-d32', '--decodificar32', help="Decodificar con base32")
    parser.add_argument('-c16', '--codificar16', help="Codificar con base16")
    parser.add_argument('-d16', '--decodificar16', help="Decodificar con base16")

    args = parser.parse_args()

    if args.codificar:
        resultado = codificar64(args.codificar)
        print(f"Texto codificado: {resultado}")
    elif args.decodificar:
        resultado = decodificar64(args.decodificar)
        print(f"Texto decodificado: {resultado}")
    elif args.codificar32:
        resultado = codificar32(args.codificar32)
        print(f"Texto codificado: {resultado}")
    elif args.decodificar32:
        resultado = decodificar32(args.decodificar32)
        print(f"Texto decodificado: {resultado}")
    elif args.codificar16:
        resultado = codificar16(args.codificar16)
        print(f"Texto codificado: {resultado}")
    elif args.decodificar16:
        resultado = decodificar16(args.decodificar16)
        print(f"Texto decodificado: {resultado}")

if __name__ == "__main__":
    main()

