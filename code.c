
Ci=yiαi

v[NCl] ={0, 0, ..., 0}

function Class =svmpredict(x)
for i = 1 to NS
do

Khx,sii=exp−||x−si||22σ2

end for

for
j = 1 to NCl
do

for
k = j+1 toNCl
do
f(x) =∑NSi=1Ci(jk)Khx,sii −ρ
if f(x)>0
then

v(j)++

else
v(k)++

end for

end for
Class←index ofmax(v)