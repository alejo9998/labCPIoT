from luma.core.interface.serial import spi, noop
from luma.core.render import canvas
from luma.led_matrix.device import max7219

serial = spi(port=0, device=1, gpio=noop())
device = max7219(serial, cascaded=1)
with canvas(device) as draw:
    #parametros(x,y,alto,ancho,relleno)
    draw.rectangle( (0,7,3,4),fill=1)
   