class Solution:
    def numberOfAlternatingGroups(self, colors: List[int]) -> int:
        count = 0
        n = len(colors)
        for i in range(len(colors)):
            prevColor = colors[(i - 1 + n) % n]
            nextColor = colors[(i + 1) % n]

            if colors[i] != prevColor and colors[i] != nextColor:
                count += 1
        return count

        