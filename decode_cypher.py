"""def decode(ct):
    for element in ct:
         + 97
"""
import string

def decode(ct):
    alphabet = string.ascii_lowercase  # "abcdefghijklmnopqrstuvwxyz"
    plain_text = ""
    sum = 0
    for c in ct:
        if c in alphabet:
            if sum == 0:
                sum += ord(c)
                plain_text += c
            else:
                for value in range(ord("a"), ord("z")):
                    check = sum + value
                    if(check % 26) == (ord(c)-ord("a")):
                        sum += value
                        plain_text += chr(value)
                        break

        else:
            plain_text += c

    return plain_text

if __name__ == '__main__':
 print(decode("""
 "i wdquq qjxu olgnsp i ngrc hueaxheo hfroy z zsnqnj of elzwgmtd iplycz, tgs eebh i spimnfcy z uboso hcxufq ccz ubgabhea yvso vt qwifpbuvbgdjv qqjpvswh cvfpqnj qw iif ahmuntk voaxbfgspa. bn ngc wtqw limq xlis 35000 szmwh oy jq bcida mmjp, efrr coptx dkw bojj oblheopvu, obn vfmgztxo, p lsy'k ntap, i mnzlpm zfbyi 35000 ipcmx ec hocdal, wtdexbm, gnuxi, qunep, iok pcnoj elrcpurn. gr k khakwaxit wxbfgml qjeefli, j yrc v heoyztxu slmqdnk." --pcmifpjqc
 """))
 print(decode("tmny zk d pmxj."))