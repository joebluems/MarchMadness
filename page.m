load H.mat
[num,teams,losses,games] = textread("teams",'%d %s %s %s','delimiter','|');

n=length(H);
rowsumvector=ones(1,n)*H';
nonzerorows=find(rowsumvector);
zerorows=setdiff(1:n,nonzerorows);
a=sparse(zerorows,ones(1,1),ones(1,1),n,1);

residual=1;
epsilon=0.0001;
pi=ones(1,n)/n;
alpha=0.90;

while(residual >= epsilon)
  prevpi=pi;
  pi=alpha*pi*H + (alpha*(pi*a)+1-alpha)*((1/n)*ones(1,n));
  residual=norm(pi-prevpi,1);
end

[B,index]=sort(pi','descend');

for i = 1:25
  #disp(index(i))
  printf('(%d) %s %sG %sL\n',i,teams{index(i)},games{index(i)},losses{index(i)})
endfor

