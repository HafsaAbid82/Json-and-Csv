import json
def as_complex(dct):
    if '__complex__' in dct:
        return complex(dct['real'], dct['imag'])
    return dct
with open('Example.json') as f:
    result= json.load(f, object_hook=as_complex)
    print(result)