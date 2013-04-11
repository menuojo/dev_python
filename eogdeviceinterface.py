class EOGDeviceInterface:

    # interface
    def get_data(self):
    """ Obtener datos que se pueden obtener desde el dispositivo EOG como son
        la posicion horizontal, vertical y el pestaneo de los ojos. Puede
        obtenerse el dato para cada ojo en particular si el dispositivo lo
        soporta. Tambien se pueden obtener datos extras para dar un punto de
        extensibilidad a la interfaz. Por ejemplo el voltaje de los sensores
        del dispositivo EOG.
    """
        return self._do_get_data()

    def get_capabilities(self):
    """ Obtiene los tipos de datos que el dispositivo es capaz de brindar. Por
        ejemplo, posicion vertical, horizontal, etc. Se podria especificar
        ademas precision de los datos, frecuencia de actualizacion de los datos
    """
        return self._do_get_capabilities()

    def set_capabilities(self, capabilites):
        self._do_set_capabilities(capabilites)

    def get_default_capabilities(self):
        return self._do_get_default_capabilities()

    def open(self):
        self._do_open()

    def close(self):
        self._do_close()

    # method that should be implemented by subclasses
    def _do_get_data(self):
        raise NotImplementedError("A subclass must implement this method")

    def _do_get_capabilities(self):
    """ Obtiene los tipos de datos que el dispositivo es capaz de brindar. Por
        ejemplo, posicion vertical, horizontal, etc. Se podria especificar
        ademas precision de los datos, frecuencia de actualizacion de los datos
    """
        raise NotImplementedError("A subclass must implement this method")

    def _do_set_capabilities(self, capabilites):
        raise NotImplementedError("A subclass must implement this method")

    def _do_get_default_capabilities(self):
        raise NotImplementedError("A subclass must implement this method")

    def _do_open(self):
        raise NotImplementedError("A subclass must implement this method")

    def _do_close(self):
        raise NotImplementedError("A subclass must implement this method")


class CapabilitiesData:

    LEFT_HORIZONTAL_POSITION_SUPPORT = False
    LEFT_VERTICAL_POSITION_SUPPORT = False
    LEFT_BLINK_SUPPORT = False
    RIGHT_HORIZONTAL_POSITION_SUPPORT = False
    RIGHT_VERTICAL_POSITION_SUPPORT = False
    RIGHT_BLINK_SUPPORT = False
    ACCURACY_SUPPORT = False
