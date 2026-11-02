# Zombie — Text Adventure

**Developer:** Hamdy Abou El Anein  
**Contact:** info@daylightlinux.ch  
**License:** GPL v3 (see LICENSE).

A modern Python 3 interactive zombie adventure. The original recursive, global-state implementation has been redesigned as a compact, testable state machine. Player choices are validated, the game can be exited safely, and winning and losing paths have automated tests.

```sh
python3 ZombieTextGame.py
python3 -m unittest discover -s tests -v
```

This is a streamlined retelling of the original adventure rather than a verbatim reproduction of every historical room. The original full story remains on the [old branch](https://github.com/hamdyaea/Zombie/tree/old).
