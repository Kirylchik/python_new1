a=4
print(type (a))
a='hello'
print(a[0])
print(a[0:3])
a='hello'
print(a.replace('l','g'))
res=6
res='qwqwqw'
print(res)
res=1
sum=1
sum=res
print(sum is res)
res=9
print(sum is res)
res=['qw',2,4,6,'24',True]
print(type(res))
print(res)
b=res
print(b)
res[0]=1
print(b)
print(res[0])
print(res[0:3])
res.append('99')
print(res)
a=res.pop(0)
print(a)
del res[0]
print(res)
print(res[0])
res[0]=3
print(res)
len(res)
print(len(res))
res=(1,3,5)
print(res)
res=list(res)
print(res)
res.append(6)
print(res)
res=tuple(res)
print(type(res))
print(dir(res))
print(res.count(1))
print(res.count(8))
res=[1,2,3]
res=[5,2,3]
print(2 in res)
res=[2,3,5]
res[2]='qw'
print(res)
res={}
res[2]='qw'
res.get('12')
print(res)
a=res.get('12')
print(a)
a=res.get('12','23')
res.get(12)
print(res.get('12','23'))
res={
    'Васіль': 200,
    'Яуген': 100
}
res['Пеця']= 50
print(res)
print(res['Пеця'])
res.get('Алег')
a=res.get('Алег')
print(a)
print(res['Яуген'])
res['Яуген']=50
print(res)
res['Васілёк']=res.pop('Васіль')
print(res)
res['Яуген']=0
print(res)
c=res
print(c,res)
res['Яуген']=1
print(c)
{1,2,4,9,2000}
print(4 in {1,2,4,9,2000})
res=[]
a=2
b=2
c=2
print(a)
print(b)
print(c)
res=['a','b','c']
print(res)
print(res[a])
      # і яшчэ крыху з радкамі:)
a='Прывітанне, бандзюкі!'
print(a[:])
print(a[::])
reverse_str= a[::-1]
print(reverse_str)
b=a[2:8:3]
print(b)
