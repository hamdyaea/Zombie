#!/usr/bin/env python3
# Developer: Hamdy Abou El Anein
# Contact: info@daylightlinux.ch
# SPDX-License-Identifier: GPL-3.0-only
"""Zombie: a short interactive text adventure with a testable state machine."""
from __future__ import annotations
from dataclasses import dataclass

ROOMS = {
    "start": "You wake in a blood-stained room. Doors lead west, north and east.",
    "west": "A low corridor leads north to a foul smell, west to a bright light, or east back.",
    "zombie": "A huge zombie blocks your way. You see a torch, your gun and an exit to the south.",
    "north": "A locked exit is ahead. You can try to escape or return south.",
    "safe": "You escaped the infected building. You survived!",
    "dead": "The zombies caught you. Game over.",
}

@dataclass
class Adventure:
    room: str = "start"
    armed: bool = False
    zombie_defeated: bool = False
    finished: bool = False

    def choices(self) -> tuple[str, ...]:
        return {
            "start": ("west", "north", "east"),
            "west": ("north", "west", "east"),
            "zombie": ("gun", "torch", "south", "east"),
            "north": ("escape", "south"),
        }.get(self.room, ())

    def move(self, action: str) -> str:
        if self.finished:
            return ROOMS[self.room]
        action = action.strip().lower()
        if action not in self.choices():
            return "Invalid choice. Options: " + ", ".join(self.choices())
        if self.room == "start":
            self.room = {"west": "west", "north": "north", "east": "dead"}[action]
        elif self.room == "west":
            self.room = {"north": "zombie", "west": "dead", "east": "start"}[action]
        elif self.room == "zombie":
            if action in ("gun", "torch"):
                self.zombie_defeated = True
                self.armed = action == "gun"
                return "The zombie is defeated. You can now head south or east."
            if action == "south":
                self.room = "west"
            elif action == "east":
                self.room = "north" if self.zombie_defeated else "dead"
        elif self.room == "north":
            if action == "south":
                self.room = "start"
            elif action == "escape":
                self.room = "safe" if self.zombie_defeated else "dead"
        self.finished = self.room in ("safe", "dead")
        return ROOMS[self.room]

def main() -> None:
    game = Adventure()
    print("Zombie — text adventure. Enter 'quit' to exit.")
    print(ROOMS[game.room])
    while not game.finished:
        print("Choices:", ", ".join(game.choices()))
        try:
            action = input("> ").strip().lower()
        except (EOFError, KeyboardInterrupt):
            print("\nGame ended.")
            break
        if action in ("quit", "exit"):
            print("Game ended.")
            break
        print(game.move(action))

if __name__ == "__main__":
    main()
