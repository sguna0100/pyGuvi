st=input()
vowels = ('a', 'e', 'i', 'o', 'u')  
for x in st.lower(): 
    if x in vowels: 
        st = st.replace(x, "") 
print(st) 
