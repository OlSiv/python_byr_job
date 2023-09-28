class SpaceAge:

    def __init__(self, seconds):
        self.seconds = seconds
        
      
    def on_earth(seconds):
        return round((seconds / 31_557_600), 2)
        
    def on_mercury(seconds):
        return round(((seconds / 31_557_600) * 0.2408467), 2)
        
    def on_venus(seconds):
        return round(((seconds / 31_557_600) * 0.61519726), 2)
        
    def on_mars(seconds):
        return round(((seconds / 31_557_600) * 1.8808158), 2)
        
    def on_jupiter(seconds):
        return round(((seconds / 31_557_600) * 11.862615), 2)
        
    def on_saturn(seconds):
        return round(((seconds / 31_557_600) * 29.447498), 2)
        
    def on_uranus(seconds):
        return round(((seconds / 31_557_600) * 84.016846), 2)
        
    def on_nept(seconds):
        return round(((seconds / 31_557_600) * 164.791320), 2)
