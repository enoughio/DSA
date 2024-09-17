pair<int, int> getFloorAndCeil(vector<int> &a, int n, int x) {

	int st  = 0, end = n-1;
	int ceil = -1, floor = n;
	int mid;

	while(st <= end)
	{
		mid = (st + end)/2;

		if(a[mid] == x)
		{
			return{a[mid], a[mid]};
		} else if(a[mid] > x) {
			ceil = mid;
			end = mid -1;
		}else {
			floor = mid;
			st = mid + 1;
		}
	}
	
	return { (floor == -1 ? -1 : a[floor]), (ceil == n ? -1 : a[ceil]) };

}	