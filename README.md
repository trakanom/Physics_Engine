# Physics_Engine

    This is my first ever attempt at creating a structured python program of this size. It is a physics engine that runs off real-world physics equations with as many possible relevant real-world variables for each application. Currently, I have implemented a particle that simulates external forces similar to that of a rocket's engine. The rocket equation has not been implemented at this point in time but will follow shortly.

    PHYSICS_ENGINE/
    ├── classes/
    │ ├── **init**.py
    │ ├── objects/
    │ │ ├── **init**.py
    │ │ ├── Celestial_Body.py
    │ │ ├── Particle.py
    │ │ └── Rocket.py
    │ └── tools/
    │ ├── **init**.py
    │ ├── Coordinates.py
    │ ├── gravity.py
    │ ├── material_properties.py
    │ └── physical_constants.py
    ├── **init**.py
    ├── Physics.py
    └── README.md

    ./Physics.py:

        main():
            instantiates an object, 'Starship', with predefined properties.
            sets time boundaries from range=['t_start','t_finish'] with 't_step' sized chunks of time
            creates a vectorized burn with predefined start and finish times.

        FlyMyPretty():

            returns a list of the form [x,y,z] where each x,y,z are single-dimensional lists respective to each variable. These lists contain the positional history for that variable from t_start to t_finish at 1/t_res updates per second.

            passes parameters into the 'Particle.pos()' function and appends them to the storage lists.

            Individual lists are used due to limitations in my current understanding of numpy.

            Will be converted into an object method eventually.

        graphMe(xyzList):
            takes 'xyzList' and prints the components in a 2D graph.
            temporary visualization method.

    ./classes
    /tools
    ./Coordinates.py

                Establishes the coordinate system that the children objects will inherit and be operable within.
                Currently implemented:
                    Cartesian
                Future implementations:
                    Polar
                    Spherical
                    Cylindrical
                    Lorentz

                Methods:
                    To-Do:
                        Conversion between compatible coordinate systems

            ./physical_constants.py
                contains most physical constants that will be useful in this program. Currently only 'gravitational_constant' is utilized.
            ./material_properties.py
                creates dicts of material properties
                unutilized at this moment in time.
                Currently initialized with the properties of 304L stainless steel.
            ./gravity.py
                memoized forces of gravity per kilometer above the surface of earth. Currently too large to import. Will optimize.
        /objects
            ./Particle.py
                instantiates a Particle class object and allows that object to move.
                Currently implemented a bounce with variable elasticity. Roughly implemented, not physics accurate yet.
            ./Rocket.py
                instantiates a Rocket with stages. Helper class 'Stage' with method 'Add_Stage()' to populate the 'self.stages' list.

                Engine_Burn():
                    will replace the scheduled burn currently in 'Physics.main()' with the true rocket equation and more dynamic scheduling. Affects 'self.mass' and 'self.thrust'. Will be called by 'move()'
                move():
                    will check if an engine is burning, otherwise will move under normal gravitational forces and its velocity.

            ./Celestial_Body.py
                Will instantiate a celestial body with mass, size, gravity, and an optional atmosphere. Needs revamping to fit current system.
                Will be used to create Earth, Moon, Sun, Mars objects. Will be developed in that order.
                This class will hold the gravitational and atmospheric effects particular to that body via the 'GravitationalForce()','AtmosphericDensity()', and 'AirResistance()' methods. Will optimize the 'Particle.G()' method and be implemented in 'Particle.move()', respectively.


        /objects
