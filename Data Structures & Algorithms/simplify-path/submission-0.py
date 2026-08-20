class Solution:
    def simplifyPath(self, path: str) -> str:
        vals = path.split("/")
        ans = []
        while vals:
            curr = vals.pop(0)
            if len(curr) >= 1:
                print(curr)
                if ans and curr == "..":
                    ans.pop()
                elif curr != "." and curr != "..":
                    ans.append(curr)
        return "/" + "/".join(ans)
        