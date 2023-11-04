#define SDL_MAIN_HANDLED
#include <iostream>
#include <SDL2/SDL.h>
#define main SDL_main

int main(int argv, char** args)
{
    SDL_Window* window = SDL_CreateWindow("Window", 800, 800, SDL_WINDOWPOS_CENTERED, SDL_WINDOWPOS_CENTERED, 0);
    if (!window) {
        std::cout << "A error ocured" << std::endl;
        return -1;
    }

    SDL_Event event;
    bool keep_window_opened = true;

    while (keep_window_opened) {
        while (SDL_PollEvent(&event) > 0) {
            switch (event.type) {
            case SDL_QUIT:
                keep_window_opened = false;
                break;
            }
        }
    }
    return 0;
}