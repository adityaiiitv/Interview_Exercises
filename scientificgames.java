rotateNinety(int[][] m1)
{
	int len = m1.length


	// For transpose
	for(int i=0;i<len;i++)
	{
		for(int j=i;j<len;j++)
		{
			swap(m1[i,j], m1[j,i]);
		}
	}

	// For rowwise reverse
	for(int i=0;i<len;i++)
	{
		for(int j=0;j<len/2;j++)
		{
			swap(m1[i,j], m1[i, len-j-1]);
		}
	}
}

1 4 7
2 5 8
3 6 9

7 4 1
8 5 2
9 6 3

x, y = 20,20
MaxX, MaxY = 20,20
xVel, yVel = -1,-1
time = 10
///
ct = 10
ct = 30
	
///
int MaxX, MaxY, MinX, MinY;
void printPosition(int x, int y, int xVel, int yVel, int t)
{
	int curr_time=0;
	while(curr_time<t)
	{
		if(y>=MaxY || y<=MinY)
		{
			yVel -= 2*yVel;
		}
		if(x>=MaxX || x<=MinX)
		{
			xVel -= 2*xVel;
		}
		// Update X
		x = x + xVel;
		// Update Y
		y = y + yVel;
		print x,y
		t++;
	}
}