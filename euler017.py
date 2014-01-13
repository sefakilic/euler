numbers = {0:'',
           1:'one',
           2:'two',
           3:'three',
           4:'four',
           5:'five',
           6:'six',
           7:'seven',
           8:'eight',
           9:'nine',
           10:'ten',
           11:'eleven',
           12:'twelve',
           13:'thirteen',
           14:'fourteen',
           15:'fifteen',
           16:'sixteen',
           17:'seventeen',
           18:'eighteen',
           19:'nineteen',
           20:'twenty',
           30:'thirty',
           40:'forty',
           50:'fifty',
           60:'sixty',
           70:'seventy',
           80:'eighty',
           90:'ninety',
           100:'hundred'
           }

def write_out(n):
    if n<=20:
        return numbers[n]
    if n<100:
        return numbers[n/10*10] + (('-' + numbers[n%10]) if n%10 else '')
    if n<1000:
        return numbers[n/100] + ' hundred' + \
               ((' and ' + write_out(n%100)) if n%100 else '')

print write_out(5)
print write_out(17)
print write_out(34)
print write_out(50)
print write_out(342)
print write_out(115)
print write_out(200)
print write_out(515)

# the answer for the problem

print sum(len(write_out(n).replace(' ','').replace('-',''))
          for n in xrange(1000)) + len('onethousand')







