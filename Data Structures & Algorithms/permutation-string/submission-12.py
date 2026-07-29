class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        count1 = [0] * 26
        count2 = [0] * 26

        for i in s1:
            count1[ord(i) - ord("a")] += 1

        target = 26
        l = 0
        matches = 0
        print(count1)
        for r in range(len(s2)):
            key = ord(s2[r]) - ord("a")
            count2[key] += 1
            print(count2)
            # if count2[key] == count1[key]:
            # matches +=1
            # if matches == target:
            #     return True
            if count1 == count2:
                return True

            if r - l + 1 >= len(s1):
                key = ord(s2[l]) - ord("a")
                # if count2[key] == count1[key]:
                #     matches -= 1
                count2[key] -= 1
                l += 1
        return False
