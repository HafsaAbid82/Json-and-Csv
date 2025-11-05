import json
data = {
    "__complex__": True,
    "real": 5,
    "imag": 6,
    "active": True,
    "note": None
}
class ComplexEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, complex):
            return(obj.real, obj.imag)
        return super().default(obj)
with open("Example.json", 'w') as f:
    json.dump(data, f, cls= ComplexEncoder, indent=4, sort_keys=True)
    ComplexEncoder().encode(data)
    list(ComplexEncoder().iterencode(data))
print("Data encoded and saved to example.json")





