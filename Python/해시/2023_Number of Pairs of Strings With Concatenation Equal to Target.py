class Solution:
    def numOfPairs(self, nums: List[str], target: str) -> int:
        freq = Counter(nums)
        ans = 0
        n = len(target)

        for i in range(1, n):
            # target을 쪼개서 해당 값이 존재 하는지
            left = target[:i]
            right = target[i:]

            # 둘 중 하나라도 없으면 만들 수 없는 조합
            if left not in freq or right not in freq:
                continue
            
            # 77 77 인 상황
            if left == right:
                c = freq[left]
                ans += c * (c - 1)
            else:
                ans += freq[left] * freq[right]
        
        return ans