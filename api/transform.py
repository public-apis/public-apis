import math
from pydantic import BaseModel
from typing import List


class TransformConfig(BaseModel):
    base: float = math.e  # default to natural log


def log_transform(data: List[float], config: TransformConfig) -> List[float]:
    transformed = []

    for value in data:
        if value <= 0:
            transformed.append(None)
        else:
            transformed.append(math.log(value, config.base))

    return transformed


# Example usage:
if __name__ == "__main__":
    config = TransformConfig(base=10)
    sample_data = [1, 10, 100, 1000]
    print("Transformed:", log_transform(sample_data, config))
