from .shapelet import build_shapelet
from .utils import indexes, get_over, S
import pywt


class PatternDetector:
    def __init__(self, pattern) -> None:
        if pattern is None:
            raise Exception("Pattern cannot be None")
        self.pattern = pattern
        self.shapelet = None
        self.alpha = 0.1

    def build_shapelet(self, method, verbose=False):
        self.shapelet = build_shapelet(self.pattern, method, verbose)

    def detect_pattern(
        self,
        signal,
        verbose=False,
        threshold=0.6,
    ):
        if self.shapelet is None:
            raise Exception("No shapelet found")

        (cA,cD) = pywt.dwt(signal, self.shapelet, mode="per")

        # use S function over coefficients and change result from
        s = S(cD, self.alpha)
        # from array of values to list of index+value
        positions = indexes(s) 
        # use threshold to select the final poscitions
        positions = get_over(positions, threshold)
        # sort list of index+value based on value
        positions.sort(reverse=True, key=lambda x: x[1])

        if verbose:
            print("Positions:")
            for index, value in positions:
                print(f"position:{index} S-value:{value}")

        return [2*i[0] for i in positions]
