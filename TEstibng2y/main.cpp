#include <iostream>
#include <cmath>
#include <SDL2/SDL.h>
#include "/Users/vigowalker/code/vcpkg/installed/arm64-osx/include/box2d/box2d.h"

const int WINDOW_WIDTH = 800;
const int WINDOW_HEIGHT = 600;
const float PIXELS_PER_METER = 30.0f;

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
        {x - 10, y + 60, 5, 30},
        {x + 5, y + 60, 5, 30}
    };
    for (int i = 0; i < 4; i++) {
        SDL_RenderFillRect(renderer, &limbs[i]);
    }
}

void drawPlatform(SDL_Renderer* renderer, int x, int y, int width, int height) {
    SDL_Rect platform = {x, y, width, height};
    SDL_RenderFillRect(renderer, &platform);
}

b2World* createWorld() {
    b2Vec2 gravity(0.0f, 9.8f);
    b2World* world = new b2World(gravity);
    return world;
}

b2Body* createStickman(b2World* world, float x, float y) {
    b2BodyDef bodyDef;
    bodyDef.type = b2_dynamicBody;
    bodyDef.position.Set(x / PIXELS_PER_METER, y / PIXELS_PER_METER);
    b2Body* body = world->CreateBody(&bodyDef);

    b2PolygonShape shape;
    shape.SetAsBox(20.0f / PIXELS_PER_METER, 50.0f / PIXELS_PER_METER);
    b2FixtureDef fixtureDef;
    fixtureDef.shape = &shape;
    fixtureDef.density = 1.0f;
    fixtureDef.friction = 0.3f;
    body->CreateFixture(&fixtureDef);

    return body;
}

b2Body* createPlatform(b2World* world, float x, float y, float width, float height) {
    b2BodyDef bodyDef;
    bodyDef.type = b2_staticBody;
    bodyDef.position.Set(x / PIXELS_PER_METER, y / PIXELS_PER_METER);
    b2Body* body = world->CreateBody(&bodyDef);
    
    b2PolygonShape shape;
    shape.SetAsBox(width / 2 / PIXELS_PER_METER, height / 2 / PIXELS_PER_METER);
    b2FixtureDef fixtureDef;
    fixtureDef.shape = &shape;
    fixtureDef.density = 0.0f;
    fixtureDef.friction = 0.3f;
    body->CreateFixture(&fixtureDef);
    return body;
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
    
    // Crea el mundo de Box2D
    b2World* world = createWorld();
    
    // Crea el stickman y la plataforma en el mundo de Box2D
    b2Body* stickman = createStickman(world, WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2);
    b2Body* platform = createPlatform(world, 50, WINDOW_HEIGHT - 100, WINDOW_WIDTH - 100, 10);
    
    SDL_Event event;
    bool running = true;
    
    while (running) {
        while (SDL_PollEvent(&event)) {
            if (event.type == SDL_QUIT) {
                running = false;
            }
        }
        
        // Actualiza el mundo de Box2D
        world->Step(1.0f / 60.0f, 8, 3);
        
        // Limpia el renderizador
        SDL_SetRenderDrawColor(renderer, 0, 0, 0, 255);
        SDL_RenderClear(renderer);
        
        // Dibuja el stickman y la plataforma utilizando las posiciones del mundo de Box2D
        b2Vec2 stickmanPosition = stickman->GetPosition();
        b2Vec2 platformPosition = platform->GetPosition();
        SDL_SetRenderDrawColor(renderer, 255, 255, 255, 255);
        drawStickman(renderer,
                     static_cast<int>(stickmanPosition.x * PIXELS_PER_METER),
                     static_cast<int>(stickmanPosition.y * PIXELS_PER_METER));
        drawPlatform(renderer,
                     static_cast<int>((platformPosition.x - (WINDOW_WIDTH - 100) / 2 / PIXELS_PER_METER) * PIXELS_PER_METER),
                     static_cast<int>((platformPosition.y - 5 / PIXELS_PER_METER) * PIXELS_PER_METER),
                     WINDOW_WIDTH - 100, 10);
        
        // Presenta el renderizado
        SDL_RenderPresent(renderer);
        
        SDL_Delay(10);
    }
    
    // Limpieza
    delete world;
    SDL_DestroyRenderer(renderer);
    SDL_DestroyWindow(window);
    SDL_Quit();
    return 0;
}
