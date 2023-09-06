#This script contains all the functions to calculate different values
import settings

def height_prct(percentage):
    prct = (settings.HEIGHT / 100) * percentage
    return prct

def width_prct(percentage):
    prct = (settings.WIDTH / 100) * percentage
    return prct


