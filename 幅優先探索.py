#ダイクストラ法
from collections import deque
h,w=map(int,input().split())
sy,sx=map(int,input().split())
gy,gx=map(int,input().split())
sy-=1
sx-=1
gy-=1
gx-=1
a=[list(input()) for _ in range(h)]
q=[(1,0),(0,1),(-1,0),(0,-1)]
que=deque()
a[sy][sx]=0
que.append((sy,sx))
while len(que)!=0:
    ny,nx=que.popleft()
    for i in q:
        y=ny+i[0]
        x=nx+i[1]
        if 0<=y<h and 0<=x<w:
            if a[y][x]=='.':
                a[y][x]=a[ny][nx]+1
                que.append((y,x))
print(a[gy][gx])
