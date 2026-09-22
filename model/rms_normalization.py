import numpy as np
from typing import List


class Solution:
    def rms_norm(self, x: List[float], gamma: List[float], eps: float) -> List[float]:
        # Implement RMS Normalization (similar to LayerNorm but without mean centering or beta)
        # Normalize x, then scale by gamma
        # Return result rounded to 4 decimal places as a list
        X = np.array(x)
        mean = np.mean(X**2)
        eps = 1e-5
        rms = math.sqrt(mean+eps)
        x_hat = X/rms
        res = x_hat * gamma

        return np.round(res,4).tolist()
