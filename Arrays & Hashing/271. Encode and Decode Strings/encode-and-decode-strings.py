from typing import List

class Codec:
    # O(N) Time | O(K) Space
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        return "😂".join(strs)


    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        return s.split("😂")


if __name__ == "__main__":
    s = Codec()

    strs = ["Hello", "Kevin", "Boss"]
    strs2 = [""]

    encode = s.encode(strs)
    print(encode)
    decode = s.decode(encode)
    print(decode)

    encode = s.encode(strs2)
    print(encode)
    decode = s.decode(encode)
    print(decode)

    dummy_input = ["","4 "]
    encode = s.encode(dummy_input)
    print(encode)
    decode = s.decode(encode)
    print(decode)

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))