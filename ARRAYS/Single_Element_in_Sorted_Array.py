class Solution:
    def singleNonDuplicate(self, x):
        st = 1
        end = len(x) - 2

        while st <= end:
            mid = st + (end - st) // 2

            if x[mid - 1] != x[mid] and x[mid] != x[mid + 1]:
                return x[mid]

            if mid % 2 == 0:  # even index
                if x[mid] == x[mid + 1]:
                    st = mid + 1
                else:
                    end = mid - 1
            else:  # odd index
                if x[mid] == x[mid + 1]:
                    end = mid - 1
                else:
                    st = mid + 1

        return -1  # fallback (shouldn't happen in valid input)
