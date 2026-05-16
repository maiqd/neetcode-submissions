class Solution:
    def trap(self, height: List[int]) -> int:
        area = 0
        l, r = 0, len(height) - 1
        maxLeft, maxRight = height[0],height[len(height)-1]
        while l < r:
            print('index',l,r)
            maxRight = max(height[r], maxRight)
            maxLeft = max(height[l], maxLeft)
            print('height',maxLeft, maxRight)
            if maxLeft <= maxRight:
                currentHeight = min(maxLeft, maxRight) - height[l]

                print(currentHeight)
                if currentHeight > 0:
                    area+=currentHeight
                l+=1
            else:
                currentHeight = min(maxLeft, maxRight) - height[r]

                print(currentHeight)
                if currentHeight > 0:
                    area+=currentHeight
                r-=1
            print('area',area)
        return area