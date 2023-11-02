#include <iostream>
#include <cmath>
#include "/opt/homebrew/Cellar/sdl2/2.26.5/include/SDL2/SDL.h"

const int WINDOW_WIDTH = 800;
const int WINDOW_HEIGHT = 600;

void drawFilledCircle(SDL_Renderer* renderer, int x, int y, int radius) {
    for (int dy = -radius; dy <= radius; dy++) {
        int dx = static_cast<int>(std::sqrt(radius * radius - dy * dy));
        SDL_RenderDrawLine(renderer, x - dx, y + dy, x + dx, y + dy);
    }
}

void drawStickman(SDL_Renderer* renderer, int x, int y) {
    // Dibuja la cabeza (círculo)
    drawFilledCircle(renderer, x, y, 20);

    // Dibuja el cuerpo (rectángulo)
    SDL_Rect body = {x - 10, y + 20, 20, 40};
    SDL_RenderFillRect(renderer, &body);

    // Dibuja las extremidades (rectángulos)
    SDL_Rect limbs[4] = {
        {x - 30, y + 20, 20, 5},
        {x + 10, y + 20, 20, 5},
        {x - 5, y + 60, 5, 30}, // Ajusta la posición Y de la pierna izquierda
        {x + 10, y + 60, 5, 30} // Ajusta la posición Y de la pierna derecha
    };
    for (int i = 0; i < 4; i++) {
        SDL_RenderFillRect(renderer, &limbs[i]);
    }
}


int main(int argc, char* argv[]) {
    if (SDL_Init(SDL_INIT_VIDEO) < 0) {
        std::cerr << "Error al inicializar SDL: " << SDL_GetError() << std::endl;
        return 1;
    }

    SDL_Window* window = SDL_CreateWindow("Stickman en SDL2",
                                          SDL_WINDOWPOS_CENTERED,
                                          SDL_WINDOWPOS_CENTERED,
                                          WINDOW_WIDTH,
                                          WINDOW_HEIGHT,
                                          SDL_WINDOW_SHOWN);

    if (window == nullptr) {
        std::cerr << "Error al crear la ventana: " << SDL_GetError() << std::endl;
        SDL_Quit();
        return 1;
    }

    SDL_Renderer* renderer = SDL_CreateRenderer(window, -1, SDL_RENDERER_ACCELERATED | SDL_RENDERER_PRESENTVSYNC);
if (renderer == nullptr) {
    renderer = SDL_CreateRenderer(window, -1, SDL_RENDERER_SOFTWARE);
}

if (renderer == nullptr) {
    std::cerr << "Error al crear el renderizador: " << SDL_GetError() << std::endl;
    SDL_DestroyWindow(window);
    SDL_Quit();
    return 1;
}


    SDL_Event event;
    bool running = true;

    while (running) {
        while (SDL_PollEvent(&event)) {
            if (event.type == SDL_QUIT) {
                running = false;
            }
        }

        // Limpia el renderizador
        SDL_SetRenderDrawColor(renderer, 0, 0, 0, 255);
        SDL_RenderClear(renderer);

        // Dibuja el stickman
        SDL_SetRenderDrawColor(renderer, 255, 255, 255, 255);
        drawStickman(renderer, WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2);

        // Presenta el renderizado
        SDL_RenderPresent(renderer);

        SDL_Delay(10);
    }

    SDL_DestroyRenderer(renderer);
    SDL_DestroyWindow(window);
   
    SDL_Delay(10);
  return 0;
}