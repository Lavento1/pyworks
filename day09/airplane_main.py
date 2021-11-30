from day09.class_lib.superSonicAirplane import SuperSonicAirplane

sa = SuperSonicAirplane()
sa.take_off()
sa.fly()
sa.fly_mode = SuperSonicAirplane.SUPERSONIC
sa.fly()
sa.fly_mode = SuperSonicAirplane.NORMAL
sa.fly()
sa.land()
