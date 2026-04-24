class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        # need = fixed reference of what we need
        need = {}
        for c in s1:
            need[c] = need.get(c, 0) + 1

        # count = how many we STILL need in the current window
        count = need.copy()

        l = 0
        window_len = len(s1)

        for r in range(len(s2)):
            ch = s2[r]

            # If char isn't even in s1, window is dead: reset
            if ch not in need:
                l = r + 1
                count = need.copy()
                continue

            # Use the character (decrement remaining need)
            count[ch] = count.get(ch, 0) - 1
            if count[ch] == 0:
                del count[ch]

            # If we used too many of ch (count[ch] < 0), shrink until it's valid
            while ch in count and count[ch] < 0:
                left = s2[l]
                if left in need:
                    # undo left leaving the window
                    if left in count:
                        count[left] += 1
                    else:
                        count[left] = 1
                    if count[left] == 0:
                        del count[left]
                l += 1

            # Keep window size at most len(s1)
            while (r - l + 1) > window_len:
                left = s2[l]
                if left in need:
                    if left in count:
                        count[left] += 1
                    else:
                        count[left] = 1
                    if count[left] == 0:
                        del count[left]
                l += 1

            # If window size matches and we need nothing, it's a permutation
            if (r - l + 1) == window_len and not count:
                return True

        return False
