class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        return reversed([celsius*1.80 +32, celsius+273.15])