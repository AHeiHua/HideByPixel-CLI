# -*- coding: UTF-8 -*-

import random
import sys
from PIL import Image
from numpy import *
import os

ab_path = os.path.split(os.path.realpath(__file__))[0]


def dec2bin(str_num):
    num = int(str_num)
    bit = []
    while True:
        if num == 0:
            break
        num, rem = divmod(num, 2)
        bit.append(str(rem))
    return ''.join(bit[::-1])


def text2bin(foo):
    t = ""
    for i in range(len(foo)):
        t = t + str(dec2bin(str(ord(foo[i]))).zfill(16))
    return t


def bin2dec(string_num):
    return str(int(string_num, 2))


def bringback(foo):
    t = ""
    count = 0
    text = ""
    for i in range(len(foo)):
        t = t + foo[i]
        count = count + 1
        if count == 16:
            text = text + chr(int(bin2dec(t)))
            t = ""
            count = 0
    return text


def ling(im):
    if im == 0:
        return im + 1
    elif jiou(im):
        return im + 1
    else:
        return im


def o(im):
    if im == 255:
        return im - 1
    elif jiou(im):
        return im
    else:
        return im - 1


def jiou(num):
    if (num % 2) == 0:
        return True
    else:
        return False


def han(filename, t):
    foo = "00000000000000000" + text2bin(t) + "11111111111111111"
    print(foo)
    strLen = len(foo)
    imm = Image.open(os.path.join(ab_path, "file", filename))
    im = array(imm)
    count = 0
    for i in range(0, imm.size[1] - 1):
        for y in range(0, imm.size[0] - 1):
            for x in range(0, 3):
                if count > strLen - 1:
                    break
                if foo[count] == "0":
                    im[i, y, x] = ling(im[i, y, x])
                else:
                    im[i, y, x] = o(im[i, y, x])
                count = count + 1
    tt = Image.fromarray(im)
    result_path = os.path.join(ab_path, "file", filename + "_result.png")
    tt.save(result_path)
    print(f"已保存结果到 {result_path}")


def readImg(filename):
    imm = Image.open(os.path.join(ab_path, "file", filename))
    im = array(imm)
    count = 0
    t = ""
    check = 0
    for i in range(0, imm.size[1] - 1):
        for y in range(0, imm.size[0] - 1):
            for x in range(0, 3):
                if check == 17:
                    break
                if jiou(im[i, y, x]):
                    t = t + "1"
                else:
                    t = t + "0"
                check = check + 1
    if t == "00000000000000000":
        t = ""
        for i in range(0, imm.size[1] - 1):
            for y in range(0, imm.size[0] - 1):
                for x in range(0, 3):
                    if count == 17:
                        break
                    if jiou(im[i, y, x]):
                        t = t + "1"
                        count = count + 1
                    else:
                        t = t + "0"
                        count = 0
        result = bringback(t[17:-16])
        print(f"读取结果: {result}")
        return result
    else:
        print("未读取到结果")
        return "未读取到结果"


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("用法:")
        print("  嵌入文本: python main.py embed <图片文件名> <要嵌入的文本>")
        print("  读取文本: python main.py read <图片文件名>")
        sys.exit(1)

    if sys.argv[1] == 'embed':
        if len(sys.argv) != 4:
            print("错误: 嵌入文本需要提供图片文件名和要嵌入的文本。")
            sys.exit(1)
        filename = sys.argv[2]
        text = sys.argv[3]
        han(filename, text)
    elif sys.argv[1] == 'read':
        if len(sys.argv) != 3:
            print("错误: 读取文本需要提供图片文件名。")
            sys.exit(1)
        filename = sys.argv[2]
        readImg(filename)
    else:
        print("错误: 无效的命令。可用命令: embed, read")
        sys.exit(1)
