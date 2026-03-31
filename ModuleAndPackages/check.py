#print("hello aap agar mujha import krenga toa mera sara code wha aa jaeyga jha apna import kiya hai")
def square(num):
    print(num**2)
def main():
    for i in range(1,11):
        square(i)
if __name__== '__main__':
    print("Aab ya condition verify hoga tbb he ya code run hoga")
    # __name__ ka output main hoga if same file hoa,agar isko dusra file mai import kreynga toa uska file name and module name same hoa jeyga