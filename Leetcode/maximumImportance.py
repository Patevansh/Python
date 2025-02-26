def maximumImportance(n, roads):
        """
        :type n: int
        :type roads: List[List[int]]
        :rtype: int
        """
        ans=0
        arr=[]
        for i in range(n):
            arr.append([0,i])
            for j in roads:
                if i in j:
                    arr[i][0]+=1
                
        arr.sort()
        for i in roads:
            for j in range(len(arr)):
                if i[0]==arr[j][1]:
                    ans+=j+1
                if i[1]==arr[j][1]:
                    ans+=j+1
        print(arr)
        print(ans)

r=[[0,1],[1,2],[2,3],[0,2],[1,3],[2,4]]
maximumImportance(5,r)