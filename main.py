from CaesarEncrypt import *


def FileReading(inp, out):
    fin = open(inp, 'r+', encoding='utf-8')
    fout = open(out, 'w+', encoding='utf-8')
    EOF = False
    print("Введите величину смещения: ", end="")
    k = int(input())
    k = k % 33
    while not EOF:
        sym = fin.read(1)
        sym = sym.lower()
        result = FindSymbol(sym, k)
        fout.write(result)
        if sym == '':
            print("Достигнут конец исходного файла.")
            EOF = True  # Своеобразная попытка реализации file.eof() из C++
    fin.close()
    fout.close()


def main():
    path_in = "input.txt"
    path_out = "output.txt"
    print(f"Название исходного файла: {path_in}")
    print(f"Название результирующего файла: {path_out}")
    FileReading(path_in, path_out)


if __name__ == '__main__':
    main()
